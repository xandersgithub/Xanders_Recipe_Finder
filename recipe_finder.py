from bs4.element import ResultSet
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os 

# Launches chrome and fetches input paths
web = webdriver.Chrome()
web.get('https://www.google.com')

input_ingredients = web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_button = web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
lucky_search_button = web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]')

# os.system('cls' if os.name == 'nt' else 'clear')
# os.system()

var_counter = 0
reset_var_counter = var_counter - var_counter
list_of_added_ingredients = ['\"recipe\" ','recipes including ']

print('Hello, this program will fetch you some recipes bubba')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_ingredients(user_done_adding_ingredients):
    clear()
    while user_done_adding_ingredients == True:
        ingredient = input('Please enter the ingredient you wish to add: \n*** If you want to stop adding ingredients just type "done"\n').lower()
        if ingredient == "done":
            user_done_adding_ingredients = False
            determine_loop('9987')
        else:
            list_of_added_ingredients.append('"{}", '.format(ingredient))

def print_list_delete():
    clear()
    range_o = range(0,len(list_of_added_ingredients)-2)
    which_to_remove = zip(range_o, list_of_added_ingredients[2:])
    print(list(which_to_remove))

# need to add a quick delete mode to delete multiple ingredients in one command. will use formatting commands
def delete_ingredients(user_ready_to_remove_ingredients):
    donzo = ''
    clear()
    print('')
    print(list_of_added_ingredients[2:])
    while user_ready_to_remove_ingredients == True:
        print('')
        delete_mode = input('To delete an item press [1] \nTo exit delete mode press [2]\n').lower()

        if delete_mode == '1':
            print_list_delete()
            print('')
            ingredient_to_remove_pre_int = input('Which item would you like to remove? [#]: \n')
            ingredient_to_remove = int(ingredient_to_remove_pre_int)
            list_of_added_ingredients.pop(ingredient_to_remove + 2)
        elif delete_mode == '2':
            user_ready_to_remove_ingredients = False
            clear()
            whats_next = input('If you would you like to add ingredients press [0] \nTo delete ingredients press [1] \nTo view your ingredients press [2] \nTo search for recipes with the added ingredients? [3], or [4] If you\'re feeling lucky\n')
            determine_loop(whats_next)
        else:
            print('input not recognized')
    
def view_added_ingredients():
    clear()
    print(list_of_added_ingredients[2:])
    input('Press any button to continue.\n')
    newloop()

def search_for_recipes():
    input_ingredients.send_keys(list_of_added_ingredients)
    search_button.click()

def lucky_search_for_recipes():
    input_ingredients.send_keys(list_of_added_ingredients)
    lucky_search_button.click()

def newloop():
    clear()
    new_tor = input('If you would you like to add ingredients press [0] \nTo delete ingredients press [1] \nTo view your ingredients press [2] \nTo search for recipes with the added ingredients? [3], or [4] If you\'re feeling lucky\n')
    determine_loop(new_tor)

def determine_loop(tor):
    clear()
    if tor == "0":
        add_ingredients(True)
    elif tor == "1":
        if len(list_of_added_ingredients) >= 3:
            delete_ingredients(True)
        print('You gots to add some ingredients first to delete them pardner!')
        add_ingredients(True)
    elif tor == "2":
        if len(list_of_added_ingredients) >= 3:
            view_added_ingredients()
        else:
            print('You gots to add some ingredients pardner!')
            add_ingredients(True)
    elif tor == "3":
        if len(list_of_added_ingredients) >= 3:
            search_for_recipes()
            # os.system('exit')
        else:
            print('You gots to add some ingredients pardner!')
            add_ingredients(True)
    elif tor == "4":
        if len(list_of_added_ingredients) >= 3:
            lucky_search_for_recipes()
            # os.system('exit')
        else:
            print('You gots to add some ingredients pardner!')
            add_ingredients(True)
    elif tor == '9987':
        newloop()
    else:
        print('I got no clue what you just said pardner, go ahead and add some ingredients')
        add_ingredients(True)

# this is the entire program, it relies on functions. 
old_tor = input('If you would you like to add ingredients press [0] \nTo delete ingredients press [1] \nTo view your ingredients press [2] \nTo search for recipes with the added ingredients? [3], or [4] If you\'re feeling lucky\n')
determine_loop(old_tor)