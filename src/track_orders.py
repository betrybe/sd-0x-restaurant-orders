class TrackOrders:
  def add_new_order(self, costumer, order, day):
    raise NotImplementedError

  def get_most_ordered_dish_per_costumer(self, costumer):
    raise NotImplementedError

  def get_order_frequency_per_costumer(self, costumer, order):
    raise NotImplementedError

  def get_never_ordered_per_costumer(self, costumer):
    raise NotImplementedError 