import random
import os
import time
import sys
numberofstudents = 55


studentfile = int(time.time())
studentbase = studentfile*100


print (studentbase)

for x in range (1, numberofstudents):
    studentbase = studentbase + 1
    firstname = (random.choice(open('firstnames.txt', 'r').read().split()).strip()).capitalize()
    middlename = (random.choice(open('firstnames.txt').read().split()).strip()).capitalize()
    lastname = (random.choice(open('lastnames.txt').read().split()).strip()).capitalize()
    major = random.choice(open('major.txt').read().split()).strip()
    gpa_sem = random.choice(open('gpa.txt').read().split()).strip()
    gpa_sem = round(float(gpa_sem)*.1,2)
    gpa_cum = random.choice(open('gpa.txt').read().split()).strip()
    gpa_cum = round(float(gpa_cum)*.1,2)
    absenses = random.choice(open('absences.txt').read().split()).strip()
    gpa_diff = int(gpa_cum)-int(gpa_sem)
    gpa_diff = round(gpa_diff*.1,2)∏
    account_paid = random.choice(open('account_paid.txt').read().split()).strip()

    username = firstname + '_' + middlename + '_' + lastname  
    user_record = str(studentbase) + ',' + lastname + ',' + firstname + ',' + major + ',' + str(gpa_sem) + ',' + str(absenses) + ',' + str(gpa_cum) + ',' + str(gpa_diff) + ',' + account_paid
  

    print (user_record)
    
    #sys.stdout=open()