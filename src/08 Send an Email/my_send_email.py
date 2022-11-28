import smtplib, ssl

def send_email(recipient: str, subject: str, body: str) -> None:
    login = ""
    password = input("Password here: ")
    port = 465
    message = f'Subject: {subject}\n\n{body}'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context) as server:
        server.login(login, password)
        server.sendmail(login, recipient, message)

subj = "HAHAHA"
bod = "hahahah"
recip = ""
send_email(recip, subj, bod)
