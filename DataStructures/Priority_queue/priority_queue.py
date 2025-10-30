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
    if pqe.get_priority(father_node) >= pqe.get_priority(child_node):
        return True
    return False

def default_compare_lower_value(father_node, child_node):
    if pqe.get_priority(father_node) <= pqe.get_priority(child_node):
        return True
    return False



def priority(my_heap, parent, child):
    return my_heap["cmp_function"](parent, child)

def is_empty(my_heap):
    if my_heap["size"]==0:
        return True
    return False

def exchange(my_heap, i, j):
    temp = my_heap['elements']['elements'][i]
    my_heap['elements']['elements'][i] = my_heap['elements']['elements'][j]
    my_heap['elements']['elements'][j] = temp
    return my_heap