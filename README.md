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
