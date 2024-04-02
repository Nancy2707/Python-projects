# creating an email validation python program
email=input("Enter your Email: ") //taking email as input
# defining values to required values used if neccesary special characters are not present
k=0
j=0
d=0
# minimum length of the email will be 6 as 1"@",1 ".", co or com or in 
if len(email)>=6:
# checking 1st letter must be alphabet
    if email[0].isalpha():
# checking there must be @ and only one 
        if ("@" in email) and (email.count("@")==1):
# the " ." must be present from 4th or 3rd place from the last
            if (email[-4]==".") ^ (email[-3]=="."):
# checking that there must be no space 
                for i in email:
                    if i== i.isspace():
                        k=1
# checking no capital alphabet should be there
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
# If it contains digit then the loop should be continue                            
                    elif i.isdigit():
                        continue
# only special character "_",".","@"
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
   
                if k==1 or j==1 or d==1:
                    print("Invalid Email 5")
            else:
                print("Invalid email 4")
        else:
            print("Invalid email 3")
    else:
        print("Invalid email 2")
    print("Valid Email")
else:
    print("Invalid email 1")
#using Regex for Email validation
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter the email")
if re.search(email_condition,user_email):
    print("right email")
else:
    print("wrong email")
    
