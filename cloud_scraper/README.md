# DESCRIPTION
This program is much like my get_html scraper. Except, everything is in the cloud. If you have large source files that are too much for your local computer, or you have big data, this is the only way to go. I'm scraping over 7M pages right now. 

# RECOMMENDED SERVICES
This script costs you money. Namely, I use a proxy service called scraperapi.com and Google Cloud Platform.

# SUGGESTED WORKFLOW
Create virtual environment in the root folder of project with terminal command (windows):

python3 -m venv <name of environment>

Activate the venv: Navigate to the root folder containing your venv and open it in terminal. Use command: env\Scripts\activate

Install dependencies such as requests, pandas, numpy, etc.

Test that the script works in the env with command: python your-main-script.py. I suggest setting your max_workers = 1 and your main for loop for entering your main function (Scraper) between 1 and 5 (see your-main-script.py).

Create requirements.txt file with command: pip freeze > requirements.txt. However, the one I provide here works for the program.

## Go to your GCP console.
Create VM instance. Suggested directions: https://towardsdatascience.com/how-to-start-a-data-science-project-using-google-cloud-platform-6618b7c6edd2

When you SSH into your VM, verify your environment.

Run the following bash shell commands:

Verify Python version:
python3 --version

Get updated:
sudo apt-get update

Install pip3 and Python Venv:
sudo apt install python3-venv python3-pip

Verify pip3 version:
pip3 --version

Create a venv on the VM:
python3 -m venv <name of environment>

Verify it was created:
ls

Upload all necessary files (at least all files in the cloud_scraper folder):
Verify the uploads:
ls

Activate your venv:
source <name of environment>/bin/activate

Install dependencies:
pip3 install -r requirements.txt


Run your-main-script.py and debug (still in venv): 
Set workers to 1 and the worker for loop to 5.
We're just testing here.
python3 your-main-script.py

Tip: When the scraper is finished and all of your work is done, download any files written to VM disk that you need, save VM instance image to the project's folder (if needed), and delete VM. You are being charged for all of this as long as it exists.

# RELEVANT GOOGLE CLOUD PLATFORM HELP

## Here are some helpful GCP links if you want to see how my scraper and it's helper functions run under the hood.

I can't even tell you how important understanding cloud billing is. Be sure that you understand that everything your script does with a GCP resource will result in some charge, unless it's explicitly a free tier service. 

https://cloud.google.com/blog/products/gcp/best-practices-for-optimizing-your-cloud-costs

Filenames in GCP include the path to the file, which is not a path at all. And, there is only one "folder". That's the bucket. The structure of the bucket is pseudo. So, if you want a folder name "my_folder" in your bucket, don't attach it to the bucket name as if the folder actually exits - like on a normal OS. Instead, you append the "folder" path to the file name because, that's just what it is to a GCP bucket - part of the file name. Read this: https://cloud.google.com/storage/docs/naming-objects

Building your VM:
https://towardsdatascience.com/how-to-start-a-data-science-project-using-google-cloud-platform-6618b7c6edd2

Creating a service account key for local authentication:
If you're running on your VM, you won't need the keys that I call with the Client() in the helper files, but I included them anyway to make it easier for you when if you use the files on a non-authenticated GCP platform, or your local computer. 

You'll store this JSON file (your-gcp-service-key.json) key in your project's main folder (where I have the placeholder) to authenticate to your GCP resources. Be sure to give it the permission it needs when you created (usually read/write permission for logging and storage buckets). With that said, for best practice, use the <em>least privileged</em> concept - only the permission needed for the project. I give my scrapers permission to read/write logs and to read/write bucket data. But not delete permissions. That give me a built in method to avoid duplicate entries.

https://console.cloud.google.com/apis/credentials/serviceaccountkey

Viewing object metadata (e.g. name):
https://cloud.google.com/storage/docs/viewing-editing-metadata#code-samples

If you're not a native linux user like myself, you'll need a cheat sheet for bash:

https://oit.ua.edu/wp-content/uploads/2016/10/Linux_bash_cheat_sheet.pdf

Reading CGP blobs (files):
https://www.kaggle.com/c/talkingdata-adtracking-fraud-detection/discussion/56014

# GLOBAL VARS
Any mutex that's defined outside of your function, be sure to define it as a global variable within the function. Otherwise, your workers may completely forget what a mutex is once inside your function, which will cause a hang.

# ULIMIT
Increase your ulimit to something respectable if you're on a linux or Debian VM like I use. Otherwise, you may get a "too many files open" error. Also, you have to do this every time you connect to your VM instance (no restart, but connect).

Commands
ulimit -a
ulimit -n 128447
ulimit -u 128447
*This number will vary depending on your instance resources. I usually just match the -n to the -u, which should already be set high by default.

Source: https://support.imply.io/hc/en-us/articles/360013273774-If-you-re-having-a-too-many-open-files-problem-I-feel-bad-for-you-son-but-I-got-99-problems-and-a-ulimit-setting-ain-t-one-

# Processing the Task
Your VM processes stop once you disconnect from your SSH session. That's including your scraper. So, the fix is to append the nohup and "&" commands when you start your script. It's simple:

nohup python3 your-main-scrip.py 2>&1 &

The appendages send the process to the background, enabling you to continue to use the terminal for other commands. And it ignores the hangup e.g. you disconnecting from the SSH session.

If you want to know more about this, read this article: https://support.ehelp.edu.au/support/solutions/articles/6000089713-tips-for-running-jobs-on-your-vm

If you need to work with your processes e.g. view and/or kill, see this article: https://phoenixnap.com/kb/how-to-kill-a-process-in-linux

# TROUBLESHOOTING
This section is most useful if you somehow inappropriately alter the code for GCP uploading, logging, or mutex placement. As these methods may not throw an error, but will cause your workers to skip all code that follows if used improperly. Also, if you use this program on a local computer and network with insufficient resources. And finally, this section is useful because the program just isn't perfect.

Example:
Correct
up_to_gc("get-data-scrapers", f"{filing_type}_{filename[row]}", f"historical_subs/subs/Other/{filing_type}_{filename[row]}")

Incorrect
up_to_gc("get-data-scrapers", f"{filing_type}_{filename[row]}", f"historical_subs/subs/Other/{filing_type}_{filename[row]}",)

That extra comma may not throw an error Python, though it is an error because GCP hates trailing commas. And it will kill your worker as described above.

Also, improper use of the Mutex will not throw an error. Your workers will just do funny things like, stopping a the code just above where the error exists.

Otherwise, you should not need the troubleshooting scripts below. I've F'd up enough for you.

## Upload Missing
If for some reason the code leaves behind file, or you just want to verify files' existence, use the upload_missing.py (standalone) file to do work on the directory. 

This script searches for filenames in the GCP cloud directory and from there, you can just count, verify, or write some logic that uploads the missing files. To upload, just import up_to_gcs.py to upload_missing.py and call the function.

Here's my workflow:

Let's say I have to stop my script for some reason and a bunch of files are left behind; but I have no idea if they have been uploaded to gcp or not.

Check for files left behind with the terminal ls command.

Copy the files to your clipboard and create a Python list of them. I use this hand tool to create my list: https://txtformat.com/. It allows you to append your quotation marks and commas all at once.

In your VM terminal, start a Python shell: 

python3

Make your imports:

import os
from up_to_gcs import up_to_gc
from upload_missing import blob_metadata, search

Create your list in Python shell script: 

lst = [paste from site txtformat]

Cut-n-paste this command - checks GCP Bucket and returns files that are NOT in GCP bucket:

for i in lst:

    try:
        blob_metadata("bucket-name", f"psuedo/path/to/{i}")
    except:
        print(i)

If no files are returned, you can skip this step and go to File Removal below. Cut and past the list of files returned into txtformat and create lst2 the same way you did with the first list.

Add list 2 to Python shell script: 

lst2 = [paste from site txtformat]

Cut-n-paste this command - uploads missing files to gcp:

for i in lst2:

    up_to_gc("bucket-name",f"/home/your_root_directory/{i}",f"psuedo/path/to/{i}")

File Removal
Cut-n-paste this command - removes all files left behind by interrupting your main script:

for i in lst:

    os.remove(f"{i}")

exit() - exit Python shell

## Compare Files
In combination with the upload_missing.py, I added a script (comparison.py) to test two files are identical. You can import this into upload_missing.py to add it to your logic, or just use it as a stand alone tool.

Source: https://www.geeksforgeeks.org/python-filecmp-cmp-method/


# DISCLAIMER
This code is not perfect. Also, it was developed in a VS Code and Windows environment. Additional debugging may be required on another OS.