# this program assumes that the text has atleast one phone number.
# this program is not intelligent enough to handle the 0 phone number in a text
import re

def isPhonenumber(text):
    phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumberRegex.search(text)
    print(type(mo.group()))
    if len(mo.group()) >0:
        print ('trying to get the length' + str(len(mo.group())))
        return mo.group()


print('Enter the text and we will find phone number from it:')

message = input()

print(isPhonenumber(message))
