import random

destination_list = ['France', 'Paris', 'Bora Bora', 'Hawaii', 'Europe']
restaurant_list = ['Goumard', 'Buffalo Grill', "Island Lava Java", "Bloody Mary's"]
transportation_list = ['Train', 'Car', 'Motorcycle', "Plane"]
entertainment_list = ['Zoo', 'Movie', 'Miniature golf', "Amusment Park"]


def greet_and_get_user_input():
    print("Greetings and welcome to the Day Trip Generator")
    destination = provide_random_item_from_list(destination_list)
    destination_chosen = get_user_input(destination_list, destination, 'destination')
    transportation = provide_random_item_from_list(transportation_list)
    transportation_chosen = get_user_input(transportation_list, transportation, 'transportation')
    restaurant = provide_random_item_from_list(restaurant_list)
    restaurant_chosen = get_user_input(restaurant_list, restaurant, 'restaurant')
    entertainment = provide_random_item_from_list(entertainment_list)
    entertainment_chosen = get_user_input(entertainment_list, entertainment, 'entertainment')

    choices_object = {
        'destination': destination_chosen,
        'transportation': transportation_chosen,
        'restaurant': restaurant_chosen,
        'entertainment': entertainment_chosen
    }

    finalize_transaction(choices_object)

def provide_random_item_from_list(selected_list, previous_element=''):
    print('#####',previous_element)
    index = random.randrange(0, len(selected_list))
    new_element = selected_list[index]
    while previous_element == new_element:
         index = random.randrange(0, len(selected_list))
         new_element = selected_list[index]
    return new_element


def get_user_input(list_to_choose_from, selection_from_list, type_of_selection, alt_message_bool=False):

    if alt_message_bool == False:
        user_input = input(
            f'We have picked {selection_from_list} for your {type_of_selection}! Do you like this option? y/n: ')
    if alt_message_bool == False:
        if user_input == 'y':
            return selection_from_list
        else:
            new_selection_from_list = provide_random_item_from_list(
                list_to_choose_from, selection_from_list)
            return get_user_input(list_to_choose_from, new_selection_from_list, type_of_selection, True)
    if alt_message_bool == True:
        new_selection_from_list = provide_random_item_from_list(
            list_to_choose_from, selection_from_list)
        user_input = input(
            f'Oh sorry, no problem {type_of_selection}. Lets try something else {new_selection_from_list}? Do you like this option? y/n: ')
    if alt_message_bool == True:
        if user_input == 'y':
            return new_selection_from_list
        else:
            new_selection_from_list = provide_random_item_from_list(
                list_to_choose_from, new_selection_from_list)
            return get_user_input(list_to_choose_from, new_selection_from_list, type_of_selection, True)


def finalize_transaction(choices_obj):
    new_line = '\n'

    destination_chosen = choices_obj['destination']
    transportation_chosen = choices_obj['transportation']
    restaurant_chosen = choices_obj['restaurant']
    entertainment_chosen = choices_obj['entertainment']

    print(
        f'Great! Lets move to the next step!{new_line}Congrats! We have completed you trip. Now lets confirm everything.')
    print(
        f'The trip we have made for you is:{new_line}Destination: {destination_chosen}')
    print(f'Transportation: {transportation_chosen}')
    print(f'Restaurant: {restaurant_chosen}')
    print(f'Entertainment: {entertainment_chosen}')
    finalize = input(f'Are you happy with these options? y/n: ')
    if finalize == 'y':
        handle_final_message(choices_obj)
    else:
        handle_modify_booking(choices_obj)


def handle_modify_booking(choices_obj):
    new_line = '\n'
    print(
        f'no problen, what would you like to change? {new_line} a: destination {new_line} b: transportation {new_line} c: entertainment {new_line} d: restaurant {new_line}')
    user_input = input('Please provide answer here ( a b c OR d ):  ')
    if user_input == 'a':
        destination_chosen = get_user_input(destination_list, choices_obj['destination'], 'destination', True)
        choices_obj['destination'] = destination_chosen
        return finalize_transaction(choices_obj)
    elif user_input == 'b':
        transportation_chosen = get_user_input(transportation_list, choices_obj['transportation'], 'transportation', True)
        choices_obj['transportation'] = transportation_chosen
        finalize_transaction(choices_obj)
    elif user_input == 'c':
        entertainment_chosen = get_user_input(entertainment_list, choices_obj['entertainment'], 'entertainment', True)
        choices_obj['entertainment'] = entertainment_chosen
        finalize_transaction(choices_obj)
    elif user_input == 'd':
        restuarant_chosen = get_user_input(restaurant_list, choices_obj['restaurant'], 'restaurant', True)
        choices_obj['restaurant'] = restuarant_chosen
        finalize_transaction(choices_obj)


def handle_final_message(choices_obj):
    destination_chosen = choices_obj['destination']
    transportation_chosen = choices_obj['transportation']
    restaurant_chosen = choices_obj['restaurant']
    entertainment_chosen = choices_obj['entertainment']

    print(
        f'Get ready for an exciting trip we booked for you! You will be arriving to {destination_chosen} by {transportation_chosen} where you will spend the day checking out {entertainment_chosen}.')
    print(
        f'When you want to eat you will have directions to the {restaurant_chosen} we picked out for you.')
    print('Thank you for booking with us and enjoy your stay!')


greet_and_get_user_input()