def sum_list_integers():
    """
    Accepts user input to create a list of integers and then computes their sum.
    """
    integer_list = []
    while True:
        try:
            user_input = input("Enter an integer (or type 'done' to finish): ")
            if user_input.lower() == 'done':
                break
            integer = int(user_input)
            integer_list.append(integer)
        except ValueError:
            print("Invalid input. Please enter an integer or 'done'.")

    if integer_list:
        list_sum = sum(integer_list)
        print(f"\nThe list of integers you entered is: {integer_list}")
        print(f"The sum of the integers in the list is: {list_sum}")
    else:
        print("\nYou didn't enter any integers.")

if __name__ == "__main__":
    sum_list_integers()
