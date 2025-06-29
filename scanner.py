import re

def scan_text(text):
    leaks = []
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    if emails:
        leaks.extend(emails)
    return leaks

