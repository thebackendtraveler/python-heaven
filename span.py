import re  
txt = "The rain in Spain"
x = re.search(r"\bS\w+",txt)
print("-"*80)
print("Position of first occurence: ", x.span())
print("-"*80)

import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print("-"*80)
print("Printing the string into the function: ", x.string)
print("-"*80)

import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print("-"*80)
print("Printing the part of the string where the match was: ", x.group())
print("-"*80)