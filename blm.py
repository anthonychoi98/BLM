import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from credentials import *

with open('us-house.json') as json_file:
    data = json.load(json_file)
    for p in data:
        send_to_email = p['name'].replace(' ', '.') + '@mail.house.gov'
        print("sendtoemail: " + send_to_email)
        if p['gender'] == 'male':
            mrormrs = 'Mr. '
        else:
            mrormrs = 'Mrs. '

        subject = "End Qualified Immunity"
        message = "Hello " + mrormrs + " " + p['name'] + ",\n\n" + "My name is Anthony Choi and as a proud Asian American I would like to implore you to support the Ending Qualified Immunity Act in light of the George Floyd protests. " + "This will aid in setting law enforcement to a higher standard and may impede future incidents like what we saw last week with George Floyd. " + "A moral and good officer would have nothing to lose from this motion and I hope you feel the same. " + "You have power and influence that can actually make a real difference for those that are hurting and I hope you hear us out. " + "Thanks!\n\n" + "Best Regards,\n" + "Anthony Choi"

        msg = MIMEMultipart()
        msg["From"] = email
        msg["To"] = send_to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        server.quit()
