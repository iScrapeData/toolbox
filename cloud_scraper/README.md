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

Verify pip3 verison:
pip3 --version

Create a venv on the VM:
python3 -m venv <name of environment>

Verify it was created:
ls

Upload all necessary files:
Verify the uploads:
ls

Activate your venv:
source <name of environment>/bin/activate

Install dependencies:
pip3 install -r requirements.txt


Run and debug (still in venv): 
python3 your-main-script.py

Tip: When finished - download any files written to vm disk, save instance image to the project's folder - set automatic delete if needed, release firewall ip, and delete vm. You are being charged for all of this as long as it exists.

# GOOGLE CLOUD PLATFORM HELP

## Here are some helpful GCP links if you want to see how my scraper and it's helper functions run under the hood.

I can't even tell you how important understanding cloud billing is. Be sure that you understand that everything your script does with a GCP resource causes some charge, unless it's explicitly a free tier service. 

https://cloud.google.com/blog/products/gcp/best-practices-for-optimizing-your-cloud-costs

Building your VM:
https://towardsdatascience.com/how-to-start-a-data-science-project-using-google-cloud-platform-6618b7c6edd2

Creating a service account key for local authentication:
You'll store this JSON file key in your projects to authenticate to your GCP resources. Be sure to give it the permission it needs. But for best practice, use <em>least privileged</em> concept - only the permission needed by the project. I gave my scraper permission to read/write logs and to read/write bucket data.
https://console.cloud.google.com/apis/credentials/serviceaccountkey

Viewing object metatdat (e.g. name):
https://cloud.google.com/storage/docs/viewing-editing-metadata#code-samples

If you're not a native linux user like myself, you'll need a cheat sheet for bash:

https://oit.ua.edu/wp-content/uploads/2016/10/Linux_bash_cheat_sheet.pdf

Reading CGP blobs (files):
https://www.kaggle.com/c/talkingdata-adtracking-fraud-detection/discussion/56014

# GLOBAL VARS
Any mutex that's defined outside of your function, be sure to define it as a global variable within the function. Otherwise, your workers may completely forget what a mutex is once inside your function, which will cause a hang.

# ULIMIT
Increase your ulimit to something respectable if you're on a linux or Debian VM like I use. Otherwise, you may get a "too many files open" error.

Commands
ulimit -n 128444
ulimit -u 128444

Source: https://support.imply.io/hc/en-us/articles/360013273774-If-you-re-having-a-too-many-open-files-problem-I-feel-bad-for-you-son-but-I-got-99-problems-and-a-ulimit-setting-ain-t-one-