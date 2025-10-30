def new_list():
    newlist = {'elements': [], 'size': 0}
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list,element,cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range (0,size):
            info = my_list["elements"][keypos]
            if cmp_function(element,info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1


def add_first(my_list, element):
    newlist = [element]
    for i in range(size(my_list)):
        newlist.append(my_list['elements'][i])
    my_list['size'] += 1
    my_list['elements'] = newlist
    return my_list

def add_last(my_list, element):
    my_list['elements'].append(element)
    my_list['size'] +=1
    return my_list

def size(my_list):
    return my_list['size']

def first_element(my_list):
    if my_list["size"] == 0:
        return None
    return my_list['elements'][0]

def is_empty(my_list):
    if len(my_list['elements']) == 0:
        return True
    return False

def last_element(my_list):
    if my_list["size"] == 0:
        return None
    return my_list['elements'][-1]

def delete_element(my_list, pos):
    my_list['size'] -= 1
    my_list['elements'].pop(pos)
    return my_list
    
def remove_first(my_list):
    if my_list["size"] == 0:
        return None
    my_list["size"] -= 1
    return my_list["elements"].pop(0)

def remove_last(my_list):
    if my_list["size"] == 0:
        return None
    my_list["size"] -= 1
    return my_list["elements"].pop(-1)

def insert_element(my_list, element, pos):
    index = 0
    nueve_lista = new_list()
    while index < my_list["size"]:
        add_last(nueve_lista,my_list["elements"][index])
        if index == pos:
            add_last(nueve_lista,element)
        index += 1                  
    return nueve_lista
    

def change_info(my_list, pos, element):
    my_list['elements'][pos] = element
    return my_list

def exchange(my_list, pos1, pos2):
    temp = my_list["elements"][pos1] 
    my_list["elements"][pos1] = my_list["elements"][pos2] 
    my_list["elements"][pos2] = temp 
    return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= my_list["size"] or num_elements <= 0:
        return None
    
    lista_nueva = new_list()
    fin = min(pos_i + num_elements, my_list["size"])  
    
    contador = pos_i
    while contador < fin:
        add_last(lista_nueva, my_list["elements"][contador])
        contador += 1
    
    return lista_nueva


def default_sort_criteria(element_1,element_2):
    is_sorted = False
    if element_1 <= element_2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list, default_sort_criteria):
    for i in range(my_list["size"]):
        for j in range(i, my_list["size"]):
            if default_sort_criteria(my_list["elements"][j], my_list["elements"][i]):
                my_list = exchange(my_list, i, j)
    return my_list

def insertion_sort(my_list, default_sort_criteria):
    for i in range(my_list["size"]):
        j = i - 1
        while j >= 0 and default_sort_criteria(my_list["elements"][i], my_list["elements"][j]):
            my_list = exchange(my_list, j, j + 1)
    return my_list

def shell_sort(my_list, default_sort_criteria):
    n = size(my_list)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = get_element(my_list, i)
            j = i
            while j >= gap and not default_sort_criteria(get_element(my_list, j - gap), temp):
                change_info(my_list, j, get_element(my_list, j - gap))
                j -= gap
            change_info(my_list, j, temp)
        gap //= 2

    return my_list



def merge_sort(my_list,default_sort_criteria):
    if 1 >= size(my_list):
        return my_list
    mitad = size(my_list) // 2
    izquierda = sub_list(my_list,0,mitad)
    derecha = sub_list(my_list,mitad,size(my_list)-mitad)
    izquierda_ordenada = merge_sort(izquierda,default_sort_criteria)
    derecha_ordenada = merge_sort(derecha,default_sort_criteria)
    return merge(izquierda_ordenada,derecha_ordenada,default_sort_criteria)

def merge(izq,der,default_sort_criteria):
    respuesta = new_list()
    i = 0
    j = 0
    while i < size(izq) and j < size(der):
        if default_sort_criteria(get_element(izq,i), get_element(der,j)):
            add_last(respuesta,get_element(izq,i))
            i += 1
        else:
            add_last(respuesta,get_element(der,j))
            j += 1
    while i < size(izq):
        add_last(respuesta,get_element(izq,i))
        i += 1
    while j < size(der):
        add_last(respuesta,get_element(der,j))
        j += 1
    return respuesta

def quick_sort(my_list,default_sort_criteria):
    if size(my_list) <= 1:
        return my_list
    pivote = get_element(my_list, size(my_list)//2)
    izquierda = new_list()
    mitad = new_list()
    derecha = new_list()
    for i in range(size(my_list)):
        elemento = get_element(my_list,i)
        if default_sort_criteria(elemento,pivote) and not default_sort_criteria(pivote, elemento):
            add_last(izquierda,elemento)
        elif default_sort_criteria(pivote,elemento) and not default_sort_criteria(elemento, pivote):
            add_last(derecha,elemento)
        else:
            add_last(mitad,elemento)
    izquierda_ordenada = quick_sort(izquierda,default_sort_criteria)
    derecha_ordenada = quick_sort(derecha,default_sort_criteria)
    return unir_lista(izquierda_ordenada,mitad,derecha_ordenada)

def unir_lista(lista_1, lista_2, lista_3):
    nueva_lista = new_list()
    for i in range(size(lista_1)):
        add_last(nueva_lista, get_element(lista_1, i))
    for i in range(size(lista_2)):
        add_last(nueva_lista, get_element(lista_2, i))
    for i in range(size(lista_3)):
        add_last(nueva_lista, get_element(lista_3, i))
    return nueva_lista