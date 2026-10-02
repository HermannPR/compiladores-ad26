# cola (FIFO): enqueue, dequeue, front/peek, is_empty, size, clear
# esta hecha con lista ligada, con punta al primero y al ultimo
class _Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class Cola:
    def __init__(self):
        self._primero = None
        self._ultimo = None
        self._tam = 0

    # agrega al final de la cola
    def enqueue(self, x):
        nodo = _Nodo(x)
        if self._ultimo is None:
            self._primero = nodo
        else:
            self._ultimo.siguiente = nodo
        self._ultimo = nodo
        self._tam += 1

    # saca y regresa el primero, error si esta vacia
    def dequeue(self):
        if self._primero is None:
            raise IndexError("dequeue sobre una cola vacia")
        nodo = self._primero
        self._primero = nodo.siguiente
        if self._primero is None:
            self._ultimo = None
        self._tam -= 1
        return nodo.valor

    # regresa el primero sin sacarlo
    def front(self):
        if self._primero is None:
            raise IndexError("front sobre una cola vacia")
        return self._primero.valor

    # igual que front
    def peek(self):
        return self.front()

    # true si no tiene elementos
    def is_empty(self):
        return self._tam == 0

    # cuantos elementos hay
    def size(self):
        return self._tam

    # vacia la cola
    def clear(self):
        self._primero = None
        self._ultimo = None
        self._tam = 0

    def __len__(self):
        return self._tam

    # recorre del primero al ultimo (orden de salida)
    def __iter__(self):
        actual = self._primero
        while actual is not None:
            yield actual.valor
            actual = actual.siguiente

    def __repr__(self):
        return "Cola(frente -> final: " + repr(list(self)) + ")"
