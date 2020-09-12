from py_imessage import imessage

phone = "6262029474"

if not imessage.check_compatibility(phone):
    print("Not an iPhone")

imessage.send(phone, "hey hey i'm hungry")