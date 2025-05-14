def get_person_info():
    """
    Asks the user for information about a person and stores it in a dictionary.
    Then, prints the dictionary.
    """
    person_info = {}

    person_info['name'] = input("Enter the person's name: ")
    while True:
        try:
            person_info['age'] = int(input("Enter the person's age: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid age (an integer).")
    person_info['favorite_color'] = input("Enter the person's favorite color: ")

    print("\nPerson Information:")
    print(person_info)

if __name__ == "__main__":
    get_person_info()
