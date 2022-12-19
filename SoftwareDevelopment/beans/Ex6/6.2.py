def GetEmail():
    inputEmail = str( input("Please enter email address: ") )
    while inputEmail.count("@") !=1 or ( int( inputEmail.index("@") ) <3):
        print("Invalid email format. | Please re-enter email!\nexample@example.com")
        inputEmail = str( input("Please enter your email address: ") )
    finalemail = inputEmail.strip(" ")
    return finalemail

def ProcessEmail(email):
    pos = int(email.index("@"))
    mailbox = email[0:pos]
    domain = email[pos:]
    return mailbox,domain

def DisplayDetails(emial,domain):
    print(f'Mailbox = {emial}')
    print(f'Domain = {domain}')

email = GetEmail()
mailbox,domain = ProcessEmail(email)
DisplayDetails(mailbox, domain)