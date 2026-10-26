# importing math_utils
import math_utils

# we can't import them direct by function name first 
# we have to use math_utils then followed by function name
print("Adding 5 and 2:",(math_utils.add(5,2)))

print("Subtract 5 and 2:",(math_utils.subtract(5,2)))

# if we use this way we call the function direct by the their name
from math_utils import square

print("Square of 2:",(square(2)))

import string_utils

print("Capitalize 'hello' word:",(string_utils.capitalize_words("hello")))

print("Reverse 'hello' word:",(string_utils.reverse_string("hello")))

print("Counting 'hello' word:",(string_utils.word_count("hello")))

# here every function store "shop_package" folder 
# we are calling function and denoting with a short name
# so if function name is so long we can use frequently by using short name of it 

import shop_package.discount as disc

print("Price after discount:",(disc.apply_discount(1000,10)))

from shop_package.billing import calculate_total

print("The sum of the list=[100,200,300]:",(calculate_total([100,200,300])))

import shop_package

print("The default value of discount deducted:",(shop_package.flat_discount(1000)))

print("The 5% tax added on price:",(shop_package.apply_tax(1000)))