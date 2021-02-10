#Syed Ahsan
#1867491

num_lemon_cups = float(input('Enter amount of lemon juice (in cups):'))
num_water_cups = float(input('Enter amount of water (in cups):'))
num_nectar_cups = float(input('Enter amount of agave nectar (in cups):'))
num_servings_cups = float(input('How many servings does this make?'))

print('\nLemonade ingredients - yields {} servings'.format(num_servings_cups))
print('{} cup(s) lemon juice'.format(num_lemon_cups))
print('{} cup(s) water'.format(num_water_cups))
print('{} cup(s) agave nectar'.format(num_nectar_cups))


num_servings_required = float(input('\nHow many servings would you like to make?\n'))

print('\nLemonade ingredients - yields {} servings'.format(num_servings_required))
print('{} cup(s) lemon juice'.format(num_lemon_cups * num_servings_required / num_servings_cups))
print('{} cup(s) water'.format(num_water_cups * num_servings_required / num_servings_cups))
print('{} cup(s) agave nectar'.format(num_nectar_cups * num_servings_required / num_servings_cups))


print('\nLemonade ingredients - yields {} servings'.format(num_servings_required))
print('{} gallon(s) lemon juice'.format(num_lemon_cups * num_servings_required / num_servings_cups / 16))
print('{} gallon(s) water'.format(num_water_cups * num_servings_required / num_servings_cups / 16))
print('{} gallon(s) agave nectar'.format(num_nectar_cups * num_servings_required / num_servings_cups / 16))