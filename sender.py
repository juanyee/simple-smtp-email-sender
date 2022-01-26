import smtplib
import input_variables as var
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = f'Test'
msg['From'] = var.FROM_EMAIL
msg['To'] = ', '.join(var.TO_EMAILS)
msg.set_content(f"Hello", subtype='html')
with smtplib.SMTP(var.SERVER, var.PORT) as s:
    s.starttls()
    s.login(var.SENDER, var.PASSWORD)
    s.send_message(msg)
    s.quit()
