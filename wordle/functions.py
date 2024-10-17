import json
from typing import Any
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_dict_data() -> list:
    with open("dictionary.json", "r") as file:
        data: list = json.load(file)
        data = data["dictionary"]
    return data

def click_available_element(element, element_id, driver) -> None:
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, element_id))
    )
    element.click()


def x_wrong(letters: list, data: list) -> list:
    letters = list(set(letters))
    new_words = data
    for letter in letters:
        new_words = [word for word in new_words if letter not in word]
    return new_words

def x_wrong_location(blocks: dict, data: list) -> list:
    new_words = data
    for letter, position in blocks:
        new_words = [word for word in new_words if letter in word and letter not in word[position]]
    return new_words

def x_correct(blocks: dict, data) -> list:
    new_words = data
    for letter, position in blocks:
        new_words = [word for word in new_words if letter in word and letter in word[position]]
    return new_words


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


def get_tiles_data(driver) -> dict[str, Any]:
    tile_elements = driver.find_elements(By.CLASS_NAME, "tile")

    tiles_data = {
        "wrong": "",
        "wrong-location": [],
        "correct": []
    }

    for tile in tile_elements:
        letter = tile.text.lower()
        if not letter:
            continue

        data_state = tile.get_attribute("data-state")
        pos = tile_elements.index(tile) % 5
        block = (letter, pos)

        if data_state != "wrong":
            tiles_data[data_state].append(block)
        else:
            tiles_data["wrong"] += letter
    
    return tiles_data

def send_word(word: str, actions) -> None:
    actions.send_keys(word + Keys.ENTER)
    actions.perform()

def filter_words(tiles_data: dict[str, Any], words: list):
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
    