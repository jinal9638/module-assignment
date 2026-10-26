# Python Importing,Creating Modules and Packages

This project demonstrates how to organize code into modules and packages to make the project 
reusable and scalable.

# Structure of the folder

modules_assignment/
main.py
Math_utils.py
string_utils.py
shop_package/
init _. py
discount.py
billing.py

# Task

# Task 1 : Create a simple module

This module explain simple arithmetic calculation done by using function which store in one file and then it wil import in other main file to use when required.In task,we have instructed to use two way to import function in main file.

1.import math_utils

When you import this way you have to use file name followed by function name
(e.g.,math_utils.add)

2.from math_utils square

Here you are only calling single and specific function.You can now use directly by name of this function.Don't need to use file name.

# Task 2 : Create another module 

This module specific for string.Here we are capitalize,reverse and counting length of the word.

For capitalize using built-in method text.capitalize()

For reverse the text using negative indexing 

For word count, use the built-in len() function to check how many characters a word contains.

# Task 3 : Create a Simple Package

In this task creating a main folder named 'shop_package' which contains 3 files which names are 
'discount.py','billing.py','__init__.py'.This files contains simple arithmetic function that use for billing.

# discount.py

This files contains two function:

1. apply_discount

-> using two parameters price and discount
-> You have to give both value mandatory for calculation
-> You can get value of the price after discount

2. flat_discount

-> use single paramter price
-> default value 50 deduct

# billing.py

This file contains two function

1. calculate_total

-> use single argument containing the whole list
-> sum of the list elements

2. apply_tax

-> use single parameter 
-> default 5% tax add

# __init__.py

An __init__.py file is a special file placed inside a directory to tell Python that the directory should be treated as a package (a collection of modules).

Because of this __init__.py setup, a user can write cleaner, shorter import statements in their main script.

# Task 4 : Importing the package in main.py

Here every function store "shop_package" folder we are calling function and denoting with a short name so if function name is so long we can use frequently by using short name of it 

import shop_package.discount as disc

Called every function which is inside the package.

# How to Run

1.Make sure Python 3.10+ is installed on your system.
2.Download the project ZIP file.
3.Extract this downloaded ZIP file to a folder on your computer.
4.Open the extracted folder with Visual studio code. 
5.Press F5 (or click the Run/Play button) in VS Code to run the file.

# Github Link

This GitHub repo link:

[(https://github.com/jinal9638/module-assignment.git)]