# Description
This program builds a "urls.csv" file to use as a dataframe to iterate over in a web scraper. This takes the workload off of the scraper itself and reduces debugging issues. 

# Testing
Obviously, as a scientist you already know to check random samples of the urls created by this program to ensure they work as intended.

# Planning
It's best practice to preplan your csv header row with variables. This helps write the script.

In this example, we'll keep it generic. As a bonus - and for the same reason - we'll also create the output filename that the scraper will use to output the scraped html text.

Note: The variables are the parts of the url and filename. They come from another dataframe (via csv) that is not included in this program. 

# Prototype
Place a prototype of the output here, for all the essential variables. It's useful for referencing and comparing to the output file - urls.csv:

url: 
Past examples of all unique urls that you intend your scraper will see.
Creation - f"https://www.example.com/{var_1}/{var_3}/{var_4}/{var_x}/"
Output - https://www.example.com/var_1/var_3/var_4/var_x/

Bonus: We'll also use this program to prefabricate output filenames for the scraper as well. I separate concerns this way so that my Scraper only has to do one thing - my motto - "Get the data."

Note: Never include your API key in the url variable, or anywhere that it would be recorded/logged into other documents. Always place keys and other credentials directly into code. You don't want your credentials showing up in logs or output/input files. You could also store credentials in an external file. But that's only necessary in a web application or in software.