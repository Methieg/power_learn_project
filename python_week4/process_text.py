#!/bin/python3
def read_file(filename):
    """Reads the content of a file.

    Args:
        filename (str): The name of the file to read.

    Returns:
        str: The content of the file, or None if an error occurs.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

def count_words(text):
    """Counts the number of words in a string.

    Args:
        text (str): The string to count words in.

    Returns:
        int: The number of words in the string.
    """
    words = text.split()
    return len(words)

def convert_to_uppercase(text):
    """Converts a string to uppercase.

    Args:
        text (str): The string to convert.

    Returns:
        str: The uppercase version of the string.
    """
    return text.upper()

def write_to_file(filename, content):
    """Writes content to a file.

    Args:
        filename (str): The name of the file to write to.
        content (str): The content to write.
    """
    try:
        with open(filename, 'w') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error writing to file '{filename}': {e}")
        return False

if __name__ == "__main__":
    input_filename = "input.txt"
    output_filename = "output.txt"

    file_content = read_file(input_filename)

    if file_content is not None:
        word_count = count_words(file_content)
        uppercase_text = convert_to_uppercase(file_content)

        output_content = f"Processed Text (Uppercase):\n{uppercase_text}\n\nWord Count: {word_count}\n"

        if write_to_file(output_filename, output_content):
            print(f"Successfully processed '{input_filename}' and created '{output_filename}'.")
        else:
            print("Processing completed, but there was an issue writing to the output file.")
