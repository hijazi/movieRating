#! /usr/bin/python2.7

import random
import json
import urllib2
#import ast

def processTitle( title ):
    title = title.replace(" ", "+")
    return title

def getRating( processedTitle ):
    url = "http://www.omdbapi.com/?t="+processedTitle+"&y=&plot=short&r=json"
    data = urllib2.urlopen(url)    
    html = data.read()
    dictData = json.loads(html)
    imbdRating = dictData['imdbRating']

    return imbdRating

textFile = open("./yMList.txt", "r")
lines = textFile.read().split("\n")
mList = []
count = 0
for line in lines:
    if line != '':
        count += 1
        mList.append(line)

print "number of movies is {}".format(count)

Glist = []
i = 0
while i < len(mList):
    title = mList[i]
    pTitle = processTitle(title)
    rating = getRating(pTitle)
    rating = float(rating)
    print "{}. {} rating is {}".format(i+1, title, rating)
    Glist.append([title,rating])
    i += 1

i = 0
j = k = 0
temp = [0,0]

# sort the list
while k < (len(Glist)-1):
    # iterations
    j = k+1
    while j < (len(Glist)):
        if Glist[k][1] < Glist[j][1]:
            temp[0] = Glist[k][0]
            temp[1] = Glist[k][1]
            Glist[k][0] = Glist[j][0]
            Glist[k][1] = Glist[j][1]
            Glist[j][0] = temp[0]
            Glist[j][1] = temp[1]
        j += 1
    k += 1

count = 1        
for i in Glist:
    print "{}.\t{}\t{}".format(count, i[1], i[0])
    count += 1
print "Done"
