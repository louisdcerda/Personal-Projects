import time
import shutil
import os
import logging 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



home_dir = "/Users/louiscerda/Downloads"
dest_dir_cpp = "/Users/louiscerda/Desktop/Downloaded_C++_Files"
dest_dir_py = "/Users/louiscerda/Desktop/Downloaded_Python_Files"
dest_dir_img = "/Users/louiscerda/Desktop/Downloaded_Images"
dest_dir_pdf = "/Users/louiscerda/Desktop/Downloaded_PDFs"

def makeUniqueFileName(path):
    filename, extension = os.path.splitext(path)
    counter = 1
    ## IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while os.path.exists(path):
        path = filename + " (" + str(counter) + ")" + extension
        counter += 1

    return path



def move(dest, entry, name):
    # Moves the file to the destination directory
    file_exits = os.path.exists(dest+"/"+name)
    if file_exits:
        unique_name = makeUniqueFileName(name)
        os.rename(entry, unique_name)
    shutil.move(entry, dest)




class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(home_dir) as entries:
            for entry in entries: # Iterate through the files in the directory
                name = entry.name
                dest = home_dir
                if name.endswith(".cpp"): # If the file is a C++ file then move it to the C++ directory
                    dest = dest_dir_cpp
                    move(dest,entry,name)
                elif name.endswith(".py"):
                    dest = dest_dir_py
                    move(dest,entry,name)
                elif name.endswith(".jpg"):
                    dest = dest_dir_img
                    move(dest,entry,name)
                elif name.endswith(".pdf"):
                    dest = dest_dir_pdf
                    move(dest,entry,name)



 

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = home_dir
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()






