import hm_ascii_art as hm_module
import random

def get_random_word(word_list):
  """ This function returns a random string from the passed list of strings."""
  word_index = random.randint(0, len(word_list) - 1)
  return word_list[word_index]

def display_board(missed_letters, correct_letters, secret_word):
  """ This function creates the board game.

  Params:
    missed_letters (str): string 
    correct_letters (str): string
    secret_word (str): string
  
  Returns:
    N/A
    """
  print(hm_module.HANGMAN_PICS[len(missed_letters)])
  print()

  print('Missed letters:', end=' ')
  for letter in missed_letters:
    print(letter, end=' ')
  print()

  blanks = '_' * len(secret_word)

  for i in range(len(secret_word)): # Replace blanks with correctly guessed letters.
    if secret_word[i] in correct_letters:
      blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
  
  for letter in blanks: # Show the secret word with spaces in between each letter.
    print(letter, end=' ')
  print()
 
print('H A N G M A N')
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(hm_module.words)


def get_guess(already_guessed):
  """Returns the letter the player entered. This function makes sure the player
  entered a single letter and not something else."""
  while True:
    print('Guess a letter.')
    guess = input()
    guess = guess.lower()
    if len(guess) != 1:
      print('Please enter a single letter.')
    elif guess in already_guessed:
      print("You have already guessed that letter. Choose again.")
    elif guess not in "abcdefghijklmnopqrstuvwxyz":
      print("Please enter a LETTER.")
    else:
      return guess
