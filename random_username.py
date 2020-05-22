import random
import os, argparse
import time, datetime
import sys, getopt

# Without an argument, this script will create 42 new entries. The entries are called students but it is irrelavant.  They are really users for the purposes of this script.
numberofstudents = 42

# To guarantee unique ID's we are using time.  But if this script is running in different locations simultaneously or the number of users is > 100 then ther is the posibility of overlaping id numbers.

from datetime import datetime
now=datetime.now() 
centisecond=now.microsecond*100
studentfile = int(time.time()*100+centisecond)
studentbase = studentfile*100
print ("The first record ID number is: ")
print (studentbase)

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('random_username.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('random_username.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('Input file is "', inputfile)
   print ('Output file is "', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])



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

    username = firstname + '_' + middlename + '_' + lastname  
    user_record = str(studentbase) + ',' + lastname + ',' + firstname + ',' + major + ',' + str(gpa_sem) + ',' + str(absenses) + ',' + str(gpa_cum) + ',' + str(gpa_diff) + ',' + account_paid
  

    print (user_record)
    studentbase = studentbase + 1
    #sys.stdout=open()