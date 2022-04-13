
import os
from datetime import datetime
import pyperclip

print("""
░█████╗░██████╗░██████╗░██╗░░░░░██╗░█████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░░░░░██║██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
███████║██████╔╝██████╔╝██║░░░░░██║██║░░╚═╝███████║░░░██║░░░██║██║░░██║██╔██╗██║
██╔══██║██╔═══╝░██╔═══╝░██║░░░░░██║██║░░██╗██╔══██║░░░██║░░░██║██║░░██║██║╚████║
██║░░██║██║░░░░░██║░░░░░███████╗██║╚█████╔╝██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░╚══════╝╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
""")
print("   by Wesley Smith\n\nhttps://github.com/wesseck/apptrack\nhttps://wesseck.com\n")
print("____________________________________________________________________")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

task_count = 0
def make_count(z):
    print(" ", z, "/ 10")

def ok_text():
    print("""
                                   11111
                                  1111
                                 111
                          1     111
                           11  11
                             111
                              1
                              
    """)

def line_break():
    print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n\n")

def fast_entry(a):
    if a == "fast-entry-pasted-here":
        a = pyperclip.paste()
        return a
    else:
        return a

def fancy_output():
    make_count(task_count)
    ok_text()
    line_break()

company_name = input("COMPANY NAME ? ") or "fast-entry-pasted-here"
company_name = str(fast_entry(company_name))
task_count += 1
fancy_output()

job_title = input("JOB TITLE ? ") or "fast-entry-pasted-here"
job_title = str(fast_entry(job_title))
task_count += 1
fancy_output()

job_location = input("LOCATION ? ") or "fast-entry-pasted-here"
job_location = str(fast_entry(job_location))
task_count += 1
fancy_output()

salary_estimate = input("SALARY ESTIMATE ? ") or "fast-entry-pasted-here"
salary_estimate = str(fast_entry(salary_estimate))
task_count += 1
fancy_output()

listing_origin = input("WEBSITE OF LISTING ? ") or "fast-entry-pasted-here"
listing_origin = str(fast_entry(listing_origin))
task_count += 1
fancy_output()

listing_id = input("ID OR NUMBER ASSOCIATED WITH LISTING ? ") or "fast-entry-pasted-here"
listing_id = str(fast_entry(listing_id))
task_count += 1
fancy_output()

application_origin = input("PORTAL FOR APPLICATION SUBMITTAL ? ") or "fast-entry-pasted-here"
application_origin = str(fast_entry(application_origin))
task_count += 1
fancy_output()

application_creds = input("PORTAL CREDENTIALS ? ") or "fast-entry-pasted-here"
application_creds = str(fast_entry(application_creds))
task_count += 1
fancy_output()

def job_match_preference(x):
    if x == "low":
        x = "job-match-low"
        return x
    else:
        x = "job-match-high"
        return x

job_match = input("LIKELY JOB MATCH ? ") or "low"
job_match = str(job_match_preference(job_match))
task_count += 1
fancy_output()

point_of_contact = input("POSSIBLE POINT OF CONTACT OR ADDITIONAL INFO ? ") or "fast-entry-pasted-here"
point_of_contact = str(fast_entry(point_of_contact))
task_count += 1
make_count(task_count)
ok_text()

now = datetime.now()
today = now.strftime("%m-%d-%Y")

folder_name = today + "-applications"
folder_check = os.path.isdir(folder_name)
if folder_check != True:
    os.mkdir(folder_name)

file_name = company_name + " - " + job_title + ".txt"
file_handling = open(folder_name + "/" + file_name, "w")
file_handling.write(company_name + "\n" + job_title + "\n" + job_location + "\n" + salary_estimate + "\n" + listing_origin + "\n" + listing_id + "\n" + application_origin + "\n" + application_creds + "\n" + job_match + "\n" + point_of_contact + "\n" + today)
file_handling.close()

print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("____________________________________________________________________")
print("""
░██████╗██╗░░░██╗░█████╗░░█████╗░███████╗░██████╗░██████╗░░░
██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝░░░
╚█████╗░██║░░░██║██║░░╚═╝██║░░╚═╝█████╗░░╚█████╗░╚█████╗░░░░
░╚═══██╗██║░░░██║██║░░██╗██║░░██╗██╔══╝░░░╚═══██╗░╚═══██╗░░░
██████╔╝╚██████╔╝╚█████╔╝╚█████╔╝███████╗██████╔╝██████╔╝██╗
╚═════╝░░╚═════╝░░╚════╝░░╚════╝░╚══════╝╚═════╝░╚═════╝░╚═╝
""")
