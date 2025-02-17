# Q3. Uptime Monitoring and Alert System

# Write a Python script that checks the uptime of provided URLs and 
# notifies the user if any of the URLs return 4xx or 5xx HTTP status 
# codes (indicating client or server errors). 
# For demonstration purposes, you can use the following URLs as inputs

import time
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

import requests as rq
url=input("Enter the URL: ")

while True:
    file=open("answer3logs.txt","a")
    req=rq.get(url)
    print(str(req))
    file.write(f"\n{str(req)}")
    # message=f"Subject: {url} is down\n\nThe URL {url} is down. Please check it."
    time.sleep(5)
    file.close()




# if req.status_code>=400:

#     def send_email(subject,body, to_email):
#         from_email = "viransh.bhardwaj@cloudkeeper.com"
#         from_password = "vlitnqccszqlnhle"

#         msg = MIMEMultipart()
#         msg['From'] = from_email
#         msg['To'] = to_email
#         msg['Subject'] = subject
#         msg.attach(MIMEText(body, 'plain'))

#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(from_email, from_password)

#         # Send the email
#         server.send_message(msg)
#         server.quit()
#     print(message)
#     send_email("URL Down",f"{message}", "viranshbhardwaj110203@gmail.com")
# else:
#     print("The URL is working fine\nStatus code: ",req.status_code)

