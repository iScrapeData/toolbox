import pandas as pd
import concurrent.futures
import threading

# Prevent data race step 1, Initialization
row = 0

# Prevent data race step 2, Construct Lock
mutex = threading.Lock()

# Pretend Function
def Scraper(row):

    print(f"{row}: makes Jack a dull boy.",end="\n")

if __name__ == "__main__":

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:

        # Dataframe for filtering against this df
        file_ = "file_1.csv"

        df_filter = pd.read_csv(file_)

        # Dataframe for iterating over to enter scraper
        file_2 = "file_2.csv"

        df_master = pd.read_csv(file_2)
        
        mutex.acquire()

        # Set to 1 for quick testing
        # Set to range(len(df_master)) for testing production
        for row in range(len(df_master)):

            # Check row of one df against col of another
            if df_master.cusip[row] in df_filter.cusip.values:

                print(f"{row}: All work and no play",end="\n")
                pass

            else:

                # Enter the Creator
                pool.submit(Scraper, row)
            
        mutex.release()