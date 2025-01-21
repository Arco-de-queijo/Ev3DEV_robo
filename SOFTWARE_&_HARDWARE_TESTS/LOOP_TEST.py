#!/usr/bin/env python3
import time
from debug_print_function import debug_print

START = time.time()
counter = 0

while ((time.time() - START) <= 60):

    counter = counter + 1

debug_print("60 SEGUNDOS, ", counter," LOOPS")
