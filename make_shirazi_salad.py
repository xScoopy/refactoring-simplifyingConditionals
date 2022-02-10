
# by Kami Bigdely
# Consolidate conditional expressions

def dice(ingredients):
    print("diced all ingredients.")


def mix_all(diced_ingredients):
    print("mixed all.")


def add_salt():
    print('added salt.')


def pour(liquid):
    print('poured', liquid + '.',)


def is_not_full_of_ingredients(ingredients):
    return ('cucumber' not in ingredients or 'tomato' not in ingredients or
            'onion' not in ingredients or 'lemon juice' not in ingredients)


def make_shirazi_salad(ingredients):
    if is_not_full_of_ingredients(ingredients):
        print('lacks ingredients')
        return
    dice(ingredients)
    mix_all(ingredients)
    add_salt()
    pour('lemon juice')
    print('Your yummy shirazi salad is ready!')


if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])
