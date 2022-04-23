## UPDATE 4-23-22
### [known-bugs]

If the company name or job title contains " / " the script will think you're referencing a file path; thereby, resulting in an error and potential loss of progress with the entry you're working through.

## Workaround: Don't use " / " in company name or job title until it's resolved

## UPDATE 4-17-22
### [added functionality]

Now you can point your screen capture application to output **.png** files to the main directory containing *apptrack.py*

Doing so will automatically move the screen capture(s) into a newly created and relevant folder based on the script prompts



## USAGE

> First and foremost, use this at your own risk. I take no responsibility in the use, or misuse of this script.

This script depends on **Python 3.x.x** *and* **"Pyperclip" module**

https://www.python.org/downloads/

https://github.com/asweigart/pyperclip
```
Create a job hunt folder
ex. "jobhuntfolder"
```
```
place "apptrack.py" script into the newly created folder
```
```
Open terminal / command prompt
```
```
cd desktop/jobhuntfolder
```
```
python3 apptrack.py
```

*Proceed to fill out info from prompts via typing followed by pressing enter. "SUCCESS" will display and the resulting directory and text file will be automatically created.*

## NOTE:

If a prompt field is left **empty**; pressing *enter* will paste the last item from your clipboard. This is by design, in order to speed up the workflow.

**"LIKELY JOB MATCH ? "** prompt will default to **"job-match-low"** value **IF** left *empty*, otherwise any character(s) will result in **"job-match-high"**. Yet again, this is by design for efficiency.

*Time to follow up on job(s) you're most interested in?*
```
Open terminal / command prompt
```
```
cd desktop/jobhuntfolder
```
```
grep -rwi --color "job-match-high" your/various/directories/with/apptrack/text/files/here
```
*Now you've located the text file(s) with info to support your follow up(s).*


## CAVEATS

* I’m self-taught. I've likely wrote repeated and inefficient code, and nothing was commented due to the project size. My programming background(mostly Lua) is with games I developed on-off over the past decade or more. With that said, there’s plenty of room for improvement and definitely areas to add functionality.

* Directories and files are created and potientally overwritten **WITHOUT** warning. *Be mindful of script placement and usage.*


If two job entries have the same company name(or recruitment agency), job title **and** each are saved on the same day; then the most recent entry will **overwrite** the older entry. This is due to the lack of file name checking.
```
folder name format auto-generated: MM-DD-YYYY-applications

ex. “04-13-2022-applications”
```
```

file name format auto-generated: Company A - Job Title A.txt

ex. “Fortune 500 - Manager of Management.txt”
```

* Everything is saved in clear text, and this may or may not be an issue depending on *your* situation.

* Precision is key to effective usage. There is no undo, only **CTRL+C**.
