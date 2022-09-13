import csv, smtplib, re
from email.mime.text import MIMEText

main_mail = 'testd3vmaster@gmail.com'
password  = 'D3Vm@st3r'

fp  = open(r'C:\Users\Isac\Documents\Personal\mess\python\mass-email-sender\message.txt', 'rb')
msg = MIMEText(fp.read().decode())
fp.close()
msg['Subject'] = 'SUBJECT HERE'
msg['From']    = main_mail

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()

server.login(main_mail, password)
email_data    = csv.reader(open('emails.csv', 'rb'))
email_pattern = re.compile("^.+@.+\..+$")

for row in email_data:
    if (email_pattern.search(row[1])):
        del msg['To']
        msg['To'] = row[1]
        try:
            server.sendmail(main_mail, [row[1]], msg.as_string())
        except smtplib.SMTPException:
            print("An error occured.")
server.quit()