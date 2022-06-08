class NameTooShortError(Exception):
    '''Name must be more than 4 characters'''
    pass

class MustContainAtSymbolError(Exception):
    '''Email must contain @'''
    pass

class InvalidDomainError(Exception):
    '''Domain must be one of the following: .com, .bg, .org, .net'''
    pass

valid_domains = {"com", "bg", "net", "org"}

text = input()

while text != 'End':
    email = text
    parts = email.split('@')
    if len(parts) != 2:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain_name = parts

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = domain_name.split('.')[-1]

    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    text = input()