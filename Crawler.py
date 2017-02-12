# WebCrawler
import urllib.request
import re

def extractData(data, pattern):
    extracted = pattern.findall(data)
    noRepeatData = set(extracted)
    extracted = list(noRepeatData)
    return extracted

initialiser = 'http://www.ram.org/ramblings/philosophy/spam/spammers.html'

initialLink = urllib.request.urlopen(initialiser)

#Patterns
linkPattern = re.compile(r'http[s]*\://[www\.]?\w+\.\w+[\.\w+]*[/\w[\.\w]*]*')
emailPattern = re.compile(r'\w+@\w+\.\w+[\.\w]*')

crudeData = str(initialLink.read())

linkList = extractData(crudeData, linkPattern)
emailList = extractData(crudeData, emailPattern)

for email in emailList:
    emailFile = open('Emails.txt', 'a')
    emailFile.write(email + '\n')
    emailFile.close()

for link in linkList:

    try:
        crudeLink = urllib.request.urlopen(link)
        crudeData = str(crudeLink.read())
        
        tempEmails = extractData(crudeData, emailPattern)
        tempLinks = extractData(crudeData, linkPattern)

        for email in tempEmails:
            if email not in emailList:
                emailFile = open('Emails.txt', 'a')
                emailFile.write(email + '\n')
                emailFile.close()

        for tempLink in tempLinks:
            if tempLink not in linkList:
                linkFile = open('Crawled.txt', 'a')
                linkFile.write(tempLink + '\n')
                linkFile.close()
                linkList.append(tempLink)
    except:
        pass
