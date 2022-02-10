

# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('!!!')
    print('there is a toxin in the food!')
    print('!!!')
    print('made alert sound.')


def make_accept_sound():
    print('***')
    print('Toxin Free')
    print('***')
    print('made acceptance sound')


harmful_ingredients = ['sodium nitrate', 'sodium benzoate', 'sodium oxide']


def is_harmful(ingredients):
    harmful = False
    for ingredient in ingredients:
        if ingredient in harmful_ingredients:
            harmful = True
    return make_alert_sound() if harmful else make_alert_sound()


ingredients = ['sodium benzoate']

is_harmful(ingredients)
