pip install -r requirement.txt



### send mail SMTP, SendGrid, or Amazon SES

##### in this repo that use Amazon SES

- To use flask_mail with Amazon SES, you will need to configure your application to use the Amazon SES SMTP interface. Here's how you can do it
```bash
pip install boto3
```


```py
MAIL_SERVER = 'email-smtp.us-east-1.amazonaws.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'your_ses_smtp_username'
MAIL_PASSWORD = 'your_ses_smtp_password'
MAIL_DEFAULT_SENDER = 'your_default_sender_email_address'
```


##### for SendGrid

Create a SendGrid account and obtain an API key. You can sign up for a free account at https://sendgrid.com/free/.

```bash
pip install sendgrid
```

```py
MAIL_SERVER = 'smtp.sendgrid.net'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'apikey'
MAIL_PASSWORD = 'your_sendgrid_api_key'
MAIL_DEFAULT_SENDER = 'your_default_sender_email_address'
```

```py
from flask_mail import Message

message = Message(subject='Hello from Flask-Mail',
                  recipients=['recipient@example.com'])
message.body = 'This is a test email sent from Flask-Mail using SendGrid.'
mail.send(message)
```

