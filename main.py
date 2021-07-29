import smtplib
import datetime


#...........establishing connection............
my_email= "thepythonbot1306@gmail.com"
connection= smtplib.SMTP("smtp.gmail.com")

#.......encrypting using tls to prevent data being leaked if intercepted...........

connection.starttls()
connection.login(user=my_email,password="sid130698")

#...........sending mail..............
try:
    connection.sendmail(from_addr=my_email,
    to_addrs="sidsingh130698@gmail.com",
    msg="subject: Testing mail\n\nsending mail via bot")
except:
    print("Error sending mail")
else:
    print("mail sent successfully")
finally:
    connection.close()


datetime.datetime

