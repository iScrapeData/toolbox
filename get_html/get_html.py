"""
See README file for more information on this program.
"""

# Make requests
import requests

# Parallel Programming
import concurrent.futures
import threading

# Working with Files
import pandas as pd
import csv
from time import time
import pendulum
import os

# Upload files to Google cloud Platform
from up_to_gcs import up_to_gc

# Initialize datetime (for logging only)
dt_start = pendulum.now()

# Log start of program
with open(
    f'Logs/start_run_{pendulum.now().format("YYYY-MM-DD")}.csv',
    "a",
    newline="",
) as f:

    write = csv.writer(f)

    write.writerow(
        [
            pendulum.now().format("YYYY-MM-DD"),
            pendulum.now().format("HH:mm:ss"),
            os.path.realpath(__file__),
        ]
    )

# Prevent data race step 1, Initialization
row = 0

# Prevent data race step 2, Construct Lock
mutex = threading.Lock()

# Scraper function
def Scraper(row):

    # Initialize Globals
    global url
    global var

    # Scraper API Key URL String
    api_url = f"http://api.scraperapi.com?api_key=<your_key>&url={url[row]}"
      
    # Logging relevant variables prior to use
    try:
        mutex.acquire()
        with open(
            f"Logs/relevant_variables.csv",
            "a",
            newline="",
        ) as f:

            write = csv.writer(f)

            write.writerow(
                [
                    pendulum.now().format("YYYY-MM-DD"),
                    pendulum.now().format("HH:mm:ss"),
                    row,
                    your_vars,
                    url[row],
                    os.path.realpath(__file__),
                ]
            )
        mutex.release()
    except Exception as e:
        
        with open(f"Logs/filings.csv", "a", newline="") as f:

                write = csv.writer(f)

                write.writerow(
                    [
                        pendulum.now().format("YYYY-MM-DD"),
                        pendulum.now().format("HH:mm:ss"),
                        row,
                        your_vars,
                        url[row],
                        e,
                        os.path.realpath(__file__),
                    ]
                )

    try:

        # Per scraperapi docs -  set timeout to 60
        with requests.request("GET", api_url, timeout=60) as req:

            status_code = req.status_code

            text = req.text

        if status_code >= 200 and status_code < 300:

            # Get the Data
            with open("o.csv", "w") as f:

                f.write(text)
            
            # Upload
            up_to_gc("your_key.json","your-bucket-name","o.csv","o.csv")

            # Delete
            os.remove("o.csv")

            mutex.acquire()
            with open(f"Logs/filings.csv", "a", newline="") as f:

                write = csv.writer(f)

                write.writerow(
                    [
                        pendulum.now().format("YYYY-MM-DD"),
                        pendulum.now().format("HH:mm:ss"),
                        row,
                        your_vars,
                        url[row],
                        os.path.realpath(__file__),
                    ]
                )
            mutex.release()

        else:

            with open(
                f'Logs/error_{pendulum.now().format("YYYY-MM-DD")}.csv',
                "a",
                newline="",
            ) as f:

                write = csv.writer(f)

                write.writerow(
                    [
                        pendulum.now().format("YYYY-MM-DD"),
                        pendulum.now().format("HH:mm:ss"),
                        status_code,
                        row,
                        your_vars,
                        url[row],
                        os.path.realpath(__file__),
                    ]
                )

    except Exception as e:

        with open(
            f'Logs/error_{pendulum.now().format("YYYY-MM-DD")}.csv',
            "a",
            newline="",
        ) as f:

            write = csv.writer(f)

            write.writerow(
                [
                    pendulum.now().format("YYYY-MM-DD"),
                    pendulum.now().format("HH:mm:ss"),
                    row,
                    you_vars,
                    url[row],
                    os.path.realpath(__file__),
                    e,
                ]
            )


if __name__ == "__main__":

    # Test max_workers with max allowed concurrent workers
    # in your scraperapi dashboard.
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as pool:

      source = "urls.csv"

      df_source = pd.read_csv(source)

      # Global Variables for Scraper Function
      url = df_source.url
      # I often prefabricate output filenames as well
      var = df_source.var

      # Prevent data race step 3 - wait before iterating
      mutex.acquire()

      # Set to 1 for testing
      # Set to range(len(df_source)) for production
      for row in range(1): 

          # Some condition to decide to scrape the url or not
          # Handy if you expect to stop/restart the scraper
          # without duplicating API calls or iterations.
          if True:

              # You could set up a Log here
              pass

          else:

              # Enter the scraper
              pool.submit(Scraper, row)

          row += 1

      mutex.release()

# Log end of program
with open(
    f"Logs/end_run_{pendulum.now().format('M_DD_YYYY')}.csv",
    "a",
    newline="",
) as f:

        ct = pendulum.now().to_datetime_string()

        dt_end = pendulum.now()

        # dt2 in relation to dt1
        diff = dt_start.diff(dt_end)

        write = csv.writer(f)

        write.writerow(
            [
                ct,
                os.path.realpath(__file__),
                f"{diff.in_days()} days elapsed",
                f"{diff.in_hours()} hours elapsed",
                f"{diff.in_minutes()} minutes elapsed",
                f"{diff.in_seconds()} seconds elapsed",
            ]
        )