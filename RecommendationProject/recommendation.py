from data import games, genres

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

game_shelf = game_dictionary(games)

def main():
    # Game selection
    while True:
        genre_types = input("What would you like to play? \nEnter first letter: ").strip().lower()
        
        try:
            genre_choices = genre_dictionary(genres)[genre_types]
        except KeyError as e:
            print(f"There is no input for {e}! ")
        else:
            break

    print(f"Your options are ", end="")
    for i in range(len(genre_choices)):
        if i < len(genre_choices) - 1:
            print(genre_choices[i], end=", ")
            continue
        print("and " + genre_choices[i] + ".", end="\n")
    
    genre_choice = input("Which one \n Enter Name: " ).strip().lower()
    while True:
        if genre_choice in genre_choices:
            confirmation = input(f"Do you want to see {genre_types} games? \n y/n: ".strip().lower())
            break
        else:
            print("No such option available.")
        genre_choice = input("Which one do you want? \n Enter Name: " ).strip().lower()
        

    
   


### TESTING ###
main()
#print(meat_dictionary(meat))
#print(meal_dictionary(meat))