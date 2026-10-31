## Respuesta de preguntas

**¿Por qué queue.Queue es apropiada para compartir trabajos?**

Porque permite que varios trabajadores accedan a una misma cola de forma segura, cada documento es retirado por un solo trabajador evitando que se procese dos veces.

**¿Qué protege Lock y qué pasaría si se actualizara el resumen sin él?**

Protege el diccionario de resultados y registro compartido, sin el bloqueo varios hilos podrían modificar los datos al mismo tiempo y provocar condiciones de carrera.

**¿Qué cambiarías si cada documento tuviera que guardarse en un archivo real?**

La simulación con time.sleep() por operaciones reales de lectura, procesamiento y escritura. Tambien controles para evitar que el programa se detenga si ocurre algún error con el archivo.

## Interpretación de los trabajadores

Cada trabajador representa un hilo que procesa documentos de una cola compartida.

**1. Candia**

Representa el 1er hilo. Retira documentos de la cola compartida, los procesa y registra cada documento terminado. Cuando finaliza un documento, puede retirar otro que todavía esté pendiente.

**2. Poma**

Representa el 2do hilo. Trabaja concurrentemente con los demás trabajadores, retirando y procesando documentos disponibles. Registra sus resultados utilizando el mecanismo de sincronización Lock.

**3. Siles**

Representa el 3er hilo. Procesa los documentos que obtiene de la cola compartida. Su cantidad de documentos procesados depende del tiempo que tarde en completar cada uno.

**4. Figueredo**

Representa el 4to hilo. Participa en el procesamiento concurrente y continúa retirando documentos mientras existan trabajos pendientes en la cola.

### Interpretación general

Los cuatro trabajadores procesan los 24 documentos de manera concurrente. No necesariamente reciben la misma cantidad, porque cada documento tiene un tiempo de procesamiento diferente.

Cuando un trabajador termina antes, puede retirar otro documento pendiente. El uso de queue.Queue evita que dos trabajadores retiren el mismo documento, mientras que Lock protege la actualización de los resultados compartidos.

Al finalizar, se comprueba que los 24 documentos hayan sido procesados una sola vez y que todos los trabajadores hayan terminado correctamente.