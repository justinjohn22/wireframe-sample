### Instructions on how to compile and run the executable

The QueryProgram is very easy to run and use. 

<b> Synopsis </b> <br>
The QueryProgram is made for users who love lego. Users can use this application to easily browse the huge library of information about lego sets and their themes. 

## Project Setup and Use
1. Ensure Python is installed 
2. Download the zip file and unpack in a local folder 
3. Open command prompt `at this folder location` 
4. Enter the following command into command prompt: `py .\ProgramRunner.py`

## Program use 

Once program is running, the user is presented with a console CLI.

<i>Users have two options:  </i>

1. Enter the set ID of the lego set/theme they would like the information of.

2. Type the command 'exit' into the program to exit the program.

After a valid ID has been input, the program will retrieve the appropiate information and offers the user for another input. As stated above, the users have the option to either make another query or to exit the program by entering 'exit'.

## Program Complexity 
1. For reading each file, the program has to loop through every field from the external file, giving an O(n) complexity.

2. The program uses a Python Dictionary (which is Python's HashMap) to store data, therefore it only required an O(1) operation to make a query from the Sets dictionary and another O(1) operation to make a query from the Themes dictionary.

<br><br>

> Thanks for using the QueryProgram.



