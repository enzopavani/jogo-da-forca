import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["violeta", "vermelho", "laranja", "rosa", "amarelo"]
letter_list = []
chosen_word = random.choice(word_list)
lives = 6
# print(f"Palavra secreta: {chosen_word}")
word_lenght = len(chosen_word)

display = []
for letter in chosen_word:
    display.append("_")
print(f"{' '.join(display)}\n")

game_end = False
while not game_end:
    guess = input("Adivinhe uma letra: ").lower()
    if guess in letter_list:
        print("Letra ja adivinhada. Tente novamente.")
    else:
        letter_list.append(guess)
        for position in range(word_lenght):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        if guess not in chosen_word:
            lives -= 1
        print(f"{' '.join(display)}")
        print(f"Vidas: {lives}\n\n\n")
        stage = 6 - lives
        print(HANGMANPICS[stage])

        if "_" not in display:
            game_end = True
            print(f"Você ganhou. A palavra secreta era: \"{chosen_word}\".")
        if lives == 0:
            game_end = True
            print(f"Você perdeu. A palavra secreta era: \"{chosen_word}\".")

