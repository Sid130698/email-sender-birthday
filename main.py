import smtplib
import datetime


#...........establishing connection............
my_email= <yOUR_EMAIL>
connection= smtplib.SMTP("smtp.gmail.com")

#.......encrypting using tls to prevent data being leaked if intercepted...........

connection.starttls()
connection.login(user=my_email,password=<yOUR_PASSWORD>)

#...........sending mail..............
try:
    connection.sendmail(from_addr=my_email,
    to_addrs=<rECV_EMAIL>,
    msg="subject: Testing mail\n\nsending mail via bot")
except:
    print("Error sending mail")
else:
    print("mail sent successfully")
finally:
    connection.close()


datetime.datetime

