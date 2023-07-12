'''
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
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
        time = words[5]
        index = time.split(':')
        hour = index[0]
        dict[hour] = dict.get(hour, 0) + 1

lst = []        
for hour, count in dict.items():
    new = (hour, count)
    lst.append(new)
lst = sorted(lst, reverse=False)

for hour, count in lst:
    print(hour, count)