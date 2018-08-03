import sys
import clipboard
import pyautogui
import time


input_to_copy = ""
num = 0
same_or_next = ""
text=""
time_till_spam=0

def input_For_Copying():
    global input_to_copy, num,same_or_next
    go_no_go=''
    input_to_copy = input("Input text to copy with spaces : ")
    num = int(input("Number of times to copy : "))
    if num >= 999999:
        print("Warning!!! \nYou can FILL / KILL your dive if the number is to high!!!\n")
        go_no_go = input("Umm so that's a lot.... are you sure? \n[Y]es / [N]o : ")
        if go_no_go in ('y'):
            pass
        elif go_no_go in ('n'):
            input_For_Copying()
    else:

        same_or_next = input("[S]ame line or [N]ext line : ")

def loopy():
    global num, input_to_copy, same_or_next, open_file
    for loop in range(num):
        if same_or_next in ("s"):
            #printy_same_line()    #  Debug
            open_file.write(input_to_copy)

        elif same_or_next in ("n"):
            # printy_next_line()    #  Debug
            new_line_copy = input_to_copy + "\n"
            open_file.write(new_line_copy)

################ Debug ###################

def printy_same_line():
    print(input_to_copy, end='')
    sys.stdout.flush()

def printy_next_line():
    print(input_to_copy,"\n")

################ Debug -END-###################

def to_the_clip():
    global text
    open_file = open("copy_temp.txt", "r+")
    text= open_file.read()
    clipboard.copy(text)

def type_it():
    global text, time_till_spam
    my_interval = float(input("\nInput the interval at which to type each character [try 0.02] # : "))
    print("\n[TIMER STARTED!]")
    time.sleep(time_till_spam)
    pyautogui.typewrite(text, interval=my_interval)


def main():
    global open_file ,time_till_spam
    open_file = open("copy_temp.txt", "w+")
    input_For_Copying()
    loopy()
    open_file.close()
    to_the_clip()
    open_file.close()
    print("\nOk it's copied to your Clipboard AND Saved to copy_temp.txt")
    spam= input("\nDo you need it typed out? [Good for Spamming] \n[Y]es / [No] : ")
    if spam in ("y"):
        time_till_spam =float(input("\nNumber of sec till spamming starts? : "))
        type_it()

    else:
        print('Ok. Quitting...')

main()