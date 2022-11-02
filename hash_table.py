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
    self.add_element(k, v, self.harray)
    self.num_elements += 1
    self.resize()

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



