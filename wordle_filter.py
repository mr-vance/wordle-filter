import re

def prompt_user_input():
    # Prompt user for non-existing letters (NEL)
    nel = input("Enter non-existing letters in the word separated by comma: ").replace(" ", "").split(',')
    nel = [letter.lower() for letter in nel if letter]  # Clean and normalize input
    
    # Prompt user for existing letters in incorrect positions (ELIP)
    elip_input = input("Enter existing letters in the word separated by comma: ").replace(" ", "").split(',')
    elip = [(letter.lower(), -1) for letter in elip_input if letter]  # Normalize and assume unknown positions

    # Prompt user for letters in correct positions (ELCP)
    elcp = []
    for i in range(5):
        letter = input(f"Enter letter in position {i + 1} (leave empty if none): ").lower()
        if letter:
            elcp.append((letter, i))

    return nel, elip, elcp

def wordle_filter(dictionary, nel, elip, elcp):
    # Condition 1: Exclude words with letters in NEL
    nel_pattern = f"[{''.join(nel)}]"
    filtered_words = [word for word in dictionary if not re.search(nel_pattern, word)]
    
    # Condition 2: Ensure ELIP letters are present but not in specific positions
    for letter, _ in elip:
        elip_pattern = f"{letter}"
        filtered_words = [word for word in filtered_words if re.search(elip_pattern, word)]
    
    # Condition 3: Ensure ELCP letters are in the correct positions
    for letter, pos in elcp:
        elcp_pattern = f"^{'.' * pos}{letter}"
        filtered_words = [word for word in filtered_words if re.search(elcp_pattern, word)]
    
    return filtered_words

def load_dictionary(file_path):
    try:
        with open(file_path, 'r') as file:
            words = [line.strip().lower() for line in file]
        return words
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred while loading the dictionary: {e}")
        return []

# Main program
if __name__ == "__main__":
    # Path to the five-letter words dictionary
    dictionary_file = 'fiveLetterWords.txt'
    dictionary = load_dictionary(dictionary_file)

    if dictionary:
        # Prompt user for input
        nel, elip, elcp = prompt_user_input()

        # Filter words based on user input
        filtered_words = wordle_filter(dictionary, nel, elip, elcp)

        # Display the filtered words
        print("Filtered words:", filtered_words)