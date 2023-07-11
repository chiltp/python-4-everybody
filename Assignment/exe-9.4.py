'''
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dict = {}

for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        if not email in dict:
            dict[email] = 1
        else:
            dict[email] = dict[email] + 1
        #dict[name] = dict.get(name, 0) + 1

max_count = None
max_email = None

for email,count in dict.items():
    if max_count is None or count > max_count:
        max_count = count
        max_email = email
print(max_email, max_count)