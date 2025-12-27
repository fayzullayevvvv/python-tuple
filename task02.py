def count_math(students: list[tuple[str, list]]) -> str:
    count_math = 0
    for name, scene in students:
        if scene:
            if 'Matematika' in scene:
                count_math += 1
    
    return '{} ta talaba Matematika fanini tanlagan.'.format(count_math)
    

students = [("Ali", ["Fizika", "Matematika"]), ("Laylo", ["Ingliz tili"]), ("Jasur", ["Matematika", "Informatika"])]

print(count_math(students))