import smtplib
from email.message import EmailMessage
import creds


email = creds.email()
password = creds.app_password()

def send_email(subject, body, to_email):
    from_email = email
    app_password = password
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(body)    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(from_email, app_password)
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def sent():
    to_email = email
    send_email(
        subject="NCAA Website has been Updated",
        body=(
            f"Hello {', '.join(to_email)},\n\n"
            "The NCAA has been updated, so I believe it would be time to check the script to see if anything has been updated.\n\n"
            "Have a great day :) \n\n"
            "Best,\n\n"
            "Jason Rodriguez"
        ),
        to_email=to_email
    )

sent()