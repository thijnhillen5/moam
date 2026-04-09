




def send_email(subject, html_body, to_names, cc_names):
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    import win32com.client
    mail.Subject = subject

    # Add TO recipients by name
    for name in to_names:
        r = mail.Recipients.Add(name)
        r.Type = 1  # 1 = To

    # Add CC recipients by name
    for name in cc_names:
        r = mail.Recipients.Add(name)
        r.Type = 2  # 2 = CC

    # Force Outlook to resolve names (Ctrl+K behavior)
    mail.Recipients.ResolveAll()

    mail.Display()  # load signature
    signature = mail.HTMLBody
    mail.HTMLBody = html_body + signature
