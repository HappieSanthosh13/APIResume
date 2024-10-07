import azure.functions as func
from azure.cosmos import CosmosClient
import os
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    resume_id = req.params.get('id')

    url = os.environ['COSMOS_DB_URL']
    key = os.environ['COSMOS_DB_KEY']
    client = CosmosClient(url, credential=key)
    database = client.get_database_client('yamlk ')
    container = database.get_container_client('SampleContainer')

    # Query the item
    query = f"SELECT * FROM Resumes r WHERE r.id = '{id}'"
    items = list(container.query_items(query, enable_cross_partition_query=True))

    if items:
        return func.HttpResponse(json.dumps(items[0]), mimetype="application/json")
    else:
        return func.HttpResponse("Resume not found", status_code=404)
