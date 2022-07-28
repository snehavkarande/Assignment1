#!/usr/bin/env python
# coding: utf-8

# In[16]:


import re
import pandas as pd
import csv
Q=int(input("DO you want to register or Login? (0 for register and 1 for login)"))
if Q==0:
    email_add=input("enter your email address")
    regex='^[a-zA-z]+[a-zA-Z0-9]+[@]\w+[a-z0-9]+[.]\w{2,3}$'

    is_valid=re.search(regex,email_add)
    if is_valid:
        password=input("enter your password")
        regex1="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pattern=re.compile(regex1)
        match=re.search(pattern,password)
        if match:
            col1 = "email_add"
            col2 = "password"
            data = pd.DataFrame({col1:[email_add],col2:[password]})
            data.to_csv('login.csv',mode='a', index=False,header =False)
        
        else:
            print("Password is invalid")
        
    else:
        print("invalid email address")
        
elif Q==1:
    email_add=input("enter your email address")
    password=input("enter your password")
    with open('login.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
                if row[0]== email_add and row[1] == password:
                    login = True
                  
                else:
                    login = False       
        if login==True:
            print("You have been logged in")
        elif login==False:
            print("Incorrect credentials..")
            print("Do you want to reterive password or change your password?")
            Q= int(input("For reteriving press 0 , for changing password press 1"))
            if Q==0:
                email_add=input("enter your email address")
                df = pd.read_csv("login.csv")
                filter_data = df[df["Emailid"].str.contains(email_add,case=False)]
                if not filter_data.empty:
                      print(filter_data["Password"])   
            elif Q==1:
                email_add=input("enter your email address")
                df = pd.read_csv("login.csv")
                filter_data = df[df["Emailid"].str.contains(email_add,case=False)]
                if not filter_data.empty:
                    password=input("Enter new password ")
                    regex1="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
                    pattern=re.compile(regex1)
                    match=re.search(pattern,password)
                    if match:
                        df.loc[df["Emailid"].str.contains(email_add,case=False),"Password"]=password
                        df.to_csv('login.csv',index=False,header=True)
                    else:
                        print("Please provide valid password")
                else:
                    print("no user found. register first")


# In[ ]:





# In[ ]:





# In[ ]:




