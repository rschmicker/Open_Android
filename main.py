import subprocess
from controller import *
import threading
import time
import variables
import os
import sys
from multiprocessing.dummy import Pool as ThreadPool
	
def main():
	c = controller()

#sys.stdout = open("output.txt", "w")
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))