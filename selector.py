# Random selection python by VanQuang

import random

foods = [
    'Bun rieu',
    'Com',
    'Ca',
    'Cua',
    'Tom'

]

# random.randint(1, 5) --> random number between 1 and 5
# random.choice(array) --> random item in this array

selected = random.choice(foods) # randomly choose a food for the lunch at PY VINA

print('You should eat the' )
print(selected)
