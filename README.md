## PASTE_O_ MATIC

Simple Python3 script for inputting text which you wish to repeat over and over. 
Various forms of output options.  
New line or Same line.  
Your text is output to a file if you wish to save it.  
Your text can also be typed for you using PyAutoGUI for "realistic human" input.   
You can change the amount of time until spamming will begin so that you have time to move 
to whatever text field you need and you can also change the interval at which each character is typed.  
This can be useful for adjusting for spamming filters in various chat applications.  

## Dependencies  

This is a simple script so there's no point in me making a install for it however the dependencies for the script are certainly worth installing.  

latest versions  

clipboard  
pyautgui  


## Warning!!! and Disclaimer!!!
Because of the sheer laziness of this script, the text that is generated is both stored on the disk and in memory.
If the text you generate takes more memory or disk space then you have... You'er probably going to have a bad time. 
There is no multi-threading so this is likely to hammer one core. 
The text file is generated before reading it into memory. 
What's more, this is very inefficient code and is going to be accessing the file for every paste. 
So as a Disclaimer I take no responsibility any damage this script may cause and I suggest you read it over first.
With all that being said if you're just trying to spam your Bae with 1000 kisses you're probably good to go.