# python3
from linked_list import LinkedList
from hash_element import HashElement
import random

class HashTable:
  def __init__(self) -> None:
    self.table_size = 13
    self.harray = self.create_table(self.table_size)
    self.magic_num = random.randint(2,50)
    self.num_elements = 0
    self.load_factor = 0
    self.max_load_factor = 0.7

  def add(self, k, v):
    index = self.hash(k)
    chain = self.harray[index]
    element = chain.head
    while element and element.key != k:
      element = element.next
    if element == None:
      hash_element = HashElement(k, v)
      hash_element.next = chain.head
      chain.change_head(hash_element)
      self.num_elements += 1
      self.resize()
    else:
      element.value = v
    
  def get_value(self, k):
    index = self.hash(k)
    chain = self.harray[index]
    element = chain.head
    while element and element.key != k:
      element = element.next
    if element:
      return element.value
    
  def remove(self, k):
    index = self.hash(k)
    chain = self.harray[index]
    element = chain.head
    previous_element = None
    while element and element.key !=k:
      previous_element = element
      element = element.next
    if element:
      if previous_element:
        previous_element.add_next(element.next)
      else:
        chain.change_head(element.next)
    



  def create_table(self, size):
    harray = []
    for _ in range(size):
      harray.append(LinkedList())
    return harray

  def resize(self):
    self.load_factor = self.num_elements / self.table_size
    if self.load_factor <= self.max_load_factor:
      return
    self.table_size = self.table_size * 2 + 1
    new_harray = self.create_table(self.table_size)
    for chain in self.harray:
      hash_element = chain.head
      while hash_element != None:
        self.add_element(hash_element.key, hash_element.value, new_harray)
        hash_element = hash_element.next
    self.harray = new_harray
    self.load_factor = self.num_elements / self.table_size


  def add_element(self, k, v, harray):
    index = self.hash(k)
    chain = harray[index]
    hash_element = HashElement(k, v)
    hash_element.add_next(chain.head)
    chain.change_head(hash_element)

  
  def hash(self, k):
    k = str(k)
    index = 0
    for i in range(len(k)):
      index += int(k[i]) * self.magic_num ** i
    index = index % self.table_size
    return index

  def collisions(self):
    collisions = []
    for chain in self.harray:
      length = 0
      el = chain.head
      while el:
        length += 1
        el = el.next
      collisions.append(str(length))
    return collisions