#OVERVIEW

This is a python command line application mean for local machines that will read an Excel file with a list of national provider identifiers (NPIs) and go to the CMS/Medicare validation site to grab information from the site.  This is critical for organizations that need to track those revalidation dates in order to stay compliant with CMS rules.

#SETUP

Ensure you have Google Chrome or Chromium downloaded on your computer.  Next, create a virtual environment and then utilize the requirements file to download all necessary packages.  

After this is complete, create a new Excel file called "Medicare_Revalidation_Results.xlsx" and put it into the "results" folder.  This file should the following columns (in order), which replicates the data in the site:

- NPI (Required: Numeric)
- Name
- Due Date
- Adjusted Due Date
- State
- Specialty
- Reassigned Providers
- Enrollment Type
- Last Checked

Fill out all of the NPIs you want to look up under the "NPI" column.  Leave the rest of the data blank as it will be pulled from the CMS site.

#RUNNING

The medicare_revalidation.py script is all that needs to be run.  In that file, you can change several options at the top like if you want selenium to run headless (in the background), only pull NPIs with adjusted dates (not recommended), and if you want to enter a debug mode where you can provide a manual list of NPIs in an array vs. reading the whole Excel file NPI list.  Additionally, the script should work on both Windows and Mac computers and will automatically detect which one it's on based on the system function results from the platform module.

When running the script, it will go through the list of NPIs in the Excel file mentioned in the setup instructions above.  As the script is running, it will print out results as it's received and then save them all back to the Excel document once done.