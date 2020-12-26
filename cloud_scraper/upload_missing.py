# This script is to search for files in GCP storage
# and upload it if they are not there

from google.cloud import storage
from up_to_gcs import up_to_gc

import os

def blob_metadata(bucket_name, blob_name):
    """Prints out a blob's metadata."""
    # bucket_name = 'your-bucket-name'
    # blob_name = 'your-object-name'

    storage_client = storage.Client.from_service_account_json(
        'your-gcp-service-key.json')

    bucket = storage_client.bucket(bucket_name)
    
    blob = bucket.get_blob(blob_name)

    return blob.name

def search(directory):

    missing = 0

    for filename in os.listdir(directory):

        try: 

            up_to_gc("bucket-name", f"{directory}{filename}", f"pseudo/path/to/{filename}")

            print(f"{filename} uploaded")

            missing += 1

        except:

            pass

    print(f"{missing} files uploaded")

# Use for direct search
# comment out or delete if exporting to script
search("path/to/folder/")