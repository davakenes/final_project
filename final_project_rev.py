
#import sending function
import smtplib
#code untuk outer email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#code untuk menambah attachment
from email.mime.base import MIMEBase
from email import encoders
#code untuk hapus file
import os

#user input untuk email yang ingin dikirimkan
jumlah_email = int(input("Berapa jumlah email : "))
for i in range(jumlah_email):
    print("Data ke {}" .format(i+1))
    user_email = input()
    penerima = open("receiver_list.txt" , "a")
    penerima.write (user_email + ",")
    penerima.close()
#buka file yang berisi email yang di input
file_list = open("receiver_list.txt" , "r")
teks = str(file_list.read())
file_list.close()



email_user = "davaputera886@gmail.com"
subject = "WEBINAR EARTH HOUR 2021 by IGAF"

#mengisi outer email
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = teks
msg['Subject'] = subject
body = "Salam Sejahtera,\n Berikut adalah sertifikat Anda setelah mengikuti Webinar EH 2021 !\n Terimakasih atas partisipasinya !"
msg.attach(MIMEText(body,'plain')) #plain maksudnya pesan biasa, 


#membuka dan upload attachment
filename="Sertifikat.pdf"
attachment  =open("D:\\Career\\Sertifikat.pdf",'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)
msg.attach(part)



#login ke email pengirim
server = smtplib.SMTP('smtp.gmail.com', 587) #connect to name and port server
server.starttls()
server.login(email_user, "davakenes56") #autentifikasi

text = msg.as_string() #konversi objek message ke string


#kirim
server.sendmail(email_user, teks.split(",") , text)


#disconnect dari server
server.quit()

os.remove("receiver_list.txt")
