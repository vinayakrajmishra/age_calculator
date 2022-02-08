# importing required modules
from datetime import datetime as dt
import sys

# today's date
date = dt.date(dt.now())
date = str(date)
present_year = int(date[:4])
present_month = int(date[5:7])
present_date = int(date[8:])

months_30 = [4,6,9,11]
months_31 = [1,3,5,7,8,10,12]

#asking for dob input
print("Hello Dear, I'm here to calculate your age")
dob = input("Tell me your date of birth in ddmmyyyy format: ")

if len(dob)==8:
    pass
else:
    print("Sorry You did not entered a correct ddmmyyyy format")
    sys.exit()

try :
    int(dob)   
except:
    print("Sorry You did not entered a correct ddmmyyyy format")
    sys.exit()
 # slicing dob in year month and date
date_dob = int(dob[:2])
month_dob = int(dob[2:4])
year_dob = int(dob[4:])

#parsing present_date according to months
if present_date < date_dob:
    if present_month in months_31:
        present_date+=31
        present_month-=1
    elif present_month in months_30:
        present_month+=30
        present_month-=1
    else :
        if present_year%4 == 0:
            present_date+=28
            present_month-=1
        else:
            present_date+=29
            present_month-=1
else:
    pass

# parsing present_month 
if present_month< month_dob:
    present_month+=12
    present_year-=1
else:
    pass

# function to calculate age of user
def age_calcualtor():
    age_date = present_date - date_dob
    age_year = present_year- year_dob
    age_month = present_month - month_dob
    
    
    print(f"You are {age_year} years {age_month} months and {age_date} days old")

age_calcualtor()