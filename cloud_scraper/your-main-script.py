# Make requests
import requests

# Parallel Programming
import concurrent.futures

# Prevent data race step 1
import threading

# Work with dataframes, csv, and other files
import pandas as pd
import csv
import os

# Save files and log with Google Cloud
from up_to_gcs import up_to_gc
from logger import *
from read_blob import read
from upload_missing import blob_metadata

play("your-main-script.py", "script-started")

# Prevent data race step 2, Initialization
row = 0

# Prevent data race step 3, Construct Lock
# Create lock(s)
mutex = threading.Lock()

# Scraper/Main function
def Scraper(row):

    # globals
    global var_1
    global var_2
    global var_3
    global var_4
    global mutex
    # Add inter-function mutexes as well
    mutex2 = threading.Lock()
    mutex3 = threading.Lock()

    api_url = f"http://api.scraperapi.com?api_key=your_key&url={url[row]}"

    # Logging the relevant variables before using them
    variables(
        "your-main-script.py",
        "relevant-variables",
        var_1[row],
        var_2[row],
        var_3[row],
        var_4[row],
        filename[row],
        url[row],
    )

    try:

        # Per scraperapi docs the timeout should be set to 60
        # for automatic retries on errors
        with requests.request("GET", api_url, timeout=60) as req:

            status_code = req.status_code

            text = req.text

        if status_code >= 200 and status_code < 300:

            # You can make this anything, 
            # i.e. a function or whatever.
            # It's just a check for some quality in the page 
            # being scraped to let us know if we want to keep it 
            # or not.
            abort = False

            #  If abort is true log it and get out of the loop
            if abort is True:

                aborted(
                    "your-main-script.py",
                    "aborted",
                    var_1[row],
                    var_2[row],
                    var_3[row],
                    var_4[row],
                    filename[row],
                    url[row],
                    "html-not-desired",
                )

            else:

                # Your filename should have been prefabricated.
                # I have such a tool in this repository:
                # "build_urls"
                # NOTE: Be careful here, the way I have it set 
                # up to create the filename, is that the file 
                # extension is already included. Don't reappend 
                # here.
                with open(f"/home/your_root_directory/{filename[row]}", "w") as f:

                    # Write
                    f.write(text)

                # Upload
                # Upload
                # Upload
                try: 

                    mutex2.acquire()
                    up_to_gc(
                        "bucket-name",
                        f"/home/your_root_directory/{filename[row]}",
                        f"psuedo/path/to/{filename[row]}"
                    )
                    mutex2.release()

                except Exception as e:
                                      
                    UploadError(
                        "your-main-script.py",
                        "Upload Error",
                        var_1[row],
                        var_2[row],
                        var_3[row],
                        var_4[row],
                        filename[row],
                        url[row],
                        e,
                    )

                # Log this iteration as done and delete the 
                # local file
                mutex.acquire()
                if os.path.exists(f"/home/your_root_directory/{filename[row]}"):

                    os.remove(f"/home/your_root_directory/{filename[row]}")
                    
                else:
                  
                    pass
                mutex.release()

            mutex3.acquire()
            with open("/home/your_root_directory/done.csv", "a", newline="") as a:

                write = csv.writer(a)

                write.writerow(
                    [
                        var_1[row],
                    ]
                )
            mutex3.release()

        else:

            response(
                "your-main-script.py",
                "url-response",
                var_1[row],
                var_2[row],
                var_3[row],
                var_4[row],
                filename[row],
                url[row],
                f"status-code-{status_code}",
            )

    except Exception as e:

        primaryFailed(
            "your-main-script.py",
            "main-block-exception",
            var_1[row],
            var_2[row],
            var_3[row],
            var_4[row],
            filename[row],
            url[row],
            e,
        )


if __name__ == "__main__":

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as pool:

        # Prevent data race step 4, Wait before iterating
        mutex.acquire()
        
        done_file = f"/home/your_root_directory/done.csv"

        done = pd.read_csv(done_file, dtype=str)

        # Read your urls and other data from table or df file
        content = read("bucket_name", "source_file_name") 

        df_source = pd.read_csv(content, dtype=str)

        done.drop_duplicates()

        df_source.drop_duplicates()

        var_1 = df_source.var_1
        var_2 = df_source.var_2
        var_3 = df_source.var_3
        var_4 = df_source.var_4
        filename = df_source.filename
        url = df_source.url

        # Range set to 5 for local testing
        for row in range(5):  # len(df_source)

            pass_1 = var_1[row] in done.col.values

            if pass_1 is False:

                # Enter the scraper
                pool.submit(Scraper, row)

            else:

                pass

            row += 1

        mutex.release()

finish("your-main-script.py", "script-finished")