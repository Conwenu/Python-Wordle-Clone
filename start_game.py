from typing import List
from letter import LetterModel
from game_handler import Wordle
from colorama import Fore
import random


def main():
    word_data_set = get_word_data_set("WordDataSet.txt")
    secret = random.choice(list(word_data_set))
    wordle = Wordle(secret)

    while wordle.can_try_again:
        x = input("\nType Guess: ")
        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f"Word must be {wordle.WORD_LENGTH} characters long" + Fore.RESET)
            continue
        if not x.upper() in word_data_set:
            print(Fore.RED + f"{x} is not a valid word" + Fore.BLUE + " Please note that this program does not have a "
                                                                      "large word bank" + Fore.RESET)
            continue
        wordle.attempt(x)
        show_results(wordle)
    if wordle.is_solved:
        if wordle.attempts_left == 0:
            print(Fore.GREEN + "Phew! That was close, you've guessed the correctWord" + Fore.RESET)
        elif wordle.attempts_left == 5:
            print(Fore.GREEN + "We've got a genius here. You;ve guessed the correct word on your first try!" + Fore.RESET)
        else:
            print(Fore.GREEN + f"Congrats! You've guessed the correct word with {wordle.attempts_left} attempts left!" + Fore.RESET)
    else:
        print(Fore.RED + f"Failed. The Correct Answer Was {wordle.secret}" + Fore.RESET)


def show_results(wordle: Wordle):
    print(f"You have {wordle.attempts_left} attempts remaining")
    for word in wordle.attempts:
        result = wordle.guess(word)
        coloredResultString = conv_to_color(result)
        print(coloredResultString)
    for _ in range(wordle.attempts_left):
        print(Fore.CYAN + "- - - - -" + Fore.RESET)


def conv_to_color(result: List[LetterModel]):
    resultWithColor = []
    for letter in result:
        if letter.validPosition:
            color = Fore.GREEN
        elif letter.validCharacter:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        coloredLetter = color + letter.character + Fore.RESET
        resultWithColor.append(coloredLetter)
    return " ".join(resultWithColor)


def get_word_data_set(file: str):
    wordDataSet = set()
    with open(file, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            wordDataSet.add(word)
    return wordDataSet


if __name__ == "__main__":
    main()
