def get_domain(emails: tuple) -> list:
    domains = []

    for i, j in emails:
        idx = j.find('@')
        if j[idx:] not in domains:
            domains.append(j[idx:])
    
    return domains

emails = (("Ali", "ali@gmail.com"), ("Vali", "vali@yandex.ru"), ("Sami", "sami@mail.ru"))
print(get_domain(emails))
