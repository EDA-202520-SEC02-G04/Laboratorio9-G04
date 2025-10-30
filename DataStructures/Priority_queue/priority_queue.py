from DataStructures.Priority_queue import pq_entry as pqe

def new_heap(is_min_pq=True):
    if is_min_pq:
        return {
            'elements': {
                 'elements': [None],
                'size': 1
            },
            'size': 0,
            'cmp_function': default_compare_lower_value()
        }
    return {
            'elements': {
                 'elements': [None],
                'size': 1
            },
            'size': 0,
            'cmp_function': default_compare_higher_value()
        }
    
def default_compare_higher_value(father_node, child_node):
    if pqe.get father_node

def default_compare_lower_value(father_node, child_node):




def is_empty(my_heap):
    empty=False
    if my_heap["size"]=0:
        empty=True
        return True
    return empty

    