from pytube import YouTube
from multiprocessing import Process, Value
import threading
import time

response = Value('i', 0)

def descargar( res ):
    t=threading.current_thread()
    if (stream.download('./videos')):
        res.value+=1
    else:
        res.value= -1
        print ("Descarga fallida")

def porcentaje(res):
    t=threading.current_thread()
    while (1):
        if (res.value == 0):
            print('Descargando', end="")
            time.sleep(0.5)
            print('.', end="", flush=True)
            time.sleep(0.5)
            print('.', end="", flush=True)
            time.sleep(0.5)
            print('.', end="", flush=True)
            time.sleep(0.5)
            print('.', end="\r", flush=True)
            print('                          ', end="\r", flush=True)
        else:
            print('Descarga completada')
            break
            
t1 = threading.Thread(name="hilo_descarga", target=descargar, args = (response,))
t2 = threading.Thread(name="hilo_carga", target=porcentaje, args = (response,))

url = input("Introduce Url del video: ")
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()

t1.start()
t2.start()

t1.join()
t2.join()

