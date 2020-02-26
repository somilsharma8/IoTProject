import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("somilsharma8@gmail.com", "somil528491")
 
msg = "Server Compromised!"
sender_id="somilsharma8@gmail.com"
receiver_id="somil_rajesh@srmuniv.edu.in"
server.sendmail(sender_id, receiver_id, msg)
server.quit()
