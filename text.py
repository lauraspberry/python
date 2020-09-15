from py_imessage import imessage

phone = "CENSORED (usually just put in 10 digit string of nums)"

if not imessage.check_compatibility(phone):
    print("Not an iPhone")

imessage.send(phone, "hey hey i'm hungry")
