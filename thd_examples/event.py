import threading
import time

def myThread(myEvent):
    while not myEvent.is_set():
        print("Waiting for Event to be set")
        time.sleep(1)
    print("myEvent has been set")

def main():
    myEvent = threading.Event()
    thread1 = threading.Thread(target=myThread, args=(myEvent,))
    thread1.start()
    time.sleep(10)
    myEvent.set()
    # Mimo że nie ma tego co pod spodem, aplikacja skończy się prawidłowo
    #thread1.join()


if __name__ == '__main__':
    main()
