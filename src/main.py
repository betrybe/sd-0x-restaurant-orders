# Recebe o sinal de order
# 

from track_orders import TrackOrders
from stock_control import StockControl
from pubsub import pub
import csv

def track_orders(costumer, order, day):
    tracker = TrackOrders()
    tracker.add_new_order(costumer, order, day)

def stock_control(costumer, order, day):
    control = StockControl()
    pass

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

    print(tracker.get_order_frequency('maria', 'hamburguer'))
    print(control.get_quantities_to_buy())
    

if __name__ == "__main__":
    main()
