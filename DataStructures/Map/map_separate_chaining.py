from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import single_linked_list as sl
from DataStructures.List import array_list as lt
import random


def new_map(num_elements, load_factor, prime=109345121):
    capacidad = mf.next_prime(int(num_elements / load_factor))
    scale = random.randint(1, prime - 1)
    shift = random.randint(1, prime - 1)

    hash_table = {
        "prime": prime,
        "capacity": capacidad,
        "scale": scale,
        "shift": shift,
        "table": sl.new_list(),   
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0,
        "type": "CHAINING_HASH_MAP"
    }

   
    for _ in range(capacidad):
        sl.add_last(hash_table["table"], sl.new_list())

    return hash_table


def put(my_map, key, value):
    index = mf.hash_value(my_map, key)
    bucket = sl.get_element(my_map["table"], index)

    
    for i in range(sl.size(bucket)):
        entry = sl.get_element(bucket, i)
        if entry["key"] == key:
            entry["value"] = value
            return

    
    sl.add_last(bucket, {"key": key, "value": value})
    my_map["size"] += 1
    my_map["current_factor"] = my_map["size"] / my_map["capacity"]

    
    if my_map["current_factor"] > my_map["limit_factor"]:
        nuevo = rehash(my_map)
        my_map.update(nuevo)   


def get(my_map, key):
    pos = mf.hash_value(my_map, key)
    bucket = sl.get_element(my_map["table"], pos)

    actual = bucket["first"]
    while actual is not None:
        entry = actual["info"]
        if me.get_key(entry) == key:
            return entry["value"]
        actual = actual["next"]

    return None


def contains(my_map, key):
    return get(my_map, key) is not None


def remove(my_map, key):
    pos = mf.hash_value(my_map, key)
    bucket = sl.get_element(my_map["table"], pos)

    index = 0
    actual = bucket["first"]
    while actual is not None:
        entry = actual["info"]
        if me.get_key(entry) == key:
            sl.delete_element(bucket, index)
            my_map["size"] -= 1
            return my_map
        actual = actual["next"]
        index += 1

    return my_map


def key_set(my_map):
    lista_llaves = lt.new_list()

    for i in range(sl.size(my_map["table"])):
        bucket = sl.get_element(my_map["table"], i)
        actual = bucket["first"]
        while actual is not None:
            entry = actual["info"]
            lt.add_last(lista_llaves, me.get_key(entry))
            actual = actual["next"]

    return lista_llaves


def value_set(my_map):
    lista_valores = lt.new_list()

    for i in range(sl.size(my_map["table"])):
        bucket = sl.get_element(my_map["table"], i)
        actual = bucket["first"]
        while actual is not None:
            entry = actual["info"]
            lt.add_last(lista_valores, entry["value"])
            actual = actual["next"]

    return lista_valores


def size(my_map):
    return my_map["size"]


def is_empty(my_map):
    return size(my_map) == 0


def rehash(my_map):
    nueva_capacidad = mf.next_prime(my_map["capacity"] * 2)

    nueva_tabla = sl.new_list()
    for _ in range(nueva_capacidad):
        sl.add_last(nueva_tabla, sl.new_list())

    nuevo_mapa = {
        "prime": my_map["prime"],
        "capacity": nueva_capacidad,
        "scale": random.randint(1, my_map["prime"] - 1),
        "shift": random.randint(0, my_map["prime"] - 1),
        "table": nueva_tabla,
        "current_factor": 0,
        "limit_factor": my_map["limit_factor"],
        "size": 0,
        "type": "CHAINING_HASH_MAP"
    }

    
    for i in range(sl.size(my_map["table"])):
        bucket = sl.get_element(my_map["table"], i)
        for j in range(sl.size(bucket)):
            entry = sl.get_element(bucket, j)
            if entry is not None:
                put(nuevo_mapa, entry["key"], entry["value"])

    return nuevo_mapa


            
    