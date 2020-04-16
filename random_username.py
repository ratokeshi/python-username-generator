import random
import os

firstname = random.choice(open('firstnames.txt').read().split()).strip()
middlename = random.choice(open('firstnames.txt').read().split()).strip()
lastname = random.choice(open('lastnames.txt').read().split()).strip()

username = firstname + '_' + middlename + '_' + lastname

print (username)
