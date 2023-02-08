import random

def pick_word():
    words = ["python", "java", "javascript", "ruby", "perl"]
    return random.choice(words)

def play_hangman():
    word = pick_word()
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()
    tries = 6

    print("Hangman Game")
    print("============")

    while len(word_letters) > 0 and tries > 0:
        print("You have {} tries left".format(tries))
        unused_letters = alphabet - used_letters
        print("Unused letters:", " ".join(sorted(list(unused_letters))))
        guess = input("Enter a letter: ").lower()
        if guess in used_letters:
            print("You already used that letter. Try again.")
        elif guess in word_letters:
            print("Good job! {} is in the word.".format(guess))
            word_letters.remove(guess)
        else:
            print("{} is not in the word.".format(guess))
            tries -= 1

        used_letters.add(guess)

    if tries == 0:
        print("You lost! The word was {}".format(word))
    else:
        print("Congratulations! You won! The word was {}".format(word))

if __name__ == "__main__":
    play_hangman()
