"""Print out all the melons in our inventory."""

# from melons import melons

melon_data = {
    'Honeydew': {
    'price': 0.99,
    'seedlessness': True
    }, 
    'Crenshaw': {
    'price': 2.00,
    'seedlessness': False
    },
    'Crane': {
    'price': 2.50,
    'seedlessness': False
    },
    'Casaba': {
    'price': 2.50,
    'seedlessness': False
    },
    'Cantaloupe': {
    'price': .99,
    'seedlessness': False
    },
}

def add_melon_attributes(melons):
    for key, value in melon_data.items():
        if key in melon_data:
            melon_data[key] = [melon_data[key], 'flesh_color:']
            melon_data[key] = [melon_data[key], 'weight:']
            melon_data[key] = [melon_data[key], 'rind_color:']
            return melons

print_melon(melon_data)

def print_melon(melons):
    """Print each melon with corresponding attribute information."""
    for melon_name, attributes in melons.items():
        print(melon_name)
        for new_attribute, value in attributes.items():
            print(f'{new_attribute}: {value}')

print(add_melon_attributes(melon_data))




    # have_or_have_not = 'have'
    # if seedless:
    #     have_or_have_not = 'do not have'

    # print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])




