import os
import json
import re
import boto3

#!/usr/bin/env python3
from openlineage.client.run import (
    RunEvent,
    RunState,
    Run,
    Job,
    Dataset,
    OutputDataset,
    InputDataset,
)
from openlineage.client.client import OpenLineageClient, OpenLineageClientOptions
from openlineage.client.facet import DataQualityAssertionsDatasetFacet, Assertion
from openlineage.client.facet import (
    SqlJobFacet,
    SchemaDatasetFacet,
    SchemaField,
    OutputStatisticsOutputDatasetFacet,
    SourceCodeLocationJobFacet,
    NominalTimeRunFacet,
    DataQualityMetricsInputDatasetFacet,
    ColumnMetric,
)
from openlineage.client.facet import JobTypeJobFacet
from openlineage.client.uuid import generate_new_uuid
from datetime import datetime, timezone, timedelta
import time
from random import random
from openlineage.client.facet import ParentRunFacet

PRODUCER = f"https://github.com/openlineage-user"
namespace = "se-intelds-kpi"
dag_name = "user_trends"

# url = "http://mymarquez.host:5000"
# api_key = "1234567890ckcu028rzu5l"
url = "http://localhost:5000"
# client = OpenLineageClient(
#     url=url,
#     # optional api key in case marquez requires it. When running marquez in
#     # your local environment, you usually do not need this.
#     options=OpenLineageClientOptions(api_key=api_key),
# )
client = OpenLineageClient(url=url)

import attr
from typing import List
from openlineage.client.facet import BaseFacet

@attr.s
class JobDetailsFacet(BaseFacet):
    s3Location: str = attr.ib()
    jobRunId: str = attr.ib()
    accountId: str = attr.ib()
    accountName: str =attr.ib()
    accountRegion: str =attr.ib()
    executionId: str = attr.ib()

    _additional_skip_redact: List[str] = ['s3Location', 'jobRunId', 'accountId',
                                          'accountName', 'accountRegion',
                                          'executionId']

    def __init__(self, s3Location, jobRunId, accountId, accountName, accountRegion, executionId):
        self.s3Location = s3Location
        self.jobRunId = jobRunId
        self.accountId = accountId
        self.accountName = accountName
        self.accountRegion = accountRegion
        self.executionId = executionId



# generates job facet
def job(job_name, sql, spark, location):
    if sql:
        facets = {"sql": SqlJobFacet(sql)}

    if spark:
        facets = {"jobType": JobTypeJobFacet(
                                processingType="BATCH",
                                integration="SPARK",
                                jobType="TASK")}

    if location != None:
        facets.update(
            {"sourceCodeLocation": SourceCodeLocationJobFacet("git", location)}
        )
    return Job(namespace=namespace, name=job_name, facets=facets)


# geneartes run racet
def run(run_id, start_time, parent_facet, s3_location, job_run_id, account_id, account_name, account_region, execution_Id):
    default_facet= {
            "nominalTime": NominalTimeRunFacet(
                nominalStartTime=start_time
            ),
            "my_facet": JobDetailsFacet(s3Location=s3_location, jobRunId=job_run_id,
                                        accountId=account_id, accountName=account_name,
                                        accountRegion=account_region, executionId=execution_Id)
        }
    if parent_facet:
        default_facet['parent'] = parent_facet
    return Run(
        runId=run_id,
        facets=default_facet,
    )


# generates dataset
def dataset(name, schema=None, ns=namespace):
    if schema == None:
        facets = {}
    else:
        facets = {"schema": schema}
    return Dataset(namespace, name, facets)


# generates output dataset
def outputDataset(dataset, stats):
    output_facets = {"stats": stats, "outputStatistics": stats}
    return OutputDataset(dataset.namespace, dataset.name, dataset.facets, output_facets)


# generates input dataset
def inputDataset(dataset, dq):
    input_facets = {
        "dataQuality": dq,
    }
    return InputDataset(dataset.namespace, dataset.name, dataset.facets, input_facets)


now = datetime.now(timezone.utc)


# generates run Event
def runEvents(job_name, sql, inputs, outputs, hour, min, location, duration):
    run_id = str(generate_new_uuid())
    myjob = job(job_name, sql, location)
    myrun = run(run_id, hour)
    started_at = now + timedelta(hours=hour, minutes=min, seconds=20 + round(random() * 10))
    ended_at = started_at + timedelta(minutes=duration, seconds=20 + round(random() * 10))
    return (
        RunEvent(
            eventType=RunState.START,
            eventTime=started_at.isoformat(),
            run=myrun,
            job=myjob,
            producer=PRODUCER,
            inputs=inputs,
            outputs=outputs,
        ),
        RunEvent(
            eventType=RunState.COMPLETE,
            eventTime=ended_at.isoformat(),
            run=myrun,
            job=myjob,
            producer=PRODUCER,
            inputs=inputs,
            outputs=outputs,
        ),
    )


# add run event to the events list
def addRunEvents(
    events, job_name, sql, inputs, outputs, hour, minutes, location=None, duration=2
):
    (start, complete) = runEvents(
        job_name, sql, inputs, outputs, hour, minutes, location, duration
    )
    events.append(start)
    events.append(complete)




def addRunEvents(job_name, sql, spark, inputs, outputs, start_time, end_time, location, parent_facet=None):
    run_id = str(generate_new_uuid())
    myjob = job(job_name, sql, spark, location)
    myrun = run(run_id, start_time, parent_facet)
    # started_at = now + timedelta(hours=hour, minutes=min, seconds=20 + round(random() * 10))
    # ended_at = started_at + timedelta(minutes=duration, seconds=20 + round(random() * 10))

    return (
        RunEvent(
            eventType=RunState.START,
            eventTime=start_time,
            run=myrun,
            job=myjob,
            producer=PRODUCER,
            inputs=inputs,
            outputs=outputs,
        ),
        RunEvent(
            eventType=RunState.COMPLETE,
            eventTime=end_time,
            run=myrun,
            job=myjob,
            producer=PRODUCER,
            inputs=inputs,
            outputs=outputs,
        ),
    )


def create_schema_fields(schema):

    schema_fields = [SchemaField(name=field["column_name"], type=field["column_type"]) for field in schema]
    schema_facet = SchemaDatasetFacet(fields=schema_fields)
    return schema_facet


def create_dataset(namespace, dataset_name, schema_facet, s3_location=None, dq_facet=None):

    facet = {"schema": schema_facet}

    if s3_location:
        facet["my_facet"]= MyFacet(s3location=s3_location)

    if dq_facet:
        facet["dataQualityAssertions"]= dq_facet

    dataset = Dataset(
                namespace=namespace,
                name=dataset_name,
                facets=facet
            )
    return dataset


def create_run_event(job_name, sql, spark, source_dataset, target_dataset, start_time, end_time,
                     src_location, s3_location=None, parent_facet=None,job_run_id=None,
                     account_id=None, account_name=None, account_region=None, execution_Id=None):
    start_run_event = None
    end_run_event = None
    run_id = str(generate_new_uuid())
    myjob = job(job_name, sql, spark, src_location)
    myrun = run(run_id, start_time, parent_facet, s3_location, job_run_id, account_id, account_name, account_region, execution_Id)


    if start_time:
        start_run_event = RunEvent(
            eventType=RunState.START,
            eventTime=start_time,
            run=myrun,
            job=myjob,
            producer=PRODUCER,
            inputs=source_dataset,
            outputs=target_dataset,
        )

    if end_time:
        end_run_event = RunEvent(
            eventType=RunState.COMPLETE,
            eventTime=end_time,
            run=myrun,
            job=myjob,
            producer=PRODUCER,
            inputs=source_dataset,
            outputs=target_dataset,
        )


    return start_run_event, end_run_event

def create_dq_facet(dq_results):
    assertions =[]
    for each in dq_results:
        assertions.append(Assertion(assertion=each.get('dq_constraint_rule'),
                                    success=True if each.get('dq_constraint_rule_status').lower() == 'success' else False,
                                    column=each.get('dq_constraint_name')))
    if assertions:
        return DataQualityAssertionsDatasetFacet(assertions=assertions)
    return assertions


if __name__ == "__main__":
    session = boto3.Session(profile_name='aws_sso')
    sqs_client = session.client('sqs', region_name='eu-west-1')

    # SQS queue URL
    queue_url = 'https://sqs.eu-west-1.amazonaws.com/035328922125/sqs-lineage-target-queue'

    # Initialize the OpenLineage client

    def receive_messages():
        response = sqs_client.receive_message(
            QueueUrl=queue_url,
            AttributeNames=['All'],
            MaxNumberOfMessages=10,
            MessageAttributeNames=['All'],
            VisibilityTimeout=30,
            WaitTimeSeconds=20
        )
        return response.get('Messages')



    job_types = ['default_info', 'job_metrics', 'data_quality_metrics']

    log_stats_data = []
    dq_event = []

    for data in receive_messages():
        print(data['Body'])
        log_stats_data.append(json.loads(data['Body']))

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



        from openlineage.client.serde import Serde
        print(Serde.to_json(start_event))
        print(Serde.to_json(end_event))
        # time.sleep(1)
        client = OpenLineageClient(url=url)
        client.emit(start_event)
        client.emit(end_event)
        for each_event in dq_event:
            client.emit(each_event)




