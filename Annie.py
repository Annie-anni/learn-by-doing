import smtplib

email = input("Sender Email: ")
receiver_email = input("Receiver Email: ")

subject = input("Subject: ")
message = input("Message: ")

text = f"Subject: {subject}\n\n{message}"
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(email,"jgcj fvkr gsek tuad")
server.sendmail(email,receiver_email,text)
print("Email has been sent to " + receiver_email)
