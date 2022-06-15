
import os
from datetime import datetime
import glob
import shutil
import pyperclip

print("""
       d8888                        88888888888                       888      
      d88888                            888                           888      
     d88P888                            888                           888      
    d88P 888 88888b.  88888b.           888  888d888 8888b.   .d8888b 888  888 
   d88P  888 888 "88b 888 "88b          888  888P"      "88b d88P"    888 .88P 
  d88P   888 888  888 888  888          888  888    .d888888 888      888888K  
 d8888888888 888 d88P 888 d88P          888  888    888  888 Y88b.    888 "88b 
d88P     888 88888P"  88888P"           888  888    "Y888888  "Y8888P 888  888 
             888      888                                                      
             888      888                                                      
             888      888                                                      
""")
print("   by Wesley Smith\n\nhttps://github.com/matterofhack/apptrack\nhttps://matterofhack.com\n")
print("____________________________________________________________________")
print("____________________________________________________________________\n\n")

task_count = 0
def make_count(z):
    print(" ", z, "/ 11")

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
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("######" * task_count)
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n\n")

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
fancy_output()

finished_with_pics = input("FINISHED WITH SCREENSHOTS ? ")
task_count += 1
make_count(task_count)
ok_text()


def folder_check(x):
        if os.path.isdir(x) != True:
            os.mkdir(x)


now = datetime.now()
today = now.strftime("%m-%d-%Y")


folder_name = today + "-applications"
folder_check(folder_name)


current_directory = os.getcwd()


nested_folder_path = current_directory + "/" + folder_name + "/" + company_name + " - " + job_title
folder_check(nested_folder_path)


destination_directory = nested_folder_path + "/"
job_pics = glob.glob(current_directory + "/*.png")


for file in job_pics:
    job_pics_file_name = os.path.basename(file)
    shutil.move(file, destination_directory + job_pics_file_name)


file_name = company_name + " - " + job_title + ".txt"
file_handling = open(nested_folder_path + "/" + file_name, "w")
file_handling.write(company_name + "\n" + job_title + "\n" + job_location + "\n" + salary_estimate + "\n" + listing_origin + "\n" + listing_id + "\n" + application_origin + "\n" + application_creds + "\n" + job_match + "\n" + point_of_contact + "\n" + today)
file_handling.close()



print("\n\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("####################################################################")
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("""
 .d8888b.                                                      
d88P  Y88b                                                     
Y88b.                                                          
 "Y888b.   888  888  .d8888b .d8888b .d88b.  .d8888b  .d8888b  
    "Y88b. 888  888 d88P"   d88P"   d8P  Y8b 88K      88K      
      "888 888  888 888     888     88888888 "Y8888b. "Y8888b. 
Y88b  d88P Y88b 888 Y88b.   Y88b.   Y8b.          X88      X88 
 "Y8888P"   "Y88888  "Y8888P "Y8888P "Y8888   88888P'  88888P'                                                          
""")
