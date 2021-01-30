import random
import time

def is_sorted(vec):
    for x in range(0, len(vec)-1):
        if (vec[x] > vec[x+1]):
            return False
    return True

def shuffle_sort(vec):
    while (True):
        random.shuffle(vec)
        if (is_sorted(vec)):
            return vec

def brilliant_sort(vec):
    while (True):
        x = random.randint(0, len(vec)-1)
        vec.append(vec.pop(x))
        if (is_sorted(vec)):
            return vec

def main():
    vec = [0, 1]
    for i in range(2, 10):
        vec.append(i)
        f = open(("data_" + str(i+1) + "_shuffle.txt"), "w") 
        whole_time = time.time()
        for x in range(1000):
            random.shuffle(vec)
            if (x % 25 == 0):
                print(x, i+1)
            start_time = time.time()
            shuffle_sort(vec)
            f.write(str(time.time() - start_time) + " seconds\n")
        f.write("Average time: " + str((time.time()-whole_time)/1000) + " Seconds             Total time: " + str((time.time()-whole_time)) + " Seconds\n")
        f.close()

main()