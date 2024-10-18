from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from wordle.auto import AutoSolver


if __name__ == "__main__":
    # STARTING_WORDS = ["cones", "trial"]
    STARTING_WORDS = ["slant"]
    BETTER_GUESS_CUTOFF = 3
    GUESSING_INTERVAL = 1.45
    options = Options()
    options.add_argument('--log-level=3')
    options.enable_bidi = True

    driver = webdriver.Chrome(options=options)
    URL = 'https://speedle.rahuljk.com/'
    
    auto_solver = AutoSolver(driver, URL)
    auto_solver.solve(starting_words=STARTING_WORDS, replay_forever=True)
