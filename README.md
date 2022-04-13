# apptrack

USAGE

First and foremost, use this at your own risk. I take no responsibility in the use, or misuse of this script.

This script depends on Python 3.x.x and "Pyperclip" module

https://www.python.org/downloads/

https://github.com/asweigart/pyperclip

Create a job hunt folder
ex. "jobhuntfolder"

place "apptrack.py" script into the newly created folder

Open terminal / command prompt

cd desktop/jobhuntfolder

python3 apptrack.py

Proceed to fill out info from prompts via typing followed by enter

NOTE:

If a prompt field is left "blank"; pressing enter will paste the last item from your clipboard. This is by design in order to speed up the workflow.

"LIKELY JOB MATCH ? " prompt will default to "job-match-low" value IF left "blank", otherwise any character(s) will result in "job-match-high". Yet again, this is by design for efficiency.

Time to follow up on jobs you're most interest in?

Open terminal / command prompt

cd desktop/jobhuntfolder

grep -rwi --color "job-match-high" your/various/directories/with/apptrack/text/files/here

now you've located text files with info to support your follow up(s)


CAVEATS

-I’m self-taught. I likely repeated code, and nothing was commented due to the project size. My programming background(mostly Lua) is with games I developed on-off over the past decade or more. With that said, there’s plenty of room for improvement and definitely areas to add functionality.

-Directories and files are created and potientally overwritten WITHOUT warning. Be mindful of script placement and usage.


If two job entries have the same company name(or recruitment agency), job title and each are saved on the same day; then the most recent entry will overwrite the older entry. This is due to a lack of file name checking.

folder name format: MM-DD-YYYY-applications
ex. “04-13-2022-applications”

file name format: Company A - Job Title A.txt
ex “Fortune 500 - Manager of Management.txt”


-Everything is saved in clear text, and this may or may not be an issue depending on your situation.

-Precision is key to effective usage. There is no undo.
