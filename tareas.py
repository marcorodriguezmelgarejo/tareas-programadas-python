import sched
import time
import threading

scheduler = sched.scheduler(timefunc=time.time, delayfunc=time.sleep)

def tirar_error():
    raise Exception('Se te acabo el tiempo, moriste.')

def insertar_contrasenia_15s():
    limite = scheduler.enter(5, 1, tirar_error)
    # crea un hilo para correr el scheduler ahi
    hilo_tirar_error = threading.Thread(target=scheduler.run)
    # comienza a ejecutar el hilo
    hilo_tirar_error.start()
    contra = int(input('Cual es la contraseña? --> '))
    while (contra != 1234):
        print('Contraseña incorrecta, intente de nuevo.')
        contra = int(input('Cual es la contraseña? --> '))
    # cierra el scheduler
    scheduler.cancel(limite)
    # cierra el hilo
    hilo_tirar_error.join()
    print('Te salvaste.')

insertar_contrasenia_15s()