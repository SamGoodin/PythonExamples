import smtplib, ssl

port = 465
email_password = input("Type your password: " )
sender = "leumasnidoog@gmail.com"
receivers = ['sgoodin1998@gmail.com']

message = """\
Subject: Yo

I sent this with Python
"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, email_password)
    
    
    
    # Send email
    server.sendmail(sender, receivers, message)