#!/usr/bin/env python3
import os
import pyautogui
import clipboard
import time
from ast import literal_eval

dict_of_info = {}
text_repeated = ''


def loopy():
    global dict_of_info, text_repeated
    text_repeated = dict_of_info['text']
    temp = dict_of_info['text']
    num = dict_of_info['times_to_repeat'] - 1  # -1 because of original

    for the_loop in range(num):

        if dict_of_info['same_or_next'] in 's':
            text_repeated += temp
            #  print(dict_of_info['times_to_repeat'])

        elif dict_of_info['same_or_next'] in 'n':
            text_repeated += "\n"
            text_repeated += temp   # see if this can be cleaned up


######################################
def do_next():
    do_this_next = input('[M]enu or [Q]uit : ')
    if do_this_next in ('m', ''):
        main()
    elif do_this_next in 'q':
        quit()
    else:
        quit()


######################################
def clipboard_mode():
    os.system("clear")
    print('Clipboard Mode'.center(50, '_'), '\n')
    global dict_of_info, text_repeated
    loopy()
    clipboard.copy(text_repeated)
    print('Copied')
    do_next()


def file_mode():
    global dict_of_info, text_repeated
    os.system("clear")
    print('File Mode'.center(50, '_'), '\n')
    loopy()
    file_name = input('Input a File Name with the file ext ie [file.txt] : ')
    try:
        open_file = open(file_name, "w+")
        open_file.write(text_repeated)
        open_file.close()
        print('Saved to ', file_name)
        do_next()
    except FileNotFoundError as e:
        print(e)
        print('You need to type a file name there...')
        time.sleep(2)
        what_do_want_to_do()


def save_mode():
    global dict_of_info, text_repeated
    os.system("clear")
    print('Saving'.center(50, '_'), '\n')
    open_config_file = open("config.txt", "a")
    open_config_file.write(str(dict_of_info) + "\n")
    open_config_file.close()
    print('Saved!')
    do_next()


def spam_mode():
    os.system("clear")
    global dict_of_info, text_repeated
    print('SPAM MODE! Menu'.center(50, '_'), '\n')
    print('First let me get some info')
    my_interval = float(input("\nInput the interval at which to type each character [try 0.02] # : "))
    delay = float(input("\nInput a delay between pastes [0 for no delay] : "))
    time_till_spam = float(input("\nNumber of sec till spamming starts? : "))
    print('Key'.center(50, '_'), '\n')
    print(f"[R]epeated = [Your text] Repeated {dict_of_info['times_to_repeat']} times\n")
    print(f"[S]pam = Repeated * # you will input\n")
    print('End of Key'.center(50, '_'), '\n')
    spam_or_repeat = input('Would you like to use [R]epeated or [S]pam \n')

    if spam_or_repeat in 'r':
        os.system("clear")
        print('SPAM MODE! Menu'.center(50, '_'), '\n')
        print(f"[Your text] will be repeated {dict_of_info['times_to_repeat']} times\n")
        print("A Return Character will be played a the End of [Your Text Repeated] as a 'Send' \n")
        loopy()

        def repeat_loop():
            go_on = input("press [Enter] to Start : ")  # dumpy input var to just wait for input find better way
            print("\n[TIMER STARTED!]")
            time.sleep(time_till_spam)

            if dict_of_info['same_or_next'] in 's':
                pyautogui.typewrite(text_repeated, interval=my_interval)
                time.sleep(delay)
                pyautogui.press('enter')

            elif dict_of_info['same_or_next'] in 'n':
                for loop in range(dict_of_info['times_to_repeat']):
                    pyautogui.typewrite(dict_of_info['text'], interval=my_interval)
                    pyautogui.press('enter')
                    time.sleep(delay)
            run_again = input('Run it Again?    [Enter]     [Q]uit      [M]enu : ')
            if run_again in ("", 'y'):
                repeat_loop()
            elif run_again in "q":
                print('Bye!')
                quit()
            elif run_again in 'm':
                what_do_want_to_do()

        repeat_loop()

    elif spam_or_repeat in 's':
        os.system("clear")
        print('SPAM MODE! Menu'.center(50, '_'), '\n')
        print(f"OK! [Your Text Repeated]{dict_of_info['times_to_repeat']} times should be spammed how many time?")
        loopy()
        print("A Return Character will be played a the END of [Your Text Repeated] as a 'Send' \n")
        times_to_spam = int(input("Times to be Spammed : "))

        def spam_loop():
            go_on = input("press [Enter] to Start : ")
            print("\n[TIMER STARTED!]")
            time.sleep(time_till_spam)
            for loop in range(times_to_spam):
                pyautogui.typewrite(text_repeated, interval=my_interval)
                pyautogui.press('enter')
                time.sleep(delay)
            run_again = input('Run it Again?    [Enter]     [Q]uit      [M]enu : ')
            if run_again in ("", 'y'):
                spam_loop()
            elif run_again in "q":
                print('Bye!')
                quit()
            elif run_again in 'm':
                what_do_want_to_do()

        spam_loop()


def print_here():
    global dict_of_info, text_repeated
    os.system("clear")
    print('Print Here'.center(50, '_'), '\n')
    loopy()
    print(text_repeated)
    do_next()


######################################
def what_do_want_to_do():
    global dict_of_info
    os.system("clear")
    print('What Do You Want to Do'.center(50, '_'), '\n')
    print(f"OK I'll Repeat that {dict_of_info['times_to_repeat']} Times \n")
    print('How to Output it')
    print('1. [C]lipboard')
    print('2. [F]ile.txt')
    print('3. [S]ave For Later')
    print('4. [J]ust SPAM IT!')
    print('5. [P]rint Here...')
    print('6. [M]ain Menu ')
    output_choice = input('Your Output Choice : ')

    if output_choice in ('1', 'c'):
        clipboard_mode()
    elif output_choice in ('2', 'f'):
        file_mode()
    elif output_choice in ('3', 's'):
        save_mode()
    elif output_choice in ('4', 'j'):
        spam_mode()
    elif output_choice in ('5', 'p'):
        print_here()
    elif output_choice in ('6', 'm'):
        main()


def add_text():
    global dict_of_info
    os.system("clear")
    print('Input Some Text to Repeat'.center(50, '_'), '\n')
    text = input('Input some text : ')
    times_to_repeat = int(input('How Many Times Do You Want That Repeated : '))
    same_or_next = input('Repeat on [S]ame or [N]ext Line : ')
    dict_of_info['text'] = text
    dict_of_info['times_to_repeat'] = times_to_repeat
    dict_of_info['same_or_next'] = same_or_next
    print(dict_of_info)
    what_do_want_to_do()


def view_saved():
    global dict_of_info
    os.system("clear")
    print('View Saved'.center(50, '_'), '\n')
    try:
        open_read_config_file = open("config.txt", "r")
        for index, line in enumerate(open_read_config_file, start=1):
            print(index, line)
        print()
        my_saved_config_choice = input("Press [Enter] to return to main menu or pick a [#] to use : ")
        # print(type(my_saved_config_choice))
        try:
            if my_saved_config_choice in '':
                main()
            else:
                try:
                    my_saved_config_choice = int(my_saved_config_choice)
                    # print(type(my_saved_config_choice))
                except ValueError as e:
                    print('!!!ERROR!!!', e)
                    print("So That's NOT a Number")
                    time.sleep(2)
                    view_saved()
            open_read_config_file = open("config.txt", "r")
            print('You want #', my_saved_config_choice)
            my_saved_config_choice -= 1
            lines = open_read_config_file.readlines()
            # print(lines)
            open_read_config_file.close()
            print(lines[my_saved_config_choice])
            use_me = lines[my_saved_config_choice]

            dict_of_info = literal_eval(use_me)
            what_do_want_to_do()
        except IndexError as e:
            print('!!!ERROR!!!', e)
            print('That Number Dose NOT Exist')
            do_next()

    except FileNotFoundError as e:
        print(e, '\nYou do have a config.txt yet.... Ill make one for you... ')
        config_file = open('config.txt', "w+")
        print('Ok its made but its empty because the file got deleted or was never there.\n')
        do_next()


def resume():
    global dict_of_info
    if not bool(dict_of_info):
        print('Nothing to Resume')
        time.sleep(2)
        main()

    else:
        what_do_want_to_do()


def main():
    os.system("clear")
    print('Main Menu'.center(50, '_'), '\n')
    print('1.[A]dd Some Text to Repeat')
    print('2.[V]iew or Use Saved')
    print('3.[R]esume')
    print('4.[Q]uit')
    main_input = input('Input : ')
    if main_input in ('1', 'a'):
        add_text()
    elif main_input in ('2', 'v'):
        view_saved()
    elif main_input in ('3', 'r'):
        resume()
    elif main_input in ('4', 'q'):
        quit()
    else:
        main()

main()
