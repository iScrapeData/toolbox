from google.cloud import storage

def up_to_gc(service_key_loc,bucket_name, source_file_name, destination_blob_name):

    """
    Source - Create GCS Bucket:
    https://cloud.google.com/storage/docs/creating-buckets
    
    Source - Create Service Account Key: 
    https://cloud.google.com/iam/docs/creating-managing-service-account-keys#iam-service-account-keys-create-console

    Source - Pass Credentials Here: 
    https://cloud.google.com/docs/authentication/production#passing_code

    Uploads a file to the bucket.
    # service_key_loc = local/path/to/key
      key you created for this script.
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    """

    storage_client = storage.Client.from_service_account_json(service_key_loc)

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)