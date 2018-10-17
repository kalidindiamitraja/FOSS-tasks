import smtplib
import getpass
b=input("From:")
c=input("To:")
d=input("Message:")
e=getpass.getpass()
a=smtplib.SMTP('smtp.gmail.com',587)
a.ehlo()
a.starttls()
a.login(b,e)
a.sendmail(b,c,d)
a.quit()
print("mail sent")
