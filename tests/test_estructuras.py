# pruebas de pila, cola y tabla hash
import unittest

from estructuras import Pila, Cola, TablaHash


class TestPila(unittest.TestCase):
    def test_pila_nueva_esta_vacia(self):
        p = Pila()
        self.assertTrue(p.is_empty())
        self.assertEqual(p.size(), 0)

    def test_push_y_pop_lifo(self):
        p = Pila()
        for x in [1, 2, 3]:
            p.push(x)
        self.assertEqual([p.pop(), p.pop(), p.pop()], [3, 2, 1])

    def test_peek_no_saca(self):
        p = Pila()
        p.push("a")
        p.push("b")
        self.assertEqual(p.peek(), "b")
        self.assertEqual(p.size(), 2)

    def test_pop_pila_vacia(self):
        with self.assertRaises(IndexError):
            Pila().pop()

    def test_peek_pila_vacia(self):
        with self.assertRaises(IndexError):
            Pila().peek()

    def test_un_solo_elemento(self):
        p = Pila()
        p.push(7)
        self.assertEqual(p.pop(), 7)
        self.assertTrue(p.is_empty())

    def test_clear(self):
        p = Pila()
        p.push(1)
        p.push(2)
        p.clear()
        self.assertTrue(p.is_empty())
        self.assertEqual(len(p), 0)

    def test_muchos_elementos(self):
        p = Pila()
        for i in range(10000):
            p.push(i)
        self.assertEqual(len(p), 10000)
        self.assertEqual(p.pop(), 9999)
        self.assertEqual(p.peek(), 9998)

    def test_iteracion_tope_a_fondo(self):
        p = Pila()
        for x in [1, 2, 3]:
            p.push(x)
        self.assertEqual(list(p), [3, 2, 1])

    def test_acepta_none_y_tipos_mezclados(self):
        p = Pila()
        p.push(None)
        p.push("x")
        self.assertEqual(p.pop(), "x")
        self.assertIsNone(p.pop())
        self.assertTrue(p.is_empty())

    def test_repr(self):
        p = Pila()
        p.push(1)
        self.assertIn("1", repr(p))


class TestCola(unittest.TestCase):
    def test_cola_nueva_esta_vacia(self):
        c = Cola()
        self.assertTrue(c.is_empty())
        self.assertEqual(c.size(), 0)

    def test_enqueue_y_dequeue_fifo(self):
        c = Cola()
        for x in [1, 2, 3]:
            c.enqueue(x)
        self.assertEqual([c.dequeue(), c.dequeue(), c.dequeue()], [1, 2, 3])

    def test_front_y_peek_no_sacan(self):
        c = Cola()
        c.enqueue("a")
        c.enqueue("b")
        self.assertEqual(c.front(), "a")
        self.assertEqual(c.peek(), "a")
        self.assertEqual(c.size(), 2)

    def test_dequeue_cola_vacia(self):
        with self.assertRaises(IndexError):
            Cola().dequeue()

    def test_front_cola_vacia(self):
        with self.assertRaises(IndexError):
            Cola().front()

    def test_un_solo_elemento(self):
        c = Cola()
        c.enqueue(5)
        self.assertEqual(c.dequeue(), 5)
        self.assertTrue(c.is_empty())

    def test_vaciar_y_volver_a_usar(self):
        # al quedar vacia los punteros se reinician
        c = Cola()
        c.enqueue(1)
        c.dequeue()
        c.enqueue(2)
        c.enqueue(3)
        self.assertEqual(list(c), [2, 3])
        self.assertEqual(c.dequeue(), 2)

    def test_clear(self):
        c = Cola()
        c.enqueue(1)
        c.enqueue(2)
        c.clear()
        self.assertTrue(c.is_empty())
        c.enqueue(9)
        self.assertEqual(c.front(), 9)

    def test_muchos_elementos(self):
        c = Cola()
        for i in range(10000):
            c.enqueue(i)
        self.assertEqual(len(c), 10000)
        self.assertEqual(c.dequeue(), 0)
        self.assertEqual(c.front(), 1)

    def test_iteracion_en_orden_de_salida(self):
        c = Cola()
        for x in "abc":
            c.enqueue(x)
        self.assertEqual(list(c), ["a", "b", "c"])
        self.assertEqual(len(c), 3)

    def test_intercalar_enqueue_y_dequeue(self):
        c = Cola()
        c.enqueue(1)
        c.enqueue(2)
        self.assertEqual(c.dequeue(), 1)
        c.enqueue(3)
        self.assertEqual(list(c), [2, 3])

    def test_repr(self):
        c = Cola()
        c.enqueue(1)
        self.assertIn("1", repr(c))


class TestTablaHash(unittest.TestCase):
    def test_tabla_nueva_esta_vacia(self):
        t = TablaHash()
        self.assertEqual(len(t), 0)
        self.assertEqual(t.keys(), [])

    def test_put_y_get(self):
        t = TablaHash()
        t.put("a", 1)
        t.put("b", 2)
        self.assertEqual(t.get("a"), 1)
        self.assertEqual(t.get("b"), 2)
        self.assertEqual(t.size(), 2)

    def test_insert_es_igual_que_put(self):
        t = TablaHash()
        t.insert("a", 1)
        self.assertEqual(t["a"], 1)

    def test_get_con_default(self):
        t = TablaHash()
        self.assertIsNone(t.get("x"))
        self.assertEqual(t.get("x", 42), 42)

    def test_getitem_llave_inexistente(self):
        with self.assertRaises(KeyError):
            TablaHash()["nada"]

    def test_sobrescribir_llave(self):
        t = TablaHash()
        t.put("a", 1)
        t.put("a", 2)
        self.assertEqual(t.get("a"), 2)
        self.assertEqual(len(t), 1)
        self.assertEqual(t.keys(), ["a"])

    def test_remove_regresa_valor(self):
        t = TablaHash()
        t.put("a", 1)
        self.assertEqual(t.remove("a"), 1)
        self.assertNotIn("a", t)
        self.assertEqual(len(t), 0)

    def test_remove_llave_inexistente(self):
        with self.assertRaises(KeyError):
            TablaHash().remove("x")

    def test_delete_y_delitem(self):
        t = TablaHash()
        t["a"] = 1
        t["b"] = 2
        t.delete("a")
        del t["b"]
        self.assertEqual(len(t), 0)

    def test_borrar_y_reinsertar(self):
        t = TablaHash()
        t.put("a", 1)
        t.put("b", 2)
        t.remove("a")
        t.put("a", 3)
        self.assertEqual(t.get("a"), 3)
        # la llave reinsertada queda al final
        self.assertEqual(t.keys(), ["b", "a"])

    def test_contains(self):
        t = TablaHash()
        t.put("a", None)
        self.assertTrue(t.contains("a"))
        self.assertIn("a", t)
        self.assertNotIn("b", t)

    def test_setitem_getitem(self):
        t = TablaHash()
        t["x"] = 10
        self.assertEqual(t["x"], 10)

    def test_orden_de_insercion(self):
        t = TablaHash()
        llaves = ["z", "a", "m", "b", "y"]
        for i, k in enumerate(llaves):
            t.put(k, i)
        self.assertEqual(t.keys(), llaves)
        self.assertEqual(t.values(), [0, 1, 2, 3, 4])
        self.assertEqual(t.items(), list(zip(llaves, range(5))))

    def test_sobrescribir_no_cambia_el_orden(self):
        t = TablaHash()
        t.put("a", 1)
        t.put("b", 2)
        t.put("a", 99)
        self.assertEqual(t.keys(), ["a", "b"])

    def test_orden_al_borrar_en_medio(self):
        t = TablaHash()
        for k in "abcde":
            t.put(k, k)
        t.remove("c")
        t.remove("a")
        t.remove("e")
        self.assertEqual(t.keys(), ["b", "d"])

    def test_iteracion(self):
        t = TablaHash()
        for k in ["uno", "dos", "tres"]:
            t.put(k, len(k))
        self.assertEqual(list(t), ["uno", "dos", "tres"])

    def test_muchos_elementos_con_resize(self):
        t = TablaHash(capacidad=2)
        for i in range(1000):
            t.put("k" + str(i), i)
        self.assertEqual(len(t), 1000)
        # el factor de carga se mantiene bajo
        self.assertLessEqual(len(t) / len(t._cubetas), TablaHash.FACTOR_MAX)
        self.assertGreater(len(t._cubetas), 2)
        for i in range(1000):
            self.assertEqual(t.get("k" + str(i)), i)
        self.assertEqual(t.keys(), ["k" + str(i) for i in range(1000)])

    def test_colisiones_misma_cubeta(self):
        # hash constante: todas las llaves chocan
        t = TablaHash(funcion_hash=lambda k: 1)
        for i in range(30):
            t.put("k" + str(i), i)
        self.assertEqual(len(t), 30)
        for i in range(30):
            self.assertEqual(t["k" + str(i)], i)
        t.remove("k10")
        self.assertNotIn("k10", t)
        self.assertEqual(t["k11"], 11)
        t.put("k5", "nuevo")
        self.assertEqual(t["k5"], "nuevo")
        self.assertEqual(len(t), 29)

    def test_distintos_tipos_de_llave(self):
        t = TablaHash()
        t.put(1, "int")
        t.put("1", "str")
        t.put((1, 2), "tupla")
        t.put(2.5, "float")
        self.assertEqual(t[1], "int")
        self.assertEqual(t["1"], "str")
        self.assertEqual(t[(1, 2)], "tupla")
        self.assertEqual(t[2.5], "float")

    def test_resize_despues_de_borrar(self):
        t = TablaHash(capacidad=2)
        for i in range(50):
            t.put(i, i)
        for i in range(0, 50, 2):
            t.remove(i)
        self.assertEqual(t.keys(), list(range(1, 50, 2)))
        for i in range(50, 100):
            t.put(i, i)
        self.assertEqual(len(t), 75)
        self.assertEqual(t.get(99), 99)

    def test_clear(self):
        t = TablaHash()
        t.put("a", 1)
        t.clear()
        self.assertEqual(len(t), 0)
        self.assertNotIn("a", t)
        t.put("b", 2)
        self.assertEqual(t.keys(), ["b"])

    def test_capacidad_invalida(self):
        with self.assertRaises(ValueError):
            TablaHash(capacidad=0)

    def test_repr(self):
        t = TablaHash()
        t.put("a", 1)
        self.assertEqual(repr(t), "TablaHash({'a': 1})")


if __name__ == "__main__":
    unittest.main()
