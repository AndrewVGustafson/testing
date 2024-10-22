from utils import get_from_file, purge

class ManualSolver():
    def __init__(self):
        self.words = get_from_file.get_dict_data()
        self.purged_words = self.words

    def run_solver(self):
        while True:
            self.do_selection()

    def get_selection(self) -> str:
        return input("Select an option:\n[W] Wrong letters, [L] Wrong Location Letters, [C] Correct Letters [G] Get Available Words [GG] Get Optimized Guess Words [E] End Game [N] New Game [S] Save/Load Options\n\n").lower()

    def do_selection(self):
        match self.get_selection():
            case 'w':
                wrong_letters = self.get_wrong()
                purged_words = purge.purge_wrong(wrong_letters, purged_words)

            case 'l':
                wrong_location_letters = self.get_wrong_location()
                print(wrong_location_letters)
                purged_words = purge.purge_wrong_location(wrong_location_letters, purged_words)

            case 'c':
                correct_letters = self.get_correct()
                purged_words = purge.purge_correct(correct_letters, purged_words)
            
            case 'g':
                print("Please choose from one of the following words:")
                print(*purged_words, "\n")

            case 'gg':
                print("Please choose from one of the following words:")
                optimized_words = purge.better_guesses(purged_words)
                print(*optimized_words, "\n")

            case 'e':
                print("Bye bye.")
                exit()

            case 'n':
                print("Resetting words...\n")
                purged_words = self.words

            case _:
                print("Enter from one of the options...\n")
                return            
            
    def save_load(self):
        selection = input("[S] Save Current Game [L] Load Last Played Game [LF] Load Game from File [R] Return to Game\n\n").lower()
        match selection:
            case "s":
                pass


    def get_wrong(self) -> list[str]:
        wrong_letters = input("\nEnter each incorrect letter, not seperated by a space:  ie. 'xyz'\n")
        wrong_letters = list(wrong_letters)
        return wrong_letters

    def get_wrong_location(self) -> list[tuple[str, int]]:
        wrong_location_letters = input("\nEnter each letter and the position it's not in, seperated by a space: ie. 'a1 b2 c3'\n")
        wrong_location_letters = wrong_location_letters.split(" ")
        wrong_location_letters = [(letter[0], int(letter[1]) - 1) for letter in wrong_location_letters]
        return wrong_location_letters

    def get_correct(self) -> list[tuple[str, int]]:
        correct_letters = input("\nEnter each letter and the position it's in, seperated by a space: ie. 'a1 b2 c3'\n")
        correct_letters = correct_letters.split(" ")
        correct_letters = [(letter[0], int(letter[1]) - 1) for letter in correct_letters]
        return correct_letters


if __name__ == "__main__":
    solver = ManualSolver()
    solver.run_solver()