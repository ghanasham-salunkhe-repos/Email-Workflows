def send_email():
    import os
    from mailjet_rest import Client

    api_key = os.environ.get('MAILJET_API_KEY')
    api_secret = os.environ.get('MAILJET_API_SECRET')
    receiver_emails = [email.strip() for email in os.environ.get('RECEIVER_EMAILS', '').split(',') if email.strip()]

    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
      'Messages': [
        {
          "From": {
            "Email": "ghanshamsalunkhe0@gmail.com",
            "Name": "GitHub Mailer"
          },
          "To": [{"Email": email} for email in receiver_emails],
          "Subject": "Daily Email",
          "TextPart": "This is your daily email."
        }
      ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())

if __name__ == "__main__":
    send_email()