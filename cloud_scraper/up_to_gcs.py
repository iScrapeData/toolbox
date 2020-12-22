# This script allows you to upload your scraped pages to GCP
from google.cloud import storage

def up_to_gc(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client.from_service_account_json(
        'your-gcp-service-key.json')
        
    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)