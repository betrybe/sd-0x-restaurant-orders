from src.inventory_control import InventoryControl


def teste_validar_atualizou_a_quantidade_em_estoque():
    inventory = InventoryControl()
    inventory.add_new_order("jorge", "hamburguer", "terça-feira")
    inventory.add_new_order("jorge", "hamburguer", "terça-feira")
    hamburguer = inventory.get_shopping_list()
    total_ingredients = {
        "pao": 2,
        "carne": 2,
        "queijo": 2,
        "molho": 0,
        "presunto": 0,
        "massa": 0,
        "frango": 0,
    }
    assert hamburguer == total_ingredients


def teste_validar_comprar_todo_estoque_de_hamburguer():
    ingredients = InventoryControl()
    count = 1
    while count <= 50:
        ingredients.add_new_order("jorge", "hamburguer", "terça-feira")
        count += 1
    hamburguer = ingredients.get_shopping_list()
    total_ingredients = {
        "pao": 50,
        "carne": 50,
        "queijo": 50,
        "molho": 0,
        "presunto": 0,
        "massa": 1,
        "frango": 0,
    }
    assert hamburguer == total_ingredients


def teste_validar_ingrediente_compartilhados():
    ingredients = InventoryControl()
    count = 1
    while count <= 50:
        ingredients.add_new_order("jorge", "hamburguer", "terça-feira")
        ingredients.add_new_order("maria", "pizza", "terça-feira")
        count += 1
    hamburguer_pizza = ingredients.get_shopping_list()
    total_ingredients = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 0,
        "massa": 50,
        "frango": 0,
    }
    assert hamburguer_pizza == total_ingredients
