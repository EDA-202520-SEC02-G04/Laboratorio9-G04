from DataStructures.Priority_queue import pq_entry as pqe
from DataStructures.List import array_list as al

def new_heap(is_min_pq=True):
    heap = {
        "elements": al.new_list(),
        "size": 0,
        "cmp_function": None
    }
    
    pareja_invalida = pqe.new_pq_entry(None, None)
    al.add_first(heap['elements'], pareja_invalida)
    if is_min_pq:
        heap['cmp_function'] = default_compare_lower_value
    else:
        heap['cmp_function'] = default_compare_higher_value
    return heap
    
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

def size(my_heap):
    return my_heap["size"]

def is_empty(my_heap):
    if size(my_heap)==0:
        return True
    return False

def exchange(my_heap, i, j):
    temp = my_heap['elements']['elements'][i]
    my_heap['elements']['elements'][i] = my_heap['elements']['elements'][j]
    my_heap['elements']['elements'][j] = temp
    return my_heap

def swim(my_heap, pos):