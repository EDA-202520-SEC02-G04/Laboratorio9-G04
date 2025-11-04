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
    k = pos
    while k > 1:
        parent = k // 2
        parent_node = al.get_element(my_heap["elements"], parent)
        curr_node = al.get_element(my_heap["elements"], k)
        if priority(my_heap, parent_node, curr_node):
            break
        exchange(my_heap, k, parent)
        k = parent

def insert(my_heap, priority_value, value):
    entrada = pqe.new_pq_entry(priority_value, value)
    al.add_last(my_heap["elements"], entrada)
    my_heap["size"] += 1
    swim(my_heap, size(my_heap))

def sink(my_heap, k):
    n = size(my_heap)
    while 2 * k <= n:
        izq = 2 * k
        der = 2 * k + 1
        if der <= n:
            left_node = al.get_element(my_heap["elements"], izq)
            right_node = al.get_element(my_heap["elements"], der)
            j = izq if priority(my_heap, left_node, right_node) else der
        else:
            j = izq
        node_k = al.get_element(my_heap["elements"], k)
        node_j = al.get_element(my_heap["elements"], j)
        if priority(my_heap, node_k, node_j):
            break
        exchange(my_heap, k, j)
        k = j

def remove(my_heap):
    if is_empty(my_heap):
        return None
    else:
        elementos = my_heap["elements"]["elements"]
        top_entry = elementos[1]
        last_entry = elementos[size(my_heap)]
        elementos[1] = last_entry 
        al.remove_last(my_heap["elements"])
        my_heap["size"] -= 1
        if not is_empty(my_heap):
            sink(my_heap, 1)

        return pqe.get_value(top_entry)

def get_first_priority(my_heap):
    if is_empty(my_heap):
        return None
    root = al.get_element(my_heap["elements"], 1)
    return pqe.get_priority(root)

def index_of_value(my_heap, value):
    n = size(my_heap)
    for i in range(1, n + 1):
        entry = al.get_element(my_heap["elements"], i)
        if pqe.get_value(entry) == value:
            return i
    return None

def is_present_value(my_heap, value):
    if my_heap is None or size(my_heap) == 0:
        return -1
    elemento = my_heap["elements"]["elements"]
    for i in range(1 , size(my_heap)+1):
        if elemento[i]["value"] == value:
            return i
    return -1

def contains(my_heap, value):
    if is_present_value(my_heap,value) == -1:
        return False
    else:
        return True

def improve_priority(my_heap, value, new_priority):
    i = index_of_value(my_heap, value)
    if i is None:
        return False
    entrada = al.get_element(my_heap["elements"], i)
    old = pqe.get_priority(entrada) 
    pqe.set_priority(entrada, new_priority)
    al.change_info(my_heap["elements"], i, entrada)
    if i > 1:
        parent = i // 2
        parent_node = al.get_element(my_heap["elements"], parent)
        curr_node = al.get_element(my_heap["elements"], i)
        if not priority(my_heap, parent_node, curr_node):
            swim(my_heap, i)
            return True
    sink(my_heap, i)
    return True

