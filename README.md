#OVERVIEW

This is a python command line application meant for local machines that will read an Excel file with a list of national provider identifiers (NPIs) and use selenium (automation package) go to the CMS/Medicare validation site to grab information from the site.  This is critical for organizations that need to track those revalidation dates in order to stay compliant with CMS rules and reduce the effort to do this monthly task.

#SETUP

Ensure you have Google Chrome or Chromium downloaded on your computer.  Next, create a virtual environment and then install all packages listed in the requirements file.  

After this is complete, create a new Excel file called "Medicare_Revalidation_Results.xlsx" and put it into the "results" folder.  This file should contain the following columns (in order), which replicates the data in the site:

- NPI (Required)
- Name
- Due Date
- Adjusted Due Date
- State
- Specialty
- Reassigned Providers
- Enrollment Type
- Last Checked

Next, add all of the NPIs you want to look up under the "NPI" column.  Leave the rest of the columns blank as that information will be pulled from the CMS site.

#RUNNING

The medicare_revalidation.py script is all that needs to be run to pull the information from the CMS site.  In that file, you can change several options at the top like if you want selenium to run headless (in the background), only pull NPIs with adjusted dates (not recommended), and if you want to enter a debug mode where you can provide a manual list of NPIs in an array vs. reading the whole Excel file NPI list.  Additionally, the script should work on both Windows and Mac computers and will automatically detect which one it's running in based on the system function results from the platform module.

When running the script, it will go through the list of NPIs in the Excel file mentioned in the setup instructions above.  As the script is running, it will print out results (or you can view them in real time if you leave headless as false) and then save them all back to the Excel document once done.

The script is also built on two customer helper classes.  The first is a custom implementation of the webdriver class to make the commands easier to call in the main script.  For example, to get the NPI's organization name and avoid errors, you need to first ensure the element is loaded on the page, then go to grab the text, and handle when sometimes the element contains text itself or the html property has the text.  This would be several blocks of code, just to do this simple task and would need to be repeated multiple times.  To simplify this, a custom "get_element_text" function was created to handle that.

The second is to handle when the Webdriver version is out of sync with Chrome or Chromium.  This error typically happens right when launching the Webdriver class and if it happens, the custom script will identify what root version of Chrome you're running locally (whether you're using Mac or Windows) and then go to download and install the latest Webdriver under bin/chome_driver location in the project folder.
