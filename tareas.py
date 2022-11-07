import sched
import time

scheduler = sched.scheduler(timefunc=time.time, delayfunc=time.sleep)

def tirar_error():
    raise Exception('Se te acabo el tiempo, moriste.')

def insertar_contrasenia_15s():
    limite = scheduler.enter(5, 1, tirar_error)
    contra = int(input('Cual es la contraseña? --> '))
    scheduler.run()
    while (contra != 1234):
        print('Contraseña incorrecta, intente de nuevo.')
        contra = int(input('Cual es la contraseña? --> '))
    scheduler.cancel(limite)
    print('Te salvaste.')

insertar_contrasenia_15s()

# FUNCION DE HILOS
# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)


# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#     logging.info("Main    : before creating thread")
#     x = threading.Thread(target=thread_function, args=(1,))
#     logging.info("Main    : before running thread")
#     x.start()
#     logging.info("Main    : wait for the thread to finish")
#     # x.join()
#     logging.info("Main    : all done")