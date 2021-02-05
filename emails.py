firstName = "chad"
lastName = "doerge"
company = "aiera.com"

usernames = [firstName[0] + lastName, firstName, lastName, firstName + lastName, firstName + '.' + lastName, firstName[0] + '.' + lastName, firstName[0] + lastName[0], firstName[0] + '.' + lastName[0],  firstName + lastName[0], firstName + '.' + lastName[0], lastName + '.' + firstName, lastName + firstName]
emails = [username + "@" + company for username in usernames]

print(', '.join(emails))