## PASTE_O_ MATIC v2

Simple Python3 "3.6" script for inputting text which you wish to repeat over and over.  
Various forms of output options.  
New line or Same line.  
Copy the text to your clipboard.  
Save to a file with a custom name.  
Save it for later.  
Printing it in the terminal.  
The ability to spam it.  


### Dependencies  

This is a simple script so there's no point in me making a install for it however the dependencies for the script are certainly worth installing.  

Latest Versions  

clipboard  
pyautgui  

# Main Menu

First you are greeted with this menu.  

    ____________________Main Menu_____________________ 
    1.[A]dd Some Text to Repeat
    2.[V]iew or Use Saved
    3.[R]esume
    4.[Q]uit
    Input : 

In this menu you can choose whether you want to...

#### Add some text to be repeated.  
This will then ask you for some text input and then ask you how many times he would like it to be repeated and then it will ask you whether you want the text to be repeated on the same line or the next line.  It will then send you to the  output options menu aka  (What do you want to do next menu) NOTE: Your text must include any spaces you want and cannot contain any new lines. You can experiment but I'm thinking ASCII art is not going to be supported unfortunately. You may also encounter problems with unicode.

#### View and or  use saved text  
This will take you to the view saved menu in which you can view text along with it's parameters that you have saved in the config file. This will give you the option to return to the main menu or choose a number from the list which he would like to load. Each saved item will show you the full python dictionary for the text and parameters that you have created.

#### Resume your session  
If there is a session to resume meaning there is a text and parameters loaded in memory this section will dump you straight into the output menu so you can choose what to do with it.

#### Quit - ends the script



## Output Menu ( "What do you want to do next" menu)

     ______________What Do You Want to Do______________ 

    OK I'll Repeat that 1 Times 

    How to Output it
    1. [C]lipboard
    2. [F]ile.txt
    3. [S]ave For Later
    4. [J]ust SPAM IT!
    5. [P]rint Here...
    6. [M]ain Menu 
    Your Output Choice : 

In this menu you will be given output options for your text.

#### Clipboard  
This will simply copy the repeated texts to your clipboard so that you can paste it in wherever you would like. It will then give you the option to quit or go to the main menu at which point you could choose to use resume to Output the text again in some manner as well as save it.

#### File.txt   
This will allow you to Output the repeated text to a custom named text file and give you the ability to go back to the main menu or quit.

#### Save for later  
Using safe for later you will be able to save the text and it's parameters for repeating to the config file.

#### Just Spam it  
Just Spam it offers you a variety of options for spamming the text. **Please see that section of the documentation**.

#### Print Here  
Print here does as the name would suggest. Printing the text in the terminal or command line.

#### Main Menu - Sends you back to the main menu

## Spamming  
As the name suggests spamming gives you the ability to spam text in a variety of ways. Please see examples.

Examples  
Spamming with _NEXT LINE_  on "Your Text"

    Your Text 
    Your Text 
    Your Text 
    Your Text 
    Your Text 
    Your Text 
    
Spamming with _SAME LINE_ on "Your Text " <-- Note the space

    Your Text Your Text Your Text Your Text Your Text Your Text 

You will be asked to input some parameters for text spamming. These parameters include:

**Interval** - Of time between each character being typed.  

**Delay** -  Which is useful for scenarios that involve anti-spam measures such as restricting the time in between messages.  

**Number** - Of seconds until start -  To give yourself time to move to the correct window and text field.  

And then you will be presented with two options.

### Repeated  
Will be your text repeated the number of times you have specified with a Enter / Send  after each.  See examples.  

Examples  
Spamming with _NEXT LINE_  on "Your Text"

    Your Text 
    Your Text 
    Your Text 
    Your Text 
    Your Text 
    Your Text 
    #Enter key pressed here
"#Enter key pressed here" line is not printed.

Spamming with _SAME LINE_ on "Your Text " <-- Note the space

    Your Text Your Text Your Text Your Text Your Text Your Text 
    #Enter key pressed here
"#Enter key pressed here" line is not printed.

### Spam  
Will take the entirety of your repeated text at the number that you have specified  then press Enter / Send and will repeat this action a number that you will specify. See examples.  

 Examples  
 Spamming with _NEXT LINE_  on "Your Text" spammed "3" times
 
    Your Text 
    Your Text 
    Your Text 
    Your Text 
    Your Text 
    Your Text 
    #Enter key pressed here
    Your Text 
    Your Text 
    Your Text 
    Your Text 
    Your Text 
    Your Text 
    #Enter key pressed here
    Your Text 
    Your Text 
    Your Text 
    Your Text 
    Your Text 
    Your Text 
    #Enter key pressed here
"#Enter key pressed here" line is not printed.  

Spamming with _SAME LINE_ on "Your Text " <-- Note the space. spammed "3" times

    Your Text Your Text Your Text Your Text Your Text Your Text 
    #Enter key pressed here
    Your Text Your Text Your Text Your Text Your Text Your Text 
    #Enter key pressed here
    Your Text Your Text Your Text Your Text Your Text Your Text 
    #Enter key pressed here
"#Enter key pressed here" line is not printed.  

You will then be offered the ability to begin the spam by pressing enter. And depending on your choices you will also at the end of the spam be given the ability to spam again quit or go back to the Main Menu.

_NOTE_ : Depending on the text field Behavior May differ. Using the "new line" option in your configuration May cause certain text fields to send that message. However the Enter / Send  is sending a key press "enter" so depending on the text field you will have to experiment with your options.  This is why I have tried to make this flexible.

## !!!Warning & Disclaimer!!!
There's no built-in limiter so you could quite easily create a set of parameters that would cause the memory to fill up as well as potentially disk space. There is no multi-threading so this is going to hammer One Core for the entire job. so this is use at your own risk. I take no responsibility for misuse of this script and I do not condone any illegal use of the script. I highly suggest you read the script before using it to familiarize yourself with what it's doing.
