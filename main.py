import subprocess
from controller import *
import threading
import time
import variables
import os
from multiprocessing.dummy import Pool as ThreadPool
	
def main():
	c = controller()

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))