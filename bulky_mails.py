import smtplib
from email.message import EmailMessage

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SENDER_EMAIL = 'demo@gmail.com'
SENDER_PASSWORD = 'xxxx xxxx xxxx xxxx'  # Use an app-specific password if using Gmail

def get_recipients():
    # Take input from user for recipient emails
    recipients_input = input("Enter recipient email addresses separated by commas: ")
    # Split the input string into a list of email addresses
    recipients = [email.strip() for email in recipients_input.split(',')]
    return recipients

def send_bulk_email(subject, body):
    try:
        # Get recipients from user input
        recipients = get_recipients()
        
        # Create an EmailMessage object
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = SENDER_EMAIL
        msg['To'] = ', '.join(recipients)  # Set the 'To' header to a comma-separated string of recipients
        msg.set_content(body)
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
            print(f"Email sent to {', '.join(recipients)}")

    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
subject = input("Enter the email subject: ")
body = input("Enter the email body: ")
send_bulk_email(subject, body)
