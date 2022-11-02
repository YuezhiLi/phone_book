class HashElement:
  def __init__(self, k, v):
    self.key = k
    self.value = v
    self.next = None

  def add_next(self, hash_element):
    self.next = hash_element