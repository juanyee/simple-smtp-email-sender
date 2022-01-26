import smtplib
import input_variables as var
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = f'Test'
msg['From'] = var.FROM_EMAIL
msg['To'] = ', '.join(var.TO_EMAILS)
msg.set_content(f"Hello")
with smtplib.SMTP(var.SERVER, var.PORT) as s: # pending to remove "587"
    s.starttls() # pending to remove
    s.login(var.SENDER, var.PASSWORD) # pending to remove
    s.send_message(msg)
    s.quit()
