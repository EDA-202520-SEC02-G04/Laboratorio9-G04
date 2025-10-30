from DataStructures.List import list_node as ln

def new_list():
    newlist = {"first": None, "last":None, "size":0,}
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    nodo_nuevo = ln.new_single_node(element)
    nodo_nuevo["next"] = my_list["first"]
    my_list["first"] = nodo_nuevo
    if my_list["size"] == 0:
        my_list["last"] = my_list["first"]
    my_list["size"] += 1
    return my_list
    
def add_last(my_list, element):
    nodo_nuevo = ln.new_single_node(element)
    nodo_nuevo["next"] = None  

    if my_list["size"] == 0:  
        my_list["first"] = nodo_nuevo
        my_list["last"] = nodo_nuevo
    else:
        my_list["last"]["next"] = nodo_nuevo  
        my_list["last"] = nodo_nuevo          
    
    my_list["size"] += 1
    return my_list
    
def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if my_list['first'] is not None:
        return my_list['first']['info']
    return None

def last_element(my_list):
    if my_list["last"] is not None:
        return my_list["last"]["info"]
    return None

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False

def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        return None
    actual = my_list["first"]
    anterior = None
    index = 0
    while index < pos:
        anterior = actual
        actual = actual["next"]
        index += 1
        
    eliminado = actual

    if anterior is None:
        
        my_list["first"] = actual["next"]
        if my_list["size"] == 1:   
            my_list["last"] = None
    else:
        
        anterior["next"] = actual["next"]
        if actual == my_list["last"]:  
            my_list["last"] = anterior

    my_list["size"] -= 1
    return eliminado  

            
def remove_first(my_list):
    eliminado = delete_element(my_list,0)
    if eliminado is None:
        return None
    else:
        return eliminado["info"]

def remove_last(my_list):
    eliminado = delete_element(my_list,my_list["size"]-1)
    if eliminado is None:
        return None
    else:
        return eliminado["info"]
    
def change_info(my_list,pos,new_info):
    if pos < 0 or pos >= my_list["size"]:
        return None
    actual = my_list["first"]
    index = 0
    while index < 0:
        actual = actual["next"]
        index += 1
    actual["info"] = new_info
    return actual
        
def exchange(my_list, pos_1, pos_2):
    if pos_1 < 0 or pos_2 < 0 or pos_1 >= my_list["size"] or pos_2 >= my_list["size"]:
        return None

    node1 = my_list["first"]
    node2 = my_list["first"]

    for _ in range(pos_1):
        node1 = node1["next"]
    for _ in range(pos_2):
        node2 = node2["next"]

    
    node1["info"], node2["info"] = node2["info"], node1["info"]

    return my_list
    
    
def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= my_list["size"]:
        return None
    
    
    if num_elements <= 0:
        return new_list()

    actual = my_list["first"]
    i = 0
    while i < pos:
        actual = actual["next"]
        i += 1

    nueva_lista = new_list()
    count = 0
    while actual is not None and count < num_elements:
        add_last(nueva_lista, actual["info"])
        actual = actual["next"]
        count += 1

    return nueva_lista
        

def insert_element(my_list,element,pos):
    if pos < 0 or pos >= my_list["size"]:
        return None
    actual = my_list["first"]
    index = 0
    nueva_lista = new_list()
    add_last(nueva_lista,actual["info"])
    while index < pos:
        actual= actual["next"]
        add_last(nueva_lista,actual["info"])
        if index == pos:
            actual["info"] = element
            add_last(nueva_lista,actual["info"])
        index += 1
        nueva_lista["size"] += 1
    return nueva_lista
    
        
def default_sort_criteria(element_1,element_2):
    is_sorted = False
    if element_1 <= element_2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list, default_sort_criteria):
    if size(my_list) <= 1:
        return my_list
    primero = my_list["first"]
    posicion_1 = 0
    while primero is not None:
        valor_minimo = primero["info"]
        posicion_minima = posicion_1
        segundo = primero["next"]
        posicion_2 = posicion_1 + 1
        while segundo is not None:
            if not default_sort_criteria(valor_minimo,segundo["info"]):
                posicion_minima = posicion_2
                valor_minimo = segundo["info"]
            segundo = segundo["next"]
            posicion_2 += 1
        if posicion_minima != posicion_1:
            exchange(my_list,posicion_1,posicion_minima)
        primero = primero["next"]
        posicion_1 += 1
    return my_list

def insertion_sort(my_list, default_sort_criteria):
    for i in range(my_list["size"]):
        j = i - 1
        while j >= 0 and  default_sort_criteria(get_element(my_list,i), get_element(my_list,j)):
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

def merge_sort(my_list, default_sort_criteria):
    """
    Ordena una lista enlazada simple usando Merge Sort.
    Usa índices 0-based con la función sub_list.
    """
    if size(my_list) <= 1:
        return my_list

    mitad = size(my_list) // 2
    izquierda = sub_list(my_list, 0, mitad)
    derecha = sub_list(my_list, mitad, size(my_list) - mitad)

    izquierda_ordenada = merge_sort(izquierda, default_sort_criteria)
    derecha_ordenada = merge_sort(derecha, default_sort_criteria)

    return merge(izquierda_ordenada, derecha_ordenada, default_sort_criteria)

def merge(izq, der, default_sort_criteria):
    """
    Funde dos listas ordenadas en una sola, manteniendo el orden.
    """
    resultado = new_list()
    i = 0
    j = 0

    while i < size(izq) and j < size(der):
        if default_sort_criteria(get_element(izq, i), get_element(der, j)):
            add_last(resultado, get_element(izq, i))
            i += 1
        else:
            add_last(resultado, get_element(der, j))
            j += 1

    while i < size(izq):
        add_last(resultado, get_element(izq, i)) 
        i += 1

    while j < size(der):
        add_last(resultado, get_element(der, j))  
        j += 1

    return resultado
    
def quick_sort(my_list,default_sort_criteria):
    if size(my_list) <= 1:
        return my_list
    pivote = get_element(my_list, size(my_list) // 2 )
    izquierda = new_list()
    derecha = new_list()
    mitad = new_list()
    actual = my_list["first"]
    while actual is not None:
        elemento = actual["info"]
        if default_sort_criteria(elemento,pivote) and not default_sort_criteria(pivote, elemento):
            add_last(izquierda,elemento)
        elif default_sort_criteria(pivote,elemento) and not default_sort_criteria(elemento, pivote):
            add_last(derecha,elemento)
        else:
            add_last(mitad,elemento)
        actual = actual["next"]
    izquierda_ordenada = quick_sort(izquierda,default_sort_criteria)
    derecha_ordenada = quick_sort(derecha,default_sort_criteria)
    return unir_lista(izquierda_ordenada,mitad,derecha_ordenada)

def unir_lista(lista_1, lista_2, lista_3):
    nueva_lista = new_list()
    actual_1 = lista_1["first"]
    while actual_1 is not None:
        elemento = actual_1["info"]
        add_last(nueva_lista,elemento)
        actual_1 = actual_1["next"]
    
    actual_2 = lista_2["first"]
    while actual_2 is not None:
        elemento2 = actual_2["info"]
        add_last(nueva_lista,elemento2)
        actual_2 = actual_2["next"]
    
    actual_3 = lista_3["first"]
    while actual_3 is not None:
        elemento3 = actual_3["info"]
        add_last(nueva_lista,elemento3)
        actual_3 = actual_3["next"]
    return nueva_lista
    
        
    
        
    