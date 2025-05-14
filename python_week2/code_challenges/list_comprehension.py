def find_common_elements():
    """
    Accepts user input to create two sets of integers and
    then finds and prints the common elements.
    """
    set1 = get_integer_set("first")
    set2 = get_integer_set("second")

    common_elements = set1.intersection(set2)

    print("\nFirst Set:", set1)
    print("Second Set:", set2)
    print("Common Elements:", common_elements)

def get_integer_set(set_name):
    """
    Accepts user input to create a set of integers.
    """
    integer_set = set()
    print(f"\nEnter integers for the {set_name} set (type 'done' to finish):")
    while True:
        try:
            user_input = input("> ")
            if user_input.lower() == 'done':
                break
            integer = int(user_input)
            integer_set.add(integer)
        except ValueError:
            print("Invalid input. Please enter an integer or 'done'.")
    return integer_set

if __name__ == "__main__":
    find_common_elements()
