# tabla hash / diccionario: put, get, remove, contains, keys, values, items, size
# encadenamiento separado (cada cubeta es una lista de nodos), con rehash
# y los nodos tambien van en una lista doble para guardar el orden de insercion
class _Nodo:
    def __init__(self, llave, valor, hash_):
        self.llave = llave
        self.valor = valor
        self.hash = hash_
        self.ant = None   # anterior en orden de insercion
        self.sig = None   # siguiente en orden de insercion


class TablaHash:
    FACTOR_MAX = 0.75

    def __init__(self, capacidad=8, funcion_hash=None):
        if capacidad < 1:
            raise ValueError("la capacidad debe ser al menos 1")
        # funcion_hash se puede cambiar para probar colisiones
        self._f = funcion_hash if funcion_hash is not None else hash
        self._capacidad_inicial = capacidad
        self._cubetas = [[] for _ in range(capacidad)]
        self._tam = 0
        self._cabeza = None
        self._cola = None

    # indice de cubeta de un hash
    def _indice(self, h):
        return h % len(self._cubetas)

    # busca el nodo de una llave, None si no esta
    def _buscar(self, llave):
        h = self._f(llave)
        for nodo in self._cubetas[self._indice(h)]:
            if nodo.hash == h and nodo.llave == llave:
                return nodo
        return None

    # duplica las cubetas y vuelve a repartir todos los nodos
    def _rehash(self):
        self._cubetas = [[] for _ in range(len(self._cubetas) * 2)]
        nodo = self._cabeza
        while nodo is not None:
            self._cubetas[self._indice(nodo.hash)].append(nodo)
            nodo = nodo.sig

    # recorre los nodos en orden de insercion
    def _nodos(self):
        nodo = self._cabeza
        while nodo is not None:
            yield nodo
            nodo = nodo.sig

    # inserta una llave nueva o cambia el valor si ya existe
    def put(self, llave, valor):
        nodo = self._buscar(llave)
        if nodo is not None:
            nodo.valor = valor
            return
        h = self._f(llave)
        nodo = _Nodo(llave, valor, h)
        self._cubetas[self._indice(h)].append(nodo)
        # al final de la lista de orden
        if self._cola is None:
            self._cabeza = nodo
        else:
            self._cola.sig = nodo
            nodo.ant = self._cola
        self._cola = nodo
        self._tam += 1
        if self._tam / len(self._cubetas) > self.FACTOR_MAX:
            self._rehash()

    # igual que put
    def insert(self, llave, valor):
        self.put(llave, valor)

    # regresa el valor de la llave o default si no existe
    def get(self, llave, default=None):
        nodo = self._buscar(llave)
        return default if nodo is None else nodo.valor

    # quita la llave y regresa su valor, KeyError si no existe
    def remove(self, llave):
        h = self._f(llave)
        cubeta = self._cubetas[self._indice(h)]
        for i, nodo in enumerate(cubeta):
            if nodo.hash == h and nodo.llave == llave:
                del cubeta[i]
                # sacarlo de la lista de orden
                if nodo.ant is None:
                    self._cabeza = nodo.sig
                else:
                    nodo.ant.sig = nodo.sig
                if nodo.sig is None:
                    self._cola = nodo.ant
                else:
                    nodo.sig.ant = nodo.ant
                self._tam -= 1
                return nodo.valor
        raise KeyError(llave)

    # igual que remove
    def delete(self, llave):
        return self.remove(llave)

    # true si la llave existe
    def contains(self, llave):
        return self._buscar(llave) is not None

    def __contains__(self, llave):
        return self.contains(llave)

    # llaves en orden de insercion
    def keys(self):
        return [n.llave for n in self._nodos()]

    # valores en orden de insercion
    def values(self):
        return [n.valor for n in self._nodos()]

    # pares (llave, valor) en orden de insercion
    def items(self):
        return [(n.llave, n.valor) for n in self._nodos()]

    # cuantas llaves hay
    def size(self):
        return self._tam

    # vacia la tabla
    def clear(self):
        self._cubetas = [[] for _ in range(self._capacidad_inicial)]
        self._tam = 0
        self._cabeza = None
        self._cola = None

    def __len__(self):
        return self._tam

    def __getitem__(self, llave):
        nodo = self._buscar(llave)
        if nodo is None:
            raise KeyError(llave)
        return nodo.valor

    def __setitem__(self, llave, valor):
        self.put(llave, valor)

    def __delitem__(self, llave):
        self.remove(llave)

    # recorre las llaves en orden de insercion
    def __iter__(self):
        for n in self._nodos():
            yield n.llave

    def __repr__(self):
        pares = ", ".join(repr(k) + ": " + repr(v) for k, v in self.items())
        return "TablaHash({" + pares + "})"
