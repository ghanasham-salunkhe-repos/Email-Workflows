def send_email():
    import smtplib
    import os
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from cryptography.fernet import Fernet

    # Load the encrypted password from environment variable
    encrypted_password = os.environ.get('GMAIL_PASSWORD')

    # Decrypt the password
    key = b'your_fernet_key_here'  # Replace with your actual Fernet key
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()

    # Email configuration
    sender_email = "your_email@gmail.com"  # Replace with your email
    receiver_emails = os.environ.get('RECEIVER_EMAILS', '')
    receiver_list = [email.strip() for email in receiver_emails.split(',') if email.strip()]
    subject = "Daily Email"
    body = "This is your daily email."

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(receiver_list)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, decrypted_password)
            server.sendmail(sender_email, receiver_list, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_email()