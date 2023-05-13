# python3

import random


_multiplier = random.randint(10, 1000)
_prime = 100010 #max amount of constraints is 10^5 (N value is 1<N<10^5), so that %_prime values are different

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        self.hashed_number = hash_func(query[1])
        if self.type == 'add':
            self.name = query[2]

def hash_func(s):
    ans = 0
    for c in reversed(s):
        ans = (ans * _multiplier + ord(c)) % _prime
    return ans

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]   #initializing query for each input line

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.hashed_number] = cur_query.name
        elif cur_query.type == 'del':
            contacts.pop(cur_query.hashed_number, None)
        else:
            response = contacts.get(cur_query.hashed_number, None)
            result.append(response if response else 'not found')
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
