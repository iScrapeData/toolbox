# Imports the Google Cloud client library for logging
# This scripts allows you to log to your project's logs
from google.cloud import logging

# Log beginning of script
def play(script,log_name):

    # Instantiates and authenticate's a client
    logging_client = logging.Client.from_service_account_json(
        'your-gcp-service-key.json')

    # Selects the log to write to
    logger = logging_client.logger(log_name)

    # Struct log. The struct can be any JSON-serializable dictionary. These are whatever you want to log and can be used like any json or python dictionary.
    logger.log_struct(
        {
            "File" : script,
            "Message": "Script Started",
        }
    )

# Log the finish of a script
def finish(script,log_name):

    logging_client = logging.Client.from_service_account_json(
        'your-gcp-service-key.json')

    logger = logging_client.logger(log_name)

    logger.log_struct(
        {
            "File" : script,
            "Message": "Script Finished",
        }
    )

# Log relevant variables before they are used 
# (ex. to make a url request or create a file)
def variables(log_name, script, Var_1, Var_2, Var_3, Var_4, filename, url):

    logging_client = logging.Client.from_service_account_json(
        'your-gcp-service-key.json')

    logger = logging_client.logger(log_name)

    logger.log_struct(
        {
            "File" : script,
            "Var_1" : Var_1, 
            "Var_2" : Var_2,
            "Var_3" : Var_3,
            "Var_4" : Var_4,
            "Filename": filename,
            "URL" : url
        }
    )

# (Optional) Log your logic to dertimen that page does
# not contain the data that you neeed
def aborted(log_name, script, Var_1, Var_2, Var_3, Var_4, filename, url, message):

    # Instantiates a client
    logging_client = logging.Client.from_service_account_json(
        'your-gcp-service-key.json')

    # Selects the log to write to
    logger = logging_client.logger(log_name)

    # Struct log. The struct can be any JSON-serializable dictionary.
    logger.log_struct(
        {
            "File" : script,
            "Var_1" : Var_1, 
            "Var_2" : Var_2,
            "Var_3" : Var_3,
            "Var_4" : Var_4, 
            "Filename": filename,
            "URL" : url,
            "Message" : message,
        }
    )

# Log a bad url response
def response(log_name, script, Var_1, Var_2, Var_3, Var_4, filename, url, message):

    # Instantiates a client
    logging_client = logging.Client.from_service_account_json(
        'your-gcp-service-key.json')

    # Selects the log to write to
    logger = logging_client.logger(log_name)

    # Struct log. The struct can be any JSON-serializable dictionary.
    logger.log_struct(
        {
            "File" : script,
            "Var_1" : Var_1, 
            "Var_2" : Var_2,
            "Var_3" : Var_3,
            "Var_4" : Var_4, 
            "Filename": filename,
            "URL" : url,
            "Message" : message,
        }
    )

# Log the failure of the main try block
def primaryFailed(log_name, script, Var_1, Var_2, Var_3, Var_4, filename, url, message):

    # Instantiates a client
    logging_client = logging.Client.from_service_account_json(
        'your-gcp-service-key.json')

    # Selects the log to write to
    logger = logging_client.logger(log_name)

    # Struct log. The struct can be any JSON-serializable dictionary.
    logger.log_struct(
        {
            "File" : script,
            "Var_1" : Var_1, 
            "Var_2" : Var_2,
            "Var_3" : Var_3,
            "Var_4" : Var_4,
            "Filename": filename,
            "URL" : url,
            "Message" : message,
        }
    )