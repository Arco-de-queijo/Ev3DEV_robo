import time

START = time.time()
counter = 0

while ((time.time() - START) <= 60):

    counter = counter + 1

print("60 SEGUNDOS, ", counter," LOOPS")
