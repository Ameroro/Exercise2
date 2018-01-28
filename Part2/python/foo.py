# Python 3.3.3 and 2.7.6
# python fo.py

from threading import Thread
import threading

# Potentially useful thing:
#   In Python you "import" a global variable, instead of "export"ing it when you declare it
#   (This is probably an effort to make you feel bad about typing the word "global")
i = 0

def incrementingFunction(sack_lock):
	global i
	with sack_lock: 
	    for j in range(0,100001):
	    	i += 1
    # TODO: increment i 1_000_000 times

def decrementingFunction(sack_lock):
	global i
	with sack_lock: 
	    for j in range(0,100000):
	    	i -= 1
    # TODO: decrement i 1_000_000 times



def main():
    global i
    sack_lock = threading.Lock() 

    incrementing = Thread(target = incrementingFunction, args = (sack_lock,),)
    decrementing = Thread(target = decrementingFunction, args = (sack_lock,),)
    
    # TODO: Start both threads
    incrementing.start()
    decrementing.start()
    
    incrementing.join()
    decrementing.join()
    
    print("The magic number is %d" % (i))


main()
