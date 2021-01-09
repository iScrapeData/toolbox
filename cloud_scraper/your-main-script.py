# Make requests
import requests

# Concurrent Programming
import concurrent.futures

# Prevent data race step 1
import threading

# Work with dataframes, csv, and other files
import pandas as pd
import csv
import os

# Save files and log with Google Cloud
from up_to_gcs import up_to_gc
from logger import play, finish

play("your-main-script.py", "script-started")

# Prevent data race step 2, Initialization
row = 0

# Prevent data race step 3, Construct Lock
# Create lock(s)
mutex = threading.Lock()
mutex2 = threading.Lock()
mutex3 = threading.Lock()

# Scraper/Main function
def Scraper(row):

    # globals
    global var_1
    global var_2
    global var_3
    global var_4

    api_url = f"http://api.scraperapi.com?api_key=your_key&url={url[row]}"

    # TODO: Log relevant variables before using them

    try:

        # Per scraperapi docs the timeout should be set to 60
        # for automatic retries on errors
        with requests.request("GET", api_url, timeout=60) as req:

            status_code = req.status_code

            text = req.text

            # TODO: Log each request
    except:

        # TODO: Handel request errors  
        pass

    if status_code >= 200 and status_code < 300:

        # You can make this anything, 
        # i.e. a function or whatever.
        # It's just a check for some quality in the page 
        # being scraped to let us know if we want to keep it 
        # or not.
        abort = False

        #  If abort is true log it and get out of the loop
        if abort is True:
            
            # TODO: Log abortions

            pass

        else:

            # Your filename should have been prefabricated.
            # I have such a tool in this repository:
            # "build_urls"
            # NOTE: Be careful here, the way I have it set 
            # up to create the filename, is that the file 
            # extension is already included. Don't reappend 
            # here.
            with open(f"/home/your_root_directory/scraped_files_folder/{filename[row]}", "w") as f:

                # Write
                f.write(text)

            # Upload
            try: 

                mutex2.acquire()
                up_to_gc(
                    "bucket-name",
                    f"/home/your_root_directory/scraped_files_folder/{filename[row]}",
                    f"psuedo/path/to/{filename[row]}"
                )
                mutex2.release()

            except:

                # TODO: Handel upload error

                pass

            # Delete local file
            mutex3.acquire()
            if os.path.exists(f"/home/your_root_directory/scraped_files_folder/{filename[row]}"):

                os.remove(f"/home/your_root_directory/scraped_files_folder/{filename[row]}")
                
            else:
              
                pass
            mutex3.release()

    else:

        # TODO: Log and handle negative status codes
        pass

if __name__ == "__main__":

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as pool:

        # Prevent data race step 4, Wait before iterating
        mutex.acquire()

        # Read your urls and other data from table or df file
        content = "/home/your_root_directory/source_file_name.csv" 

        df_source = pd.read_csv(content, dtype=str).drop_duplicates()
        
        var_1 = df_source.var_1
        var_2 = df_source.var_2
        var_3 = df_source.var_3
        var_4 = df_source.var_4
        filename = df_source.filename
        url = df_source.url

        # Range set to 5 for local testing
        for row in range(5):  # len(df_source)

            # Enter the scraper
            pool.submit(Scraper, row)

            row += 1

        mutex.release()

finish("your-main-script.py", "script-finished")