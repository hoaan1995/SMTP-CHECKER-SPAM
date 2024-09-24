import smtplib
import threading

def check_smtp_server(mail_host, mail_port, mail_user, mail_pass):
    try:
        server = smtplib.SMTP(mail_host, int(mail_port))
        server.starttls()
        server.login(mail_user, mail_pass)
        print(f"SMTP server {mail_host}:{mail_port} is live")
        with open('live.txt', 'a') as live_file:
            live_file.write(f"{mail_host}:{mail_port}:{mail_user}:{mail_pass}\n")
        server.quit()
    except smtplib.SMTPAuthenticationError:
        print(f"SMTP server {mail_host}:{mail_port} is live, but authentication failed")
    except smtplib.SMTPConnectError:
        print(f"SMTP server {mail_host}:{mail_port} is not reachable")
    except Exception as e:
        print(f"An error occurred while connecting to SMTP server {mail_host}:{mail_port}: {str(e)}")

def check_smtp_servers(filename):
    threads = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                mail_host, mail_port, mail_user, mail_pass = line.split(':')
                thread = threading.Thread(target=check_smtp_server, args=(mail_host, mail_port, mail_user, mail_pass))
                thread.start()
                threads.append(thread)

    for thread in threads:
        thread.join()

check_smtp_servers('servers.txt')
