def dict_persons():
    dict_name = input("What is your name: ")
    dict_age = int(input("How old are you? "))
    dict_city = input("Where do you live? ")
    person = {'name':dict_name,'age':dict_age,'city':dict_city}
    print(f"\nRecapitulatif\n Nom: {person['name']}\nAge: {person['age']}\nAdresse: {person['city']}\n\n")
    person['age'] = int(input("Thanks to give you a new age: "))
    print(f"\nUpdate Recapitulatif\n Nom: {person['name']}\nAge: {person['age']}\nAdresse: {person['city']}\n\n")
    person['occupation'] = input("What is your profession? ")
    print(f"\nUpdate Recapitulatif\n Nom: {person['name']}\nAge: {person['age']}\nAdresse: {person['city']}\nOccupation: {person['occupation']}\n")
    
