class Tarea:
    """ Representa una tarea y almacena todos sus datos"""
    def __init__(self, nombre:str, prioridad:str = None, fecha_limite:str = None, etiqueta:str = None) -> None:
        """Iniciamos una nueva tarea. El nombre es obligatorio y el resto son datos opcionales"""
        self.nombre = nombre
        self.prioridad = prioridad
        self.fecha_limite = fecha_limite
        self.etiqueta = etiqueta




