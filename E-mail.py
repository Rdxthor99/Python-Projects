import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email and password (make sure to use an App Password if using Gmail)
sender_email = "demo@gmail.com"
sender_password = "xxxx xxxx xxxx xxxx"

# Recipient email address
receiver_email = input("Enter the receiver E-mail address: ")


# Email subject and body
subject = input("Enter the subject : ")
body = input("Enter the message you want to deliver : ")

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Add body to email
message.attach(MIMEText(body, "plain"))

# SMTP server configuration (for Gmail)
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Start TLS (Transport Layer Security) connection
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

# Login to SMTP server using sender email and password
server.login(sender_email, sender_password)

# Send email
server.sendmail(sender_email, receiver_email, message.as_string())

# Quit SMTP server
server.quit()

# elif user_choice==5:
    

print("Email sent successfully to", receiver_email)
