from data import meals

def meal_dictionary(lst):
    meal_dict = {}
    for meal in lst:
        if meal[0] not in meal_dict.keys():
            meal_dict[meal[0]] = [meal[1:]]
            continue
        meal_dict[meal[0]] += [meal[1:]]
    return meal_dict