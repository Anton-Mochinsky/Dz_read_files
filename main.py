def get_ingredients(n, f):
    ingredients = []

    for i in range(n):
        ingredient = f.readline().rstrip().split(' | ')

        ingredients.append({
            'ingredient_name': ingredient[0],
            'quantity': int(ingredient[1]),
            'measure': ingredient[2]
        })

    return ingredients


def get_cook_book():
    f = open('recipes.txt', 'r', encoding='utf-8')
    cook_book = {}

    while True:
        dish_name = f.readline()

        if not dish_name:
            break

        dish_name = dish_name.rstrip()
        ingredient_number = int(f.readline())
        ingredients = get_ingredients(ingredient_number, f)
        cook_book[dish_name] = ingredients

        f.readline()

    f.close()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book()
    shop_list = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']

            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list[ingredient_name] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }

    return shop_list


def sort_by_length(input_str):
    return len(input_str)


def merge_files(file_names):
    contents = []

    for file_name in file_names:
        io = open(file_name, 'r', encoding='utf-8')

        contents.append(io.readlines())

        io.close()

    contents.sort(key=sort_by_length, reverse=True)

    output = open('output.txt', 'w', encoding='utf-8')

    for i in range(len(file_names)):
        output.write(file_names[i] + '\n')
        output.write(str(len(contents[i])) + '\n')
        output.write(''.join(contents[i])+'\n')

    output.close()


if __name__ == '__main__':
    merge_files(['1.txt', '2.txt', '3.txt'])