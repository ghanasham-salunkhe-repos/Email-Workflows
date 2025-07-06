# GitHub Mail Workflow

This project sets up a GitHub Actions workflow that sends a daily email using the Gmail SMTP server. The email is sent by executing a Python script that connects to the SMTP server, authenticates using an encrypted password, and sends the email.

## Project Structure

```
github-mail-workflow
├── .github
│   └── workflows
│       └── send_mail.yml
├── src
│   └── main.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Create a GitHub Repository**:
   - Create a new repository on GitHub named `github-mail-workflow`.

2. **Clone the Repository**:
   - Clone the repository to your local machine.

3. **Set Up the Project Structure**:
   - Create the directory structure as specified above.

4. **Write the Email Sending Code**:
   - Implement the email sending functionality in `src/main.py`. Ensure to use the `smtplib` library for connecting to the Gmail SMTP server.

5. **Encrypt Your Gmail Password**:
   - Use a tool like `openssl` to encrypt your Gmail password. For example:
     ```
     echo "your_password" | openssl enc -aes-256-cbc -a -salt
     ```
   - Store the encrypted password securely.

6. **Store Secrets in GitHub**:
   - Go to your GitHub repository settings.
   - Under "Secrets and variables", add a new secret named `GMAIL_PASSWORD` and paste the encrypted password.

7. **Create the GitHub Actions Workflow**:
   - In `.github/workflows/send_mail.yml`, define the workflow to run daily. The workflow is scheduled to run every day at 9 AM UTC.

8. **Add Dependencies**:
   - In `requirements.txt`, list the necessary libraries, such as:
     ```
     smtplib
     email
     ```

9. **Test the Workflow**:
   - Push your changes to the repository and check the Actions tab on GitHub to ensure the workflow runs successfully.

## Usage

Once the setup is complete, the workflow will automatically send an email to the specified recipient every day at the scheduled time. Make sure to check the Actions tab for logs and any potential errors.

## Notes

- Ensure that your Gmail account allows access from less secure apps or use an App Password if you have 2-Step Verification enabled.
- Modify the email content and recipient in the `src/main.py` file as needed.