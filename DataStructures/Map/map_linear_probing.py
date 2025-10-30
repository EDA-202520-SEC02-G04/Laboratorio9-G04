from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
import random
from DataStructures.List import array_list as al
from DataStructures.List import array_list as lt

def new_map(num_elements, load_factor, prime= 109345121):
        capacidad = mf.next_prime(int(num_elements/load_factor))
        scale = random.randint(1,prime-1)
        shift = random.randint(1,prime-1)
        hash_table = {
            "prime":prime,
            "capacity":capacidad,
            "scale":scale,
            "shift":shift,
            "table":al.new_list(),
            "current_factor":0,
            "limit_factor":load_factor,
            "size":0,
            "type": "PROBE_HASH_MAP"
        }
        for _ in range(capacidad):
                entry = me.new_map_entry(None,None)
                al.add_last(hash_table['table'], entry)
        return hash_table
    
def is_available(table, pos):

   entry = lt.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def find_slot(my_map, key, hash_value):
    first_avail = None
    found = False
    ocupied = False
    while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = lt.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, lt.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
    return ocupied, first_avail

def put(my_map,key,value):
    pos = mf.hash_value(my_map,key)
    ocupado, slot = find_slot(my_map,key,pos)
    if ocupado:
        entry = lt.get_element(my_map["table"],slot)
        entry["value"] = value
    else:
        new_entry = me.new_map_entry(key,value)
        lt.change_info(my_map["table"],slot,new_entry)
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        if my_map["current_factor"] > my_map["limit_factor"]:
            my_map = rehash(my_map)
    return my_map

def rehash(my_map):
    capacidad_doble = mf.next_prime(my_map["capacity"] * 2)
    nuevo_mapa = {
        "prime": my_map["prime"],
        "capacity": capacidad_doble,
        "scale": 1,  
        "shift": 0,  
        "table": al.new_list(),
        "current_factor": 0,
        "limit_factor": my_map["limit_factor"],
        "size": 0,
        "type": "PROBE_HASH_MAP"
    }
    for _ in range(capacidad_doble):
        entry = me.new_map_entry(None, None)
        al.add_last(nuevo_mapa['table'], entry)

    for i in range(lt.size(my_map["table"])):
        entry = lt.get_element(my_map["table"], i)
        if entry is not None and entry["key"] is not None:
            put(nuevo_mapa, entry["key"], entry["value"])

    return nuevo_mapa

def contains(my_map,key):
    respuesta = False
    for i in range(lt.size(my_map["table"])):
        entry = lt.get_element(my_map["table"],i)
        if me.get_key(entry) == key:
            respuesta = True
    return respuesta

def remove(my_map,key):
    if contains(my_map,key) == False:
        return my_map
    for i in range(lt.size(my_map["table"])):
        entry = lt.get_element(my_map["table"],i)
        if me.get_key(entry) == key:
            entry["key"] = "__EMPTY__"
            entry["value"] = "__EMPTY__"
            my_map["size"] -= 1
    return my_map

def get(my_map,key):

    valor = None
    for i in range(lt.size(my_map["table"])):
        entry = lt.get_element(my_map["table"],i)
        if me.get_key(entry) == key:
            valor = entry["value"]
    return valor
            
def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    if size(my_map) == 0:
        return True
    else:
        return False

def key_set(my_map):
    if is_empty(my_map):
        return lt.new_list()
    lista_llaves = lt.new_list()
    for i in range(lt.size(my_map["table"])):
        entry = lt.get_element(my_map["table"],i)
        if entry["key"] != None and entry["key"] != '__EMPTY__':
            lt.add_last(lista_llaves,entry["key"])
    return lista_llaves
    
def value_set(my_map):
    if is_empty(my_map):
        return lt.new_list()
    lista_llaves = lt.new_list()
    for i in range(lt.size(my_map["table"])):
        entry = lt.get_element(my_map["table"],i)
        if entry["value"] != None and entry["value"] != '__EMPTY__':
            lt.add_last(lista_llaves,entry["value"])
    return lista_llaves
    
    

            
        
        
    

    