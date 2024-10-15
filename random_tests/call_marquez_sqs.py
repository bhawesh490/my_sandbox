import boto3
import json
import logging
from datetime import datetime
import time
import os
import jsonschema
from jsonschema import validate
from schema import log_stats_schema
import traceback
import re
from openlineage.client.serde import Serde
from openlineage.client import OpenLineageClient

# Initialize the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize the SQS client
sqs_client = boto3.client('sqs', region_name='eu-west-1')

# SQS queue URL
queue_url = 'https://sqs.eu-west-1.amazonaws.com/035328922125/sqs-lineage-target-queue'

# Initialize the OpenLineage client
url = 'your_openlineage_url'  # Replace with your OpenLineage URL
client = OpenLineageClient(url=url)

def receive_messages():
    response = sqs_client.receive_message(
        QueueUrl=queue_url,
        AttributeNames=['All'],
        MaxNumberOfMessages=10,
        MessageAttributeNames=['All'],
        VisibilityTimeout=30,
        WaitTimeSeconds=20
    )
    return response.get('Messages', [])

def process_message(message_body):
    log_stats_data = []
    dq_event = []

    try:
        log_data = json.loads(message_body)
        validate(instance=log_data, schema=log_stats_schema)
        log_stats_data.append(log_data)

        for log_data in log_stats_data:
            job_name = log_data.get('job_name')
            job_run_id = log_data.get('job_id')
            account_id = log_data.get('account_id')
            account_name = log_data.get('account_name')
            account_region = log_data.get('account_region')
            execution_Id = log_data.get('execution_id')

            job_step = log_data.get('job_step').split(': ')[-1] if log_data.get('job_step', None) else None
            start_time = log_data.get('start_time')
            end_time = log_data.get('end_time', None)
            job_id = log_data.get('job_id') if 'Running_Locally' in log_data.get('job_id') else log_data.get('job_id').split('_')[-1]

            parent_job = log_data.get('parent_job', None)

            if log_data.get('log_stat_type')[0] == 'job_metrics':
                src_dataset_name = log_data.get('job_metrics').get('source_datset_name')
                target_dataset_name = log_data.get('job_metrics').get('target_dataset_name')
                job_name = job_name + f"_{target_dataset_name}"
                layers = log_data.get('job_metrics').get('layer', False)
                target_schema = log_data['job_metrics'].get('schema')
                source_schema = log_data['job_metrics'].get('src_schema')
                row_count = log_data['job_metrics'].get('inserted_records')

                source_sch_facet = create_schema_fields(source_schema)
                target_sch_facet = create_schema_fields(target_schema)

                source_dataset = create_dataset(namespace=namespace, dataset_name=src_dataset_name,
                                                schema_facet=source_sch_facet)
                if not layers:
                    target_dataset = [create_dataset(namespace=namespace, dataset_name=target_dataset_name,
                                                    schema_facet=target_sch_facet)]
                else:
                    target_dataset = [create_dataset(namespace=namespace, dataset_name=target_dataset_name + "_dl1", schema_facet=target_sch_facet),
                                    create_dataset(namespace=namespace, dataset_name=target_dataset_name + "_dl2", schema_facet=target_sch_facet)]

                start_event, end_event = create_run_event(job_name=job_name, sql=None, spark=True,
                                                        source_dataset=[source_dataset], target_dataset=target_dataset,
                                                        start_time=start_time, end_time=end_time, s3_location="",
                                                        src_location=None, parent_facet=None,job_run_id=job_run_id,
                                                        account_id=account_id, account_name=account_name, account_region=account_region,
                                                        execution_Id=execution_Id)


            if log_data.get('log_stat_type')[0] == 'data_quality_metrics':
                src_dataset_name = log_data.get('dataset_name')
                data_quality_metrics = log_data.get('data_quality_metrics').get('data_quality_metrics_list')
                source_schema = log_data['data_quality_metrics'].get('schema')

                for each in data_quality_metrics:
                    pattern = r"\(([^()]+),None\)"
                    # Search for the pattern in the input string
                    match = re.search(pattern, each.get('dq_constraint_name'))

                    # Extract the matched group
                    if match:
                        extracted_value = match.group(1)
                        each["dq_constraint_name"] = extracted_value
                        each["dq_constraint_rule"] = each["dq_constraint_rule"].split("(")[0]

                dq_facet = create_dq_facet(data_quality_metrics)

                source_sch_facet = create_schema_fields(source_schema)
                target_sch_facet = create_schema_fields(source_schema)

                source_dataset = create_dataset(namespace=namespace, dataset_name=src_dataset_name,
                                                schema_facet=source_sch_facet)

                target_dataset = [create_dataset(namespace=namespace, dataset_name=src_dataset_name,
                                                    schema_facet=target_sch_facet, dq_facet=dq_facet)]


                start_dq_event, end_dq_event = create_run_event(job_name=job_name+src_dataset_name, sql=None, spark=True,
                                                        source_dataset=[source_dataset], target_dataset=target_dataset,
                                                        start_time=start_time, end_time=end_time, s3_location='',
                                                        src_location=None, job_run_id=job_run_id,
                                                        account_id=account_id, account_name=account_name, account_region=account_region,
                                                        execution_Id=execution_Id)
                dq_event.append(start_dq_event)
                dq_event.append(end_dq_event)

            if parent_job:
                # Define the parent job
                parent_run_id = str(generate_new_uuid())
                parent_job_namespace = namespace
                parent_job_name = job_name

                parent_run = Run(runId=parent_run_id)
                parent_job = Job(namespace=parent_job_namespace, name=parent_job_name)

                parent_run_facet = ParentRunFacet(run=parent_run, job=parent_job)

            print(Serde.to_json(start_event))
            print(Serde.to_json(end_event))
            client.emit(start_event)
            client.emit(end_event)
            for each_event in dq_event:
                client.emit(each_event)

    except jsonschema.exceptions.ValidationError as ve:
        raise Exception(f'Invalid JSON: {ve.message}')
    except Exception as e:
        traceback.print_exc()
        raise e

if __name__ == "__main__":
    while True:
        messages = receive_messages()
        if not messages:
            break
        for message in messages:
            process_message(message['Body'])
            sqs_client.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )
            logger.info(f"Deleted message: {message['ReceiptHandle']} from the queue")
