def filter_five_letter_words(input_file, output_file):
    try:
        # Open the input file and read the lines
        with open(input_file, 'r') as infile:
            words = infile.readlines()

        # Filter for five-letter words (strip newline characters and check length)
        five_letter_words = [word.strip() for word in words if len(word.strip()) == 5]

        # Write the five-letter words to the output file
        with open(output_file, 'w') as outfile:
            for word in five_letter_words:
                outfile.write(word + '\n')

        print(f"Filtered {len(five_letter_words)} five-letter words to {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the input and output file names
input_file = 'words.txt'  # Replace with the path to your input file
output_file = 'fiveLetterWords.txt'

# Run the function
filter_five_letter_words(input_file, output_file)
