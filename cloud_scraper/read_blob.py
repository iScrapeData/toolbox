# This script allows the program to read a source file
# stored in a GCP bucket. To load into a df, for example.
from google.cloud import storage
from io import BytesIO

def read(bucket_name, source_file_name):

    storage_client = storage.Client.from_service_account_json(
            'your-gcp-service-key.json')
            
    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(source_file_name)

    content = blob.download_as_string()

    bytes_file = BytesIO(content)

    return bytes_file