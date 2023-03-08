from pprint import pprint

with open('Task_1,2\\recipes.txt', 'rt', encoding="utf-8") as file:
    cook_book = {}
    for line in file:
        dishes = line.strip()
        quantity_ingredients = int(file.readline())
        ingredients = []
        for _ in range(quantity_ingredients):
            ingredient_name, quantity, measure = file.readline().strip().split(" | ")
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()    
        cook_book[dishes] = ingredients

def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for d, i in cook_book.items():
        if d in dishes:
            for ingredient in i:
                name = ingredient['ingredient_name']
                quantity = int(ingredient['quantity']) * person_count
                measure = ingredient['measure']
                if name not in res.keys():
                    res[name] = {
                        'measure': measure,
                        'quantity': quantity
                    }
                else:
                    res[name]['quantity'] += quantity               
    return res    