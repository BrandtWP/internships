firstName = input("Enter lead firstname: ")
lastName = input("Enter lead lastname: ")
company = input("Enter company url (omit https:// just domainName.TLD): ")

usernames = [
    firstName[0] + lastName,
    firstName,
    lastName, 
    firstName + lastName,
    firstName + '.' + lastName,
    firstName[0] + '.' + lastName,
    firstName[0] + lastName[0],
    firstName[0] + '.' + lastName[0],
    firstName + lastName[0],
    firstName + '.' + lastName[0],
    lastName + '.' + firstName,
    lastName + firstName]
    
emails = [username + "@" + company for username in usernames]

print(', '.join(emails))