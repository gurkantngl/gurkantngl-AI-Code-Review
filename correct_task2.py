def count_valid_emails(emails):
    count = 0

    for email in emails:
        if not isinstance(email, str):
            continue
        email = email.strip()
        parts = email.split("@")
        if len(parts) != 2:
            continue
        local, domain = parts
        if not local or not domain:
            continue
        count += 1

    return count