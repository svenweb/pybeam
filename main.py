import json
from collections import Counter


with open('lbeam.json', 'r') as data:
    d = json.load(data)


thirdParty = {}
#print(d)
def getThirdParties():
    for site in d:
        if(d[site].get('thirdParties')):
           for hostname in d[site].get('thirdParties'): yield hostname


for site in getThirdParties():
    if site in thirdParty: thirdParty[site] += 1
    else: thirdParty[site] = 1

k = Counter(thirdParty)

high = k.most_common(10)

print('Top 10 most common third parties')

for i in high:
    print(i[0],' :', i[1]," ")

