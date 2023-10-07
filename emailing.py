import smtplib
from email.message import EmailMessage
import imghdr

password="duechdfncjtfzggy"
sender="dandonapari@gmail.com"
reciever="dandonapari@gmail.com"

def send_email(image_path):
    print("send email function started")
    email_message=EmailMessage()
    email_message['Subject']="New Object detected!"
    email_message.set_content("Hey,we just detected a new object!")

    with open(image_path,'rb') as file:
        content=file.read()
    email_message.add_attachment(content,maintype="image",subtype=imghdr.what(None,content))

    gmail=smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender,password)
    gmail.sendmail(sender,reciever,email_message.as_string())
    gmail.quit()
    print("send email function ended")

if __name__=="__main__":
    send_email(image_path="images/*.png")