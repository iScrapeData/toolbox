# Parallel Programming
import concurrent.futures
import threading

# File & Datetime
import csv
from time import time
import pendulum
import os

# Dataframe
import pandas as pd
import numpy as np

# Initialize date for error handling only
dt_start = pendulum.now()

# Log start of program
with open(
    f"Logs/start_run_{pendulum.now().format('M_DD_YYYY')}.csv",
    "a",
    newline="",
) as f:

    write = csv.writer(f)

    write.writerow(
        [pendulum.now().format('YYYY-MM-DD'), pendulum.now().format('HH:mm:ss'), os.path.realpath(__file__),]
    )


# Initialize time and number of requests
start_time = time()

# Prevent data race step 1, Initialization
row = 0

# Prevent data race step 2, Construct Lock
mutex = threading.Lock()

# URLs Creator function
def Creator(row):

    # Initialize Globals
    global var_1
    global var_2
    global var_3
    global var_4
    global var_5
    global var_x

    # Load empty array to store iteration data
    data_row = []

    # Create url
    url = f"https://www.example.com/{var_1[row]}/{var_3[row]}/{var_4[row]}/{var_x[row]}/"

    # Create filename
    filename = f'path/to/{var_1[row]}_{var_4[row]}_{var_x[row]}.txt'

    data_row.append(
        (
            row,
            url,
            filename,
            var_1[row],
            var_x[row],
        )
    )

    # convert output to new array
    array = np.asarray(data_row)

    # convert new array to dataframe
    df_urls = pd.DataFrame(array)

    # Append df to urls.csv
    mutex.acquire()
    df_urls.to_csv(f"urls.csv", mode="a", header=False, index=False)
    mutex.release()

if __name__ == "__main__":

    # max_workers can be whatever your system can handle
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as pool:

        # Source of master variables to build urls
        # A sample row: var_1, var_2, var_3, var_4, var_x
        master = "source.csv"

        df_master = pd.read_csv(master)

        # Global Variables for Scraper Function
        var_1 = df_master.var_1
        var_2 = df_master.var_2
        var_3 = df_master.var_3
        var_4 = df_master.var_4
        var_5 = df_master.var_5
        var_x = df_master.var_x

        # Prevent data race step 3, wait before iterating
        mutex.acquire()

        # Set to 1 for testing
        # Set to range(len(df_master)) for production
        for row in range(1):

            # Construct logic for not entering the Creator
            # Prevent duplicates?
            if True:
                
                # You could set up a Log here
                pass

            else:

                # Enter the Creator
                pool.submit(Creator, row)

            row += 1

        mutex.release()

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
