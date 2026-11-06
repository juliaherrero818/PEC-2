from app import modelos

lista_tareas = []

def añadir_tarea(nombre:str, **kwargs) -> list:
    """Creamos la función para que el usuario pueda añadir la tarea y otra información que desee (prioridad, fecha límite, etiqueta)"""
    tarea: modelos.Tarea = modelos.Tarea(nombre, **kwargs)
    lista_tareas.append(tarea)
    return lista_tareas

def mostrar_lista() -> list:
    """Devuelve la lista completa con todas las tareas"""
    return lista_tareas

def buscar_tarea(texto:str) -> modelos.Tarea | None:
    """Busca la tarea en la lista y compara el texto introducido por el usuario con el nombre de la tarea"""
    for tarea in lista_tareas:
        if texto.lower() in tarea.nombre.lower():
            return tarea
    return None


    