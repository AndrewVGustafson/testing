from functions import *
from selenium import webdriver 
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class AutoSolver():
    def __init__(self, driver: webdriver.Chrome, URL) -> None:
        
        self.driver = driver
        self.driver.get(URL)
        self.driver.execute_script("window.onbeforeunload = function() {};")
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

    def solve(self, should_replay: bool = False, guessing_interval: float = 1.45, starting_words: list = ["tales"]) -> None:

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

        if should_replay:
            self.click_available_element(self.play_again_button, self.play_again_button_id)


    def get_guess(self, row: int) -> str:
        tile_data = get_tiles_data(self.driver)
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

if __name__ == "__main__":
    # STARTING_WORDS = ["cones", "trial"]
    STARTING_WORDS = ["tales"]
    BETTER_GUESS_CUTOFF = 3
    GUESSING_INTERVAL = 1.45

    driver = webdriver.Chrome(options=Options().add_argument('--log-level=3'))
    URL = 'https://speedle.rahuljk.com/'

    auto_solver = AutoSolver(driver, URL)
    auto_solver.solve(should_replay=True)
