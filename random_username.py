import random
import os, argparse
import time, datetime
import sys, getopt

#Test for arguments
parser = argparse.ArgumentParser()
parser.add_argument("--users", default=3, type=int,
                    help="Choose your own number of records to create. The default is 42.")
parser.add_argument("--app", default='original', choices=['wordpress', 'drupal', 'moodle', 'all', 'custom', 'original'], 
                    help="Current options are original and wordpress.  Coming soon: drupal, moodle, all, and custom.  The default is original.")                    
parser.add_argument("--domain", default='r4t.net', 
                    help="The default domain is r4t.net.  Use this option to send all users to your own custom domain.")
args = parser.parse_args()




# Without an argument, this script will create 42 new entries. The entries are called students but it is irrelavant.  They are really users for the purposes of this script.
numberofstudents = args.users

# To guarantee unique ID's we are using time.  But if this script is running in different locations simultaneously or the number of users is > 100 then ther is the posibility of overlaping id numbers.

from datetime import datetime
now=datetime.now() 
centisecond=now.microsecond*100
studentfile = int(time.time()*100+centisecond)
studentbase = studentfile*100
print ("The first record ID number is: ")
print (studentbase)






for x in range (0, numberofstudents):
    
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
    gpa_diff = round(gpa_diff*.1,2)
    account_paid = random.choice(open('account_paid.txt').read().split()).strip()


    username = firstname + '.' + lastname + '.' +str(studentbase % 10000000)
    useremail = username + '@' + args.domain 
    user_registered = now.strftime("%m/%d/%Y %H:%M:%S")
    display_name = firstname + ' ' + lastname 

    if args.app=='original':
        user_record = str(studentbase) + ',' + lastname + ',' + firstname + ',' + major + ',' + str(gpa_sem) + ',' + str(absenses) + ',' + str(gpa_cum) + ',' + str(gpa_diff) + ',' + account_paid
    elif args.app=='wordpress':
        user_record = username + ',' + useremail + ',' + str(studentbase) + ',' + username + ',' + username + '.' + args.domain + ',' + user_registered + ',' + display_name + ',subscriber,' + username + ',' + firstname + ',' + lastname
    else:
        print("App value is not original.")    
    try:
        if user_record is None:
            print ("User Records is none.")    
    except NameError:
        print ("User Record is not defined.")
    else:
        print (user_record)
        studentbase = studentbase + 1
    #sys.stdout=open()