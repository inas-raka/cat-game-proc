def display_stats(cat):
    print("\nCurrent cat stats:")
    print(f"Name: {cat['name']}")
    print(f"Color: {cat['color']}")
    print(f"Intelligence: {cat['intelligence']}")
    print(f"Energy: {cat['energy']}")
    print(f"Weight: {cat['weight']}\n")


cat = {
    'name': '',
    'color': '',
    'intelligence': 10,  
    'energy': 50,        
    'weight': 10        
}


cat['name'] = input("What is your cat's name? ")
cat['color'] = input("What is your cat's color? ")

while True:
    print("\nWhat would you like to do with your cat?")
    print("1. Play with your cat")
    print("2. Train your cat")
    print("3. Feed your cat")
    print("4. Put your cat to sleep")
    print("5. Show stats")
    print("6. Exit game")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
       
        if cat['energy'] < 5:
            print("\nYour cat is too tired to play! You need to put them to sleep or feed them first.")
        else:
            print(f"\nYou play with {cat['name']}! They seem to enjoy it.")
            cat['energy'] -= 10  
            cat['weight'] -= 1   
            cat['intelligence'] += 1  

    elif choice == '2':
       
        if cat['energy'] < 10:
            print("\nYour cat is too tired to train! They need more energy.")
        else:
            print(f"\nYou train {cat['name']}!")
            cat['energy'] -= 15 
            cat['intelligence'] += 3  

    elif choice == '3':
       
        print(f"\nYou feed {cat['name']}!")
        cat['energy'] += 20  
        cat['weight'] += 2   

    elif choice == '4':
       
        print(f"\nYou put {cat['name']} to sleep!")
        cat['energy'] += 30  
        cat['weight'] += 1   

    elif choice == '5':
       
        display_stats(cat)

    elif choice == '6':
        
        print("\nThanks for playing with your cat! Goodbye!")
        break  

    else:
        print("\nInvalid choice. Please select a valid option.")
