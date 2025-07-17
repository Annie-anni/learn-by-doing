import smtplib

email = input("Sender email: ") #发送者的邮箱
receiver_email = input("Receiver email: ") #接受者的邮箱

subject = input("Subject: ") #标题
message = input("Message: ") #内容

text = f"Subject: {subject}\n\n{message}" 

server = smtplib.SMTP("smtp.gmail.com",587) #服务器
server.starttls()

server.login(email,"yvuj kexn nezl akpi")

server.sendmail(email,receiver_email,text)

print("Email has been sent to " + receiver_email)



# email = "liud76942@gmail.com"
# receiver_email = ""

# subject = ""
# message = ""

# text = f"Subject: {subject}\n\n{message}"

# server = smtplib.SMTP("smtp.gmail.com",587)
# server.starttls()

# server.login(email,"yvuj kexn nezl akpi")

# server.sendmail(email,receiver_email,text)

# print("Email has been sent to " + receiver_email)