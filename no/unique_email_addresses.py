#!/home/srini/.checkio/checkio_chrome_plugin.py --domain=py run unique-email-addresses
def unique_emails(emails: list[int]) -> int:
    # your code here
    for i,x in enumerate(emails):
        if len(emails)==0:
            break
        else:
            if '+' in x:
                x = x.replace(x[x.index('+'):x.index('@')],'')
            if '.' in x[:x.index('@')]:
                x = x[:x.index('@')].replace('.',"")+x[x.index('@'):]
            emails[i] = x.lower()
    return len(set(emails))


print("Example:")
print(unique_emails(["alex@checkio.org", "mike@google.com", "lili@apple.com"]))

assert unique_emails(["alex@checkio.org", "mike@google.com", "lili@apple.com"]) == 3
assert (
    unique_emails(
        ["mi.ke@google.com", "alex@checkio.org", "mike@google.com", "lili@apple.com"]
    )
    == 3
)
assert (
    unique_emails(
        [
            "alex+home@checkio.org",
            "lili+work@apple.com",
            "alex@checkio.org",
            "lili@apple.com",
        ]
    )
    == 2
)
assert (
    unique_emails(
        [
            "l.ili+work@apple.com",
            "a.lex@checkio.org",
            "alex+home@checkio.org",
            "lili+work@apple.com",
            "alex@checkio.org",
            "lili@apple.com",
        ]
    )
    == 2
)
assert unique_emails(["Alex@checkIO.org", "alex@checkio.org", "alex@check.io.org"]) == 2
assert unique_emails([]) == 0

print("The first mission is done! Click 'Check' to earn cool rewards!")
