from functions import *

words = get_dict_data()
purged_words = words
while True:
    selection = input("Select an option:\n[W] Wrong letters, [L] Wrong Location Letters, [C] Correct Letters [G] Get Available Words [E] End Game [N] New Game\n\n")
    match selection.lower():
        case "w":
            wrong_letters = get_wrong()
            purged_words = x_wrong(wrong_letters, purged_words)

        case "l":
            wrong_location_letters = get_wrong_location()
            print(wrong_location_letters)
            purged_words = x_wrong_location(wrong_location_letters, purged_words)

        case "c":
            correct_letters = get_correct()
            purged_words = x_correct(correct_letters, purged_words)
        
        case "g":
            print("Please choose from one of the following words:")
            print(*purged_words)

        case "e":
            print("Goodbye forever.")
            exit()

        case "n":
            print("Resetting words...\n")
            purged_words = words

        case _:
            print("Enter from one of the options, IDIOT\n")
            continue            
