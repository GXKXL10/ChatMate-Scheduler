import pywhatkit

#reciever
ph = input("enter phone number - ")

#time
hh = int(input("enter hour in 24h format - "))
mm = int(input("enter minute - "))

#textmessage
txt = input("Enter Message - ")

pywhatkit.sendwhatmsg(ph, txt, hh, mm)