import phonenumbers

from phonenumbers import geocoder
print('''
                   =================================
                   |The developer:[MOUNIR ALBDULLH]|
                   |   MY snapchat:(ar5824)        |
                   =================================
''')

tt = input("put the phone number: ")

pone = phonenumbers.parse(tt)

vv = phonenumbers.is_valid_number(pone)
if vv == True:
    print("The number is used")
else:
    print("The number is not used")

pp = phonenumbers.is_possible_number(pone)
if pp == True:
    print("the number correct" "")
else:
    print("the number is not correct" "")
ttt = geocoder.description_for_number(pone, 'en')
print(ttt)
rhh = geocoder.parse(tt)
print(rhh)
bb = phonenumbers.PhoneMetadata(tt)
print(bb)


