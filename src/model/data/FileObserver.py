from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from src.model.data.PcDataHandler import *
import time


def on_created(event):
    print("created")

def on_deleted(event):
    print("deleted")

def on_modified(event):
   print("modified")

event_handler = FileSystemEventHandler()

#calling
event_handler.on_created = on_created
event_handler.on_deleted = on_deleted
event_handler.on_modified = on_modified

observer = Observer()
observer.schedule(event_handler, r"C:\Users\morit\OneDrive\Desktop\Datastructure", recursive= False)

observer.start()
try:
    while observer.is_alive():
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
