import os

project_id = os.getenv('GCLOUD_PROJECT')

from google.cloud import datastore

datastore_client = datastore.Client(project_id)

def save_credentials(credentials):
    #key = datastore.Entity(key=datastore_client.key('username'),value=datastore_client.key('password'))
    key = datastore_client.key('movies')
    q_entity = datastore.Entity(key=key)
    for q_prop, q_val in credentials.items():
        q_entity[q_prop] = q_val

    datastore_client.put(q_entity)


