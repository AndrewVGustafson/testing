from functions import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


OPENER = "slant"
BETTER_GUESS_CUTOFF = 3
GUESSING_INTERVAL = 1.45


driver = webdriver.Chrome(options=Options().add_argument('--log-level=3'))
URL = 'https://speedle.rahuljk.com/'
driver.get(URL)
driver.execute_script("window.onbeforeunload = function() {};")
actions = ActionChains(driver)

start_button_id = "startButton"
play_again_button_id = "playAgainButton"
guess_grid_id = "guess-grid"




while True:
    words = get_dict_data()
    purged_words = words

    start_button = driver.find_element(By.ID, start_button_id)
    play_again_button = driver.find_element(By.ID, play_again_button_id)

    click_available_element(start_button, start_button_id, driver)

    guess = OPENER
    for i in range(6):
        if play_again_button.is_displayed():
            break
        
        print(f"Guess: {guess}\nWords Remaining: {len(purged_words)}\n")

        send_word(guess, actions)
        sleep(GUESSING_INTERVAL)
        
        tile_data = get_tiles_data(driver)
        purged_words = filter_words(tile_data, purged_words)
        if i <= BETTER_GUESS_CUTOFF:
            guess = better_guess(purged_words)
        else:
            guess = purged_words[0]

        if purged_words == 1:
            break

    click_available_element(play_again_button, play_again_button_id, driver)

