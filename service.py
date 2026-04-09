# Documentatie_Mail/service.py

from Documentatie_Mail.email_builder import build_subject, build_body, derive_cc_from_trades
from Documentatie_Mail.send_email import send_email

# These were in your main.py as FIXED_CC 
FIXED_CC = [
    "Robbert van Riel",
    "Bob Stroeken",
    "StructuredInvestments",
]

def send_documentatie_mail(email_data: dict) -> None:
    """
    GUI-friendly entrypoint.
    Input: email_data dict (same shape as your old EMAIL_DATA)
    Output: sends Outlook mail
    """
    subject = build_subject(email_data)
    body = build_body(email_data)

    # Start with fixed CC + any CC already provided + helper CC derived from trades
    cc_names = []
    cc_names.extend(FIXED_CC)
    cc_names.extend(email_data.get("cc", []))
    cc_names.extend(derive_cc_from_trades(email_data.get("trades", [])))

    # Remove duplicates but keep order
    seen = set()
    cc_names_unique = []
    for name in cc_names:
        if name and name not in seen:
            seen.add(name)
            cc_names_unique.append(name)

    send_email(
        subject=subject,
        html_body=body,
        to_names=email_data.get("to", []),
        cc_names=cc_names_unique,
    )

def build_documentatie_mail(email_data: dict):
    subject = build_subject(email_data)
    body = build_body(email_data)
    to_names = email_data.get("to", [])
    cc_names = sorted(
        set(email_data.get("cc", []))
        | set(FIXED_CC)
        | set(derive_cc_from_trades(email_data.get("trades", [])))
    )
    return subject, body, to