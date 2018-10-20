import smtplib
import getpass
b=input("From:")
c=input("To:")
d=input("Subject:")
e=input("Body:")
f=getpass.getpass()
a=smtplib.SMTP('smtp.gmail.com',587)
a.ehlo()
a.starttls()
a.login(b,f)
a.sendmail(b,c,"Subject:"+d+"\n"+e)
a.quit()
print("mail sent")
