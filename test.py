import os
import re
import csv

def extract_info_from_tf_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()


    name_matches = re.findall(r'name\s+=\s+"([^"]+)"', content)
    severity_matches = re.findall(r'severity\s+=\s+"([^"]+)"', content)
    sustain_matches = re.findall(r'sustain\s+=\s+"([^"]+)"', content)
    op_matches = re.findall(r'op\s+=\s+"([^"]+)"', content)
    value_matches = re.findall(r'value\s+=\s+(\d+)', content)

    extracted_data = []

    for i in range(len(name_matches)):
        extracted_data.append({
            'name': name_matches[i],
            'severity': severity_matches[i],
            'sustain': sustain_matches[i],
            'op': op_matches[i],
            'value': int(value_matches[i]),
        })

    return extracted_data

tf_dir = '.'

data = []

for filename in os.listdir(tf_dir):
    if filename.endswith('.tf'):
        file_path = os.path.join(tf_dir, filename)
        extracted_data = extract_info_from_tf_file(file_path)
        if extracted_data:
            data.extend(extracted_data) 

csv_file = 'terraform_data.csv'

with open(csv_file, 'w', newline='') as csvfile:
    fieldnames = ['name', 'severity', 'sustain', 'op', 'value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f'Data extracted and saved to {csv_file}')
