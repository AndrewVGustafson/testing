# from wordle.functions import *
from functions import *
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

class AutoSolver():
    def __init__(self, driver: webdriver.Chrome, URL) -> None:
        
        self.driver = driver
        # self.driver.execute_cdp_cmd('Debugger.enable', {})
        # self.driver.execute_cdp_cmd('Debugger.setBreakpointByUrl', {'lineNumber': 95, 'url':'https://speedle.rahuljk.com/script.js'})
        # self.driver.execute_script(get_js_commands())
        self.driver.get(URL)
        # driver.execute_cdp_cmd('Debugger.disable', {})
        # self.driver.execute_script("window.onbeforeunload = function() {};")
        self.actions = ActionChains(self.driver)

        self.words = get_dict_data()
        self.purged_words = self.words
        self.start_button_id = "startButton"
        self.play_again_button_id = "playAgainButton"
        self.guess_grid_id = "guess-grid"


    def get_starting_words(self, starting_words: list):
        while len(starting_words) < 6:
            starting_words.append(None)
        return starting_words

    def solve(self, replay_forever: bool = False, guessing_interval: float = 1.45, starting_words: list = ["tales"]) -> None:

        self.starting_words = self.get_starting_words(starting_words)
        self.purged_words = self.words

        self.start_button = self.driver.find_element(By.ID, self.start_button_id)
        self.play_again_button = self.driver.find_element(By.ID, self.play_again_button_id)

        self.click_available_element(self.start_button, self.start_button_id)

        for i in range(6):
            if starting_words[i]: self.guess = starting_words[i]

            if self.play_again_button.is_displayed():
                break
            
            print(f"Guess: {self.guess}, Words Remaining: {len(self.purged_words)}\n")

            self.send_word(self.guess)
            sleep(guessing_interval)
            self.guess = self.get_guess(i)

            if self.purged_words == 1:
                break

        if replay_forever:
            self.click_available_element(self.play_again_button, self.play_again_button_id)
            self.solve(replay_forever=True, guessing_interval=guessing_interval, starting_words=starting_words)


    def get_guess(self, row: int) -> str:
        tile_data = self.get_tiles_data()
        self.purged_words = filter_words(tile_data, self.purged_words)
        if row <= BETTER_GUESS_CUTOFF:
            return better_guess(self.purged_words)
        else:
            return self.purged_words[0]

    def send_word(self, guess: str) -> None:
        self.actions.send_keys(guess + Keys.ENTER)
        self.actions.perform()

    def click_available_element(self, element: WebElement, element_id: str) -> None:
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, element_id))
        )
        element.click()

    def get_tiles_data(self) -> dict[str, Any]:
        tile_elements = self.driver.find_elements(By.CLASS_NAME, "tile")

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

if __name__ == "__main__":
    # STARTING_WORDS = ["cones", "trial"]
    STARTING_WORDS = ["slant"]
    BETTER_GUESS_CUTOFF = 3
    GUESSING_INTERVAL = 1.45

    driver = webdriver.Chrome(options=Options().add_argument('--log-level=3'))
    # options.enable_bidi = True
    URL = 'https://speedle.rahuljk.com/'

    auto_solver = AutoSolver(driver, URL)
    auto_solver.solve(starting_words=STARTING_WORDS, replay_forever=True)
