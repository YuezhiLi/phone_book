# python3
from hash_table import HashTable

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = HashTable()
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts.add(cur_query.number, cur_query.name)
        elif cur_query.type == 'del':
            contacts.remove(cur_query.number)
        else:
            response = contacts.get_value(cur_query.number)
            if response is None:
                response = 'not found'
            result.append(response)
    # return result
    return contacts.collisions()

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

