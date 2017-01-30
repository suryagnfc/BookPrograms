def isPhoneNumber (text):
    if len(text) != 12:
        return False
    else:
        for i in range(0,3):
            if not text[i].isdecimal():
                return False
            else:
                if text[3] != "-":
                    return False
                else:
                    for i in range(4,7):
                        if not text[i].isdecimal():
                            return False
                        else:
                            if text[7] != "-":
                                return False
                            else:
                                for i in range(8,12):
                                    if not text[i].isdecimal():
                                        return False
            return True


print ('Enter your text and we will get phone numbers from the text for you:')
text = input ()
count =0
for i in range(len(text)):
    if isPhoneNumber(text[i:i+12]):
        print('Found a Phone Number: ' + text[i:i+12])
        count = count +1

if count ==0:
    print('No phone Number found.')
                                 
