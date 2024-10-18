import json
from typing import Any

from pathlib import Path
PROJECT_DIR = Path(__file__).parent
DICT_FILE_PATH = PROJECT_DIR / 'dictionary.json'
JS_FILE_PATH = PROJECT_DIR / 'alter_sources.js'


def get_dict_data() -> list:
    with open(DICT_FILE_PATH, "r") as file:
        words: list = json.load(file)
        words = words["dictionary"]
    return words

def get_js_commands() -> str:
    with open(JS_FILE_PATH, "r") as file:
        return file.read()

def x_wrong(letters: list, words: list) -> list:
    letters = list(set(letters))
    purged_words = words
    for letter in letters:
        purged_words = [word for word in purged_words if letter not in word]
    return purged_words

def x_wrong_location(blocks: dict, words: list) -> list:
    purged_words = words
    for letter, position in blocks:
        purged_words = [word for word in purged_words if letter in word and letter not in word[position]]
    return purged_words

def x_correct(blocks: dict, words: list) -> list:
    purged_words = words
    for letter, position in blocks:
        purged_words = [word for word in purged_words if letter in word and letter in word[position]]
    return purged_words


def get_wrong() -> list[str]:
    wrong_letters = input("\nEnter each incorrect letter, not seperated by a space:  ie. 'xyz'\n")
    wrong_letters = list(wrong_letters)
    return wrong_letters

def get_wrong_location() -> list[tuple[str, int]]:
    wrong_location_letters = input("\nEnter each letter and the position it's not in, seperated by a space: ie. 'a1 b2 c3'\n")
    wrong_location_letters = wrong_location_letters.split(" ")
    wrong_location_letters = [(letter[0], int(letter[1]) - 1) for letter in wrong_location_letters]
    return wrong_location_letters

def get_correct() -> list[tuple[str, int]]:
    correct_letters = input("\nEnter each letter and the position it's in, seperated by a space: ie. 'a1 b2 c3'\n")
    correct_letters = correct_letters.split(" ")
    correct_letters = [(letter[0], int(letter[1]) - 1) for letter in correct_letters]
    return correct_letters


def filter_words(tiles_data: dict[str, Any], words: list) -> list:
    purged_words = words
    for data_state, values in tiles_data.items():
        if data_state == "wrong":
            purged_words = x_wrong(values, purged_words)
            
        if data_state == "wrong-location":
            purged_words = x_wrong_location(values, purged_words)

        if data_state == "correct":
            purged_words = x_correct(values, purged_words)

        else:
            continue
    return purged_words

def better_guess(words: list) -> str:
    better_words = []
    for word in words:
        if len(list(set(word))) == 5:
            better_words.append(word)
    
    if better_words != []:
        return better_words[0]
    else:
        return words[0]
    
def better_guesses(words: list) -> str:
    better_words = []
    for word in words:
        if len(list(set(word))) == 5:
            better_words.append(word)
    
    if better_words != []:
        return better_words
    else:
        return words