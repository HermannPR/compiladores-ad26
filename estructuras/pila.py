# pila (LIFO): push, pop, peek, is_empty, size, clear
class Pila:
    def __init__(self):
        # lista de python, el tope es el ultimo elemento
        self._datos = []

    # mete un elemento arriba de la pila
    def push(self, x):
        self._datos.append(x)

    # saca y regresa el de arriba, error si esta vacia
    def pop(self):
        if not self._datos:
            raise IndexError("pop sobre una pila vacia")
        return self._datos.pop()

    # regresa el de arriba sin sacarlo
    def peek(self):
        if not self._datos:
            raise IndexError("peek sobre una pila vacia")
        return self._datos[-1]

    # true si no tiene elementos
    def is_empty(self):
        return len(self._datos) == 0

    # cuantos elementos hay
    def size(self):
        return len(self._datos)

    # vacia la pila
    def clear(self):
        self._datos = []

    def __len__(self):
        return self.size()

    # recorre del tope hacia el fondo (orden en que saldrian)
    def __iter__(self):
        for i in range(len(self._datos) - 1, -1, -1):
            yield self._datos[i]

    def __repr__(self):
        return "Pila(fondo -> tope: " + repr(self._datos) + ")"
