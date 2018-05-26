import random
import os

thing1 = random.choice(open('filename.txt').read().split()).strip()
thing2 = random.choice(open('filename.txt').read().split()).strip()
thing3 = random.choice(open('filename.txt').read().split()).strip()

username = thing1 + '_' + thing2 + '_' +thing3

print username
