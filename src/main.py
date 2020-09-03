import csv
from track_orders import TrackOrders
from stock_control import StockControl
from pubsub import pub


def print_info(tracker, control):
    # Qual o prato mais pedido por Maria?
    print(tracker.get_most_ordered_dish_per_costumer('maria'))

    # Quantas vezes Arnaldo pediu hamburguer?
    print(tracker.get_order_frequency_per_costumer('arnaldo', 'hamburguer'))
    
    # Quais pratos Joao nunca pediu?
    print(tracker.get_never_ordered_per_costumer('joao'))

    # Quais dias Joao nunca foi na lanchonete?
    print(tracker.get_days_never_visited_per_costumer('joao'))

    # Lista de compras
    print(control.get_shopping_list())

def main ():
    topic = 'order'
    path = 
    
    tracker = TrackOrders()
    control = StockControl()
    subs = [tracker.add_new_order, control.add_new_order]

    # Subscriptions
    for sub in subs:
        pub.subscribe(sub, topic)

    # Message sending
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for costumer, order, day in csv_reader:
            pub.sendMessage(topic, costumer=costumer, order=order, day=day)

    print_info(tracker, control)
    

if __name__ == "__main__":
    main()
