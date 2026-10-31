import threading
import queue
import time
import random

docs = queue.Queue()
resultados = {}
registro = []

# para proteger el registro y resumen compartido
lock = threading.Lock()

for doc_id in range(1, 25):
    tamano = random.randint(1, 5)
    docs.put((doc_id, tamano))

def trabajador(nombre):
    cantidad = 0

    while True:
        try:
            # obtener un documento, si esta vacia genera queue.Empty
            doc_id, tamano = docs.get_nowait()

        except queue.Empty:
            # no quedan documentos
            break

        tiempo_proceso = tamano * 0.1

        print(f" {nombre} comienza Documento {doc_id} ")

        time.sleep(tiempo_proceso)

        print(f" {nombre} termina Documento {doc_id} ")

        # proteger la actualizacion de los datos compartidos
        with lock:
            cantidad += 1
            resultados[nombre] = cantidad
            registro.append((doc_id, nombre))

        # indicar que el documento ya fue procesado
        docs.task_done()

def main():

    nombres = ["Candia", "Poma", "Siles", "Figueredo"]

    # contador de cada trabajador
    for nombre in nombres:
        resultados[nombre] = 0

    hilos = []

    for nombre in nombres:
        hilo = threading.Thread(
            target=trabajador,
            args=(nombre,)
        )
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    total = sum(resultados.values())

    # resumen final
    print("\n========== RESUMEN FINAL ==========")

    for nombre in nombres:
        print(f"{nombre}: {resultados[nombre]} documentos")

    print(f"\nTotal procesado: {total} de 24 documentos")

    # mostrar quien proceso cada documento
    print("\n========== REGISTRO ==========")

    for doc_id, nombre in sorted(registro):
        print(f"Documento {doc_id}: {nombre}")

    # verificación
    ids = [doc_id for doc_id, nombre in registro]

    print("\n========== VERIFICACION ==========")

    print("Total correcto:", total == 24)
    print("Sin documentos repetidos:", len(ids) == len(set(ids)))
    print("Todos los documentos procesados:", set(ids) == set(range(1, 25)))
    print("\n")
    
if __name__ == "__main__":
    main()