# Documentatie_Mail/main.py


from Documentatie_Mail.data import EMAIL_DATA
from Documentatie_Mail.service import send_documentatie_mail


def main():
    send_documentatie_mail(EMAIL_DATA)

if __name__ == "__main__":
    main()
