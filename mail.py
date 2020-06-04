import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

server.login('rahul.dss@gmail.com', '')

subject = "Email From Python!"
body = "Test Body"
msg = f"Subject: {subject}\n\n{body}"

server.sendmail(
    'rahul.dss@gmail.com',
    'narender.netsoft@gmail.com',
    msg
)
print('Email sent!!!')
server.quit()
