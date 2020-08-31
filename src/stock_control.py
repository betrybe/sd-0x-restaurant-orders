class StockControl:
    def __init__(self):
        self.ingredients = {
            'hamburguer': ['pao', 'hamburguer', 'queijo'],
            'pizza': ['massa', 'queijo', 'molho'],
            'misto-quente': ['pao', 'queijo', 'presunto'],
            'coxinha': ['massa', 'frango'],
        }
    
        self.minimum_stock = {
            'pao': 50,
            'hamburguer': 35,
            'queijo': 100,
            'molho': 30,
            'presunto': 20,
            'massa': 20,
            'frango': 10,
        }
    
    def add_new_order(self, costumer, order, day):
        raise NotImplementedError

    def get_quantities_to_buy(self):
        raise NotImplementedError