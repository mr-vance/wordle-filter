# WORDLE FILTER

## Project Overview

The **WORDLE FILTER** app is a cross-platform tool designed to assist Wordle players in narrowing down their options for five-letter English words based on the feedback received during the game. This app can be used offline, leveraging an onboard dictionary file containing all five-letter English words. The app helps players from their second Wordle attempt up to the sixth by filtering words according to specific criteria provided by the player.

## Features

- **Cross-Platform Compatibility**: Works on various operating systems.
- **Offline Usage**: No internet connection is required as it uses a local dictionary file.
- **User-Friendly Input**: Prompts users to enter non-existing letters, existing letters in incorrect positions, and letters in correct positions.
- **Efficient Filtering**: Filters the list of possible words based on user input and returns all words that match the criteria.

## Time Complexity

The program is designed with efficiency in mind, following a logical filtering process. The overall time complexity is:

`[O(N * (k + m + l))]`

Where:
- \(N\) is the number of words in the dictionary.
- \(k\) is the length of the Non-Existing Letters list (NEL).
- \(m\) is the length of the Existing Letters in Incorrect Positions list (ELIP).
- \(l\) is the length of the Existing Letters in Correct Positions list (ELCP).

### Filtering Logic
1. **Condition 1 (NEL)**: Filter out words containing any letters from the NEL list.
2. **Condition 2 (ELIP)**: Further filter words to ensure they contain all letters from the ELIP list, but not in the specified positions.
3. **Condition 3 (ELCP)**: Finally, filter words that have specific letters in the correct positions as defined by the ELCP list.

This sequence ensures that the most restrictive conditions are applied first, minimizing the number of checks needed and enhancing the performance of the filtering process.

## Installation

1. Clone this repository to your local machine.
2. Ensure Python is installed (Python 3.7+ recommended).
3. Install any necessary dependencies (though standard libraries should suffice).

## Usage

### Running the Wordle Filter Program

1. Prepare a text file (`englishWords.txt`) containing a list of English words separated by new lines.
2. Run the following Python script to filter five-letter words from the dictionary:

```python
def filter_five_letter_words(input_file, output_file):
    # Implement the code provided earlier here
```
3. This will generate a `fiveLetterWords.txt` file containing only the five-letter words.

### Running the WORDLE FILTER App
1. Run the `wordle_filter.py` script.

2. The program will prompt you for:
   - Non-existing letters: Enter letters that are not in the word, separated by commas.
   - Existing letters: Enter letters that are in the word but in incorrect positions, separated by commas.
   - Letters in correct positions: Enter letters for each specific position in the word.
3. The filtered list of words will be displayed, narrowing down your choices for the next Wordle attempt.

### Example Usage
```python
dictionary = ["apple", "arose", "aloft", "brave", "crane"]

nel, elip, elcp = prompt_user_input()

filtered_words = wordle_filter(dictionary, nel, elip, elcp)

print("Filtered words:", filtered_words)
```

## Contribution
Contributions are welcome! If you have suggestions or improvements, please submit a pull request or open an issue.

## License
This project is open-source and available under the MIT License.