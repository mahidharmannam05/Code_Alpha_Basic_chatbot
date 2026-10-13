def Wish(data):
    if data=='HELLO':
        print("hi!")
    elif data=='HOW ARE YOU':
        print("I'm fine, thanks!")
    elif data=='BYE':
        print("Goodbye!")
        return "bye"
    else:
        print("sorry, i'm  unable to understand")
while True:
    cmd=input().upper()
    if Wish(cmd)=="bye":
        break