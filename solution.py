import csv
import json
from collections import defaultdict

def read_encode_csv(file_path):
    encode_dict = {}
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            long_url = row['long_url']  # long_url is an identifier
            short_url = f"http://{row['domain']}/{row['hash']}"  # Store the row data in the dictionary
            encode_dict[short_url] = long_url
    return encode_dict

def read_decode_json(json_file_path):
    with open(json_file_path, 'r') as json_file:
        decode_data = [json.loads(line) for line in json_file]
    return decode_data

def filter_and_count_2021_clicks(decode_data, encode_dict):
    clicks_count = defaultdict(int)
    for click in decode_data:
        bitlink = click['bitlink']
        timestamp = click['timestamp']
        if bitlink in encode_dict and timestamp.startswith('2021'):
            long_url = encode_dict[bitlink]
            clicks_count[long_url] += 1
    return dict(sorted(clicks_count.items(), key=lambda x: x[1], reverse=True))

# Step 1: Read encodes.csv and create encode dictionary
encodes_file_path = 'encodes.csv'
encode_dict = read_encode_csv(encodes_file_path)

# Step 2: Read decodes.json 
decodes_file_path = 'decodes.json'
decode_dict = read_decode_json(decodes_file_path)

# Step 3 : Use decode and encodes data to count clicks from 2021 for each long URL 
results = filter_and_count_2021_clicks(decode_dict, encode_dict)
print("Clicks from 2021 for each record (sorted by count in descending order):")
print(results)

