from data import games, genres

### Functions ###
def genre_dictionary(lst):
    genre_dict = {}
    for genre in lst:
        if genre[0] not in genre_dict.keys():
            genre_dict[genre[0]] = [genre]
        else:
            genre_dict[genre[0]] += [genre]
    return genre_dict

def game_dictionary(lst):
    game_dict = {}
    for game in lst:
        if game[0] not in game_dict.keys():
            game_dict[game[0]] = [game[1:]]
            continue
        game_dict[game[0]] += [game[1:]]
    return game_dict

def display(lst):
    for i in lst:
        print('\n')
        print(f'Title: {i[0]}')
        print(f'Review Score: {i[1]}')
        print(f'Dev: {i[-1]}')

### Global Values ###
game_shelf = game_dictionary(games)


def main():

    ### Genre Selection ###
    while True:
        genre_types = input(f"What would you like to play? \n \n{genre_dictionary(genres)} \n \n Enter first letter: ").strip().lower()
        try:
            genre_choices = genre_dictionary(genres)[genre_types]
        except KeyError as e:
            print(f"There is no input for {e}! ")
        else:
            break

    ### Subselection ###
    print(f"Your options are: ", end="")
    for i in range(len(genre_choices)):
        if i < len(genre_choices) - 1:
            print(genre_choices[i], end=", ")
            continue
        print("and " + genre_choices[i] + ".", end="\n")
    
    ### Confirmation of Choice ###
    genre_choice = input("What would you like to see? \n Enter Name: " ).strip().lower()
    while True:
        if genre_choice in genre_choices:
            confirmation = input(f"Are you sure you want to see {genre_choice} games? \n y/n: ".strip().lower())
            break
        else:
            genre_choice = input(f"Please choose {genre_choices[i]} \n Enter Name: " ).strip().lower()

    ### Game Selection ###
    while True:
        if confirmation == 'y':
            print(f"\n The selection of {genre_choice} games are: ")
            display(game_shelf[genre_choice])
            while True:
                search = input(" Would to keep looking? \n y/n: " )
                if search == "y":
                    main()
                elif search == "n":
                    print("\n Good Bye!")
                    quit()
                    

        elif confirmation == 'n':
            main()

        else:
            print("Please enter y/n ")
            confirmation = input(f"Are you sure you want to see {genre_choice} games? \n y/n: ".strip().lower())


    
   


### TESTING ###
main()
#print(meat_dictionary(meat))
#print(meal_dictionary(meat))