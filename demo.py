# demo de las estructuras con ejemplos tipo compiladores
from estructuras import Pila, Cola, TablaHash


# 1) pila: revisar parentesis balanceados
def balanceado(texto):
    pares = {")": "(", "]": "[", "}": "{"}
    pila = Pila()
    for c in texto:
        if c in "([{":
            pila.push(c)
        elif c in ")]}":
            if pila.is_empty() or pila.pop() != pares[c]:
                return False
    return pila.is_empty()


def demo_pila():
    print("=== PILA: parentesis balanceados ===")
    for t in ["(a + b) * [c - d]", "{(a + b) * c}", "((a + b)", "(a + b]", ")("]:
        print("  %-22s -> %s" % (t, "balanceado" if balanceado(t) else "NO balanceado"))
    p = Pila()
    for x in [1, 2, 3]:
        p.push(x)
    print("  pila:", p, "tope:", p.peek(), "tam:", len(p))
    print("  pop:", p.pop(), "-> queda:", p)


# 2) cola: tokens de una expresion simple
def tokenizar(texto):
    cola = Cola()
    i = 0
    while i < len(texto):
        c = texto[i]
        if c.isspace():
            i += 1
        elif c.isdigit():
            j = i
            while j < len(texto) and texto[j].isdigit():
                j += 1
            cola.enqueue(("NUM", texto[i:j]))
            i = j
        elif c.isalpha():
            j = i
            while j < len(texto) and texto[j].isalnum():
                j += 1
            cola.enqueue(("ID", texto[i:j]))
            i = j
        else:
            cola.enqueue(("OP", c))
            i += 1
    return cola


def demo_cola():
    print("\n=== COLA: tokens de una expresion ===")
    expr = "x = 3 + y1 * (42 - z)"
    print("  expresion:", expr)
    tokens = tokenizar(expr)
    print("  tokens en cola:", len(tokens), "primero:", tokens.front())
    while not tokens.is_empty():
        tipo, valor = tokens.dequeue()
        print("   ", tipo, valor)
    print("  cola vacia:", tokens.is_empty())


# 3) tabla hash: tabla de simbolos
def demo_tabla():
    print("\n=== TABLA HASH: tabla de simbolos ===")
    simbolos = TablaHash()
    simbolos.put("x", {"tipo": "int", "valor": 10})
    simbolos.put("nombre", {"tipo": "string", "valor": "Hermann"})
    simbolos.put("pi", {"tipo": "float", "valor": 3.1416})
    simbolos["activo"] = {"tipo": "bool", "valor": True}
    print("  declaradas:", simbolos.keys())
    print("  busco x:", simbolos.get("x"))
    print("  busco z (no existe):", simbolos.get("z", "no declarada"))
    print("  'pi' in tabla:", "pi" in simbolos)
    simbolos["x"] = {"tipo": "int", "valor": 99}
    print("  actualizo x:", simbolos["x"])
    simbolos.remove("nombre")
    print("  borro nombre, quedan:", simbolos.keys(), "tam:", len(simbolos))
    try:
        simbolos["nombre"]
    except KeyError:
        print("  nombre ya no existe (KeyError)")
    print("  tabla completa:")
    for llave, info in simbolos.items():
        print("    %-7s %s" % (llave, info))
    # muchas entradas para que haga rehash
    grande = TablaHash()
    for i in range(100):
        grande.put("var" + str(i), i)
    print("  100 variables insertadas, tam:", len(grande),
          "primeras llaves:", grande.keys()[:3])


if __name__ == "__main__":
    demo_pila()
    demo_cola()
    demo_tabla()
