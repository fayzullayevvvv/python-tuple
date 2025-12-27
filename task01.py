def find_oldest_person(person):
    if person:
        name = person[0][0]
        age = person[0][1]

        for i, j in person:
            if age < j:
                age = j
                name = i
            
        return '{} {} yosh'.format(name, age)


peoples = [("Ali", -34), ("Laylo", -30), ("Jasur", -19)]

print(find_oldest_person(peoples))