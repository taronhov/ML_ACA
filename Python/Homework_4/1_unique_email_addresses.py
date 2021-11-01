def addr_modify(email):
    name, domain = email.split('@')
    
    for char in name:
        if char == '+':
            name = name[0:name.index(char)]
            break
    
    final_name = "".join(name.split("."))

    return ("".join([final_name, '@', domain]))


def unique_addresses(emails):
    unique_addr = set()

    for email in emails:
        unique_addr.add(addr_modify(email))
        
    return (unique_addr, len(unique_addr))


# Main part
emails_str = input("Eter the list of emails: ")

emails_list = emails_str.strip().split()

print(unique_addresses(emails_list)[1])
