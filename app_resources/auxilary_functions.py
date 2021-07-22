import json, os, sys
import re,os,shutil,tkinter
from datetime import datetime
from tkinter import filedialog, Tk, messagebox
import traceback

def author_information():
    '''
    This provides information about the author and the program.
    '''
    text="app_resources/app_docs/author_information.json"
    with open(text,mode="r",encoding="utf-8") as file:
        data=json.load(file)
        for line in data:
            print(line,data[line])
        input("Press enter to continue")

def program_description():
    text = "app_resources/app_docs/program_description.txt"
    with open(text,mode="r",encoding="utf-8") as file:
        for line in file:
            print(line)
        input("Press enter to continue")

def file_finder():
    '''
    This initiates a filedialog that is allows the user to dynamically select a file.
    '''

    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    filename = filedialog.askopenfilename()
    root.withdraw()
    print("Please wait while your file is being loaded. Larger files might require more time. ")

    return filename

def menu(output_menu, menu_name, menu_information):
    '''
    This is a variation of the main menu that is found in the main app.
    '''

    invalid_option = f'An error occurred. You can return to {menu_name} by pressing enter.'

    while True:
        print(f'\n\t\t~ {menu_name} ~\n')
        print(f'{menu_information}\n')

        for num, elem in enumerate(output_menu, start=1):
            print(f'{num}: {elem}')

        choice_str = input("\nPlease enter the menu number:")

        menu_option = output_menu.get(choice_str.title())

        if menu_option:
            break
        else:
            try:
                choice_num = int(choice_str)
            except:
                input(invalid_option)
                with open("app_resources/app_docs/error.log", mode="a") as log:
                    log.write(traceback.format_exc())
            else:
                if 0 < choice_num and choice_num <= len(output_menu):
                    func_list = list(output_menu.values())
                    function_number = choice_num - 1
                    options_func_dict = func_list[function_number]
                    break
                else:
                    input(invalid_option)
    try:
        return options_func_dict()

    except:
        with open("app_resources/app_docs/error.log", mode="a") as log:
            log.write(traceback.format_exc())
        return options_func_dict

def clear_log():
    pass