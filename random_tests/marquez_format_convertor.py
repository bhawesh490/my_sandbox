import json
import os

# Function to read a JSON file
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to write to a JSON file
def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Directory containing JSON files
json_dir = 'log_stats_logs'

# List to store file paths
json_files = [os.path.join(json_dir, file) for file in os.listdir(json_dir) if file.endswith('.json')]

# Process each JSON file
for file_path in json_files:
    data = read_json(file_path)
    # src_data_set_name = None
    # dest_data_set_name = None

    if any(each in data['job_name'] for each in ['-ingest-', '-extract-']) and data.get('job_metrics', None):
        data_set_name = data.get("job_step", None).split(': ')[-1]

        # if 'extract' in data['job_name']:
        #     src_data_set_name = 'src.' + data_set_name
        #     dest_data_set_name = data_set_name + '.extract'
        # elif 'ingest' in data['job_name'] and data.get('job_metrics', {"landing_table": None}).get("landing_table"):
        #     print("inside ingest")
        #     src_data_set_name = data_set_name + '.extract'
        #     print(src_data_set_name)
        #     dest_data_set_name = data.get('job_metrics').get('landing_table').split('/')[-1]
        #     print(dest_data_set_name)
        # else:
        #     pass

        if src_data_set_name and dest_data_set_name:
            data["source_datset_name"]=src_data_set_name
            data["target_dataset_name"]=dest_data_set_name

        if 'ingest' in data['job_name']:
            data['layer'] = True
        else:
            data['layer'] = False

        if data.get('job_metrics').get('schema', None):
            data['job_metrics']['src_schema'] = data.get('job_metrics').get('schema', None)




    # Save the modified data back to the file
    write_json(data, file_path)

print("All JSON files have been modified and saved.")
