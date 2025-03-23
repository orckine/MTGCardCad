import json

def filter_json(input_file, output_file, allow_list):

    with open(input_file,'r',encoding='utf-8') as infile:
        data = json.load(infile)

    filtered_data=[]

    for item in data:
        filtered_item = {key: item[key] for key in allow_list if key in item}
        filtered_data.append(filtered_item)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(filtered_data,outfile,ensure_ascii=False,indent=4)

input_file = 'rawdata.json'
output_file = 'data.json'
allow_list = ['name','set', 'collector_number', 'foil', 'lang', 'number', 'printed_name', 'released_at']

filter_json(input_file,output_file,allow_list)
