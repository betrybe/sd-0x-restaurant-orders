from src.inventory_control import InventoryControl


def teste_validar_atualizou_a_quantidade_em_estoque():
    inventory = InventoryControl()
    inventory.add_new_order("jorge", "hamburguer", "terça-feira")
    inventory.add_new_order("jorge", "hamburguer", "terça-feira")
    hamburguer = inventory.get_shopping_list()
    assert  hamburguer.get('pao') == 2
    assert  hamburguer.get('carne') == 2
    assert  hamburguer.get('queijo') == 2
    assert  hamburguer.get('molho') == 0
    assert  hamburguer.get('presunto') == 0
    assert  hamburguer.get('massa') == 0
    assert  hamburguer.get('frango') == 0


def teste_validar_comprar_todo_estoque_de_hamburguer():
    ingredients = InventoryControl()
    count = 1
    while count <= 50:
        ingredients.add_new_order("jorge", "hamburguer", "terça-feira")
        count += 1
    hamburguer = ingredients.get_shopping_list()
    assert  hamburguer.get('pao') == 50
    assert  hamburguer.get('carne') == 50
    assert  hamburguer.get('queijo') == 50
    assert  hamburguer.get('molho') == 0
    assert  hamburguer.get('presunto') == 0
    assert  hamburguer.get('massa') == 0
    assert  hamburguer.get('frango') == 0

def teste_validar_ingrediente_compartilhados():
    ingredients = InventoryControl()
    count = 1
    while count <= 50:
        ingredients.add_new_order("jorge", "hamburguer", "terça-feira")
        ingredients.add_new_order("maria", "pizza", "terça-feira")
        count += 1
    hamburguer_pizza = ingredients.get_shopping_list()
    assert  hamburguer_pizza.get('pao') == 50
    assert  hamburguer_pizza.get('carne') == 50
    assert  hamburguer_pizza.get('queijo') == 100
    assert  hamburguer_pizza.get('molho') == 50
    assert  hamburguer_pizza.get('presunto') == 0
    assert  hamburguer_pizza.get('massa') == 50
    assert  hamburguer_pizza.get('frango') == 0
