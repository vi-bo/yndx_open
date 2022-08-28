import csv

def get_ids():
    ids = []
    with open('promo-users.csv') as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            ids.append(row[0])
    return ids

def get_emails(ids):
    emails = []
    with open('users.csv') as f:
        r = csv.reafer(f)
        next(r)
        for row in r:
            id_ = row[0]
            if id_ in ids:
                emails.append(row[3])
    return emails

def write_emails(emails):
    with open('emails.csv', 'w') as f:
        r = csv.writer(f)
        r.writerow(['email'])
        for email in emails:
            r.writerow([email])

def main():
    ids = get_ids
    emails = get_emails(ids)
    write_emails(emails)

if __name__ == '__main__':
    main()