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

print(add_melon_attributes(melon_data))




# melon_names = {
#     1: 'Honeydew': 
#     2: 'Crenshaw',
#     3: 'Crane',
#     4: 'Casaba',
#     5: 'Cantaloupe',
# }

# melon_prices = {
#     1: 0.99,
#     2: 2.00,
#     3: 2.50,
#     4: 2.50,
#     5: 0.99,
# }

# melon_seedlessness = {
#     1: True,
#     2: False,
#     3: False,
#     4: False,
#     5: False,






