# Dataframe
import pandas as pd

# Input files
file_1 = "file_1.csv"
file_2 = "file_2.csv"

# Create Dataframes
df_1 = pd.read_csv(file_1)
df_2 = pd.read_csv(file_2)

# Create checks
check_1 = df_1.astype("string")
check_2 = df_2.astype("string")

# Manually check for values
if "F21107951" in check_1.cusip.values:
    print("yes")
else:
    print("no")

# Check using a list

lst = ["F21107951"]

if lst[0] in check_1.cusip.values:
    print("yes")
else:
    print("no")

# Check df against a list
try:
    check = lst.index(check_1.issuer[0])

    # Do work
    print("yes")

except:

    print("no")

# Check using a dictionary
dd = {
  "key_1": "F21107951",
}

if dd["key_1"] in check_1.cusip.values:
    print("yes")
else:
    print("no")

# Check df value against dictionary
if check_1.issuer[0] in dd.values():
    print("yes")
else:
    print("no")

# Check row of one df against col of another
if check_1.issuer[0] in df_2.issuer.values:
    print("yes")
else:
    print("no")