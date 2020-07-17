import json

url =  "jsons_file/file_js.json"

with open(url) as file_js:
    templates = json.load(file_js)