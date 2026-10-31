# sop_tareita_herbas
Respuesta de preguntas
¿Por qué queue.Queue es apropiada para compartir trabajos?
Porque permite que varios trabajadores accedan a una misma cola de forma segura, cada documento es retirado por un solo trabajador evitando que se procese dos veces.

¿Qué protege Lock y qué pasaría si se actualizara el resumen sin él?
Protege el diccionario de resultados y registro compartido, sin el bloqueo varios hilos podrían modificar los datos al mismo tiempo y provocar condiciones de carrera.

¿Qué cambiarías si cada documento tuviera que guardarse en un archivo real?
La simulación con time.sleep() por operaciones reales de lectura, procesamiento y escritura. Tambien controles para evitar que el programa se detenga si ocurre algún error con el archivo.