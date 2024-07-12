def es_sano(numero_calorias: int, es_vegetariano: bool) -> bool:
    if numero_calorias < 100 or es_vegetariano:
        return True
    else:
        return False

def contar_calorias(calorias: list) -> float:
    return round(sum(calorias) * 0.95, 2)

def calcular_costo(dict1: dict, dict2: dict, dict3: dict) -> float:
    return round(dict1["precio"] + dict2["precio"] + dict3["precio"], 2)

def calcular_rentabilidad(precio: float, ingrediente1: dict, ingrediente2: dict, ingrediente3: dict) -> float:
    costo_ingredientes = calcular_costo(ingrediente1, ingrediente2, ingrediente3)
    return round(precio - costo_ingredientes, 2)

def mejor_producto(producto1: dict, producto2: dict, producto3: dict, producto4: dict) -> str:
    productos = [producto1, producto2, producto3, producto4]
    producto_mas_rentable = max(productos, key=lambda x: x["rentabilidad"])
    return producto_mas_rentable["nombre"]




""" def es_sano(numero_calorias:int , es_vegetariano:bool)->bool:
    if(numero_calorias < 100 or es_vegetariano == True):
        return True
    else:
        return False

def contar_calorias(calorias:list)->float:
    sum = 0
    for caloria in calorias:
        sum += caloria
    return round(sum * 0.95 , 2)

def calcular_costo(dict1:dict , dict2:dict , dict3:dict)-> float:
    costoProductos = [dict1, dict2, dict3]
    sumaCosto =  0.0
    for cost in costoProductos:
        sumaCosto += cost["precio"]
    return round(sumaCosto, 2)

def calcular_rentabilidad(precio:float, ingrediente1:dict , ingrediente2:dict , ingrediente3:dict) -> float:
    costo_ingredientes = calcular_costo(ingrediente1, ingrediente2, ingrediente3)
    rentabilidad = precio  - costo_ingredientes
    return round(rentabilidad , 2) 

def mejor_producto(producto1:dict, producto2:dict , producto3:dict , producto4:dict)->str:
    productos = [producto1, producto2 , producto3, producto4]
    producto_mas_rentable = productos[0]

    for producto in productos[1:]:
        if(producto["rentabilidad"] > producto_mas_rentable["rentabilidad"]):
            producto_mas_rentable = producto
    
    return producto_mas_rentable["nombre"] """




