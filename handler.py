import json

def main(event, context):
    request = event['Records'][0]['cf']['request']
    if request["uri"] != "/hello.json":
        request["uri"] = "/not_found.json"
    return request