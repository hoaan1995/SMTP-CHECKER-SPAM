input_file = "smtp.txt"
output_file = "servers.txt"

with open(input_file, "r") as input_f, open(output_file, "w") as output_f:
    lines = input_f.readlines()
    smtp_data = []

    for line in lines:
        if line.startswith("URL:"):
            smtp_entry = {}
        elif line.startswith("METHOD:"):
            smtp_entry["METHOD"] = line.split(":")[1].strip()
        elif line.startswith("MAILHOST:"):
            smtp_entry["MAILHOST"] = line.split(":")[1].strip()
        elif line.startswith("MAILPORT:"):
            smtp_entry["MAILPORT"] = line.split(":")[1].strip()
        elif line.startswith("MAILUSER:"):
            smtp_entry["MAILUSER"] = line.split(":")[1].strip()
        elif line.startswith("MAILPASS:"):
            smtp_entry["MAILPASS"] = line.split(":")[1].strip()
        elif line.startswith("MAILFROM:"):
            smtp_entry["MAILFROM"] = line.split(":")[1].strip()
        elif line.startswith("FROMNAME:"):
            smtp_entry["FROMNAME"] = line.split(":")[1].strip()
            smtp_data.append(smtp_entry)

    for smtp_entry in smtp_data:
        mail_host = smtp_entry.get("MAILHOST", "")
        mail_port = smtp_entry.get("MAILPORT", "")
        mail_user = smtp_entry.get("MAILUSER", "")
        mail_pass = smtp_entry.get("MAILPASS", "")
        output_line = f'{mail_host}:{mail_port}:{mail_user}:{mail_pass}\n'
        output_f.write(output_line)
