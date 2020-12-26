# DESCRIPTION
This program scrapes html pages and uploads them to a Google Cloud Storage Bucket. It is intended for 1000+ scrapes due to its cost and robust features. Scrape almost any site on the web. Even if it uses JavaScript to load content.

# MAIN FILE
get_html.py

This script incurs costs when run. Namely a subscription to Scraperapi.com, and Google Cloud Storage costs.

Scrape fast with concurrent scraping.

Scrape anonymously with a proxy and Residential IP 
Recommended: www.scraperapi.com

It's easiest to separate the task of building urls to scrape from the scraping process itself, when you have hundreds of thousands (or even millions) of urls to scrape. So in the global variables, I created a "url" variable that is iterated over from a dataframe. But that's another script not included in this program.

# CUSTOM IMPORTS
up_to_gcs.py - uploads files to Google Cloud Storage Bucket

# DISCLAIMER
This code is not perfect. Also, it was developed in a VS Code and Windows environment. Additional debugging may be required on another OS.