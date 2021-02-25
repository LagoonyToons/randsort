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
    vec = []
    for z in range(2,11):
        for y in range(0, 1000):
            tempvec = []
            for x in range(0,z):
                tempvec.append(random.randint(1,10))
            vec.append(tempvec)

    for i in range(2, 11):
        f = open(("data_" + str(i+1) + "_index_random.txt"), "w") 
        whole_time = time.time()
        for x in range(1000):
            if (x % 25 == 0):
                print(x, i)
            start_time = time.time()
            brilliant_sort(vec[x + (i*1000)])
            f.write(str(time.time() - start_time) + "\n")
        f.write("Average time: " + str((time.time()-whole_time)/1000) + " Seconds             Total time: " + str((time.time()-whole_time)) + " Seconds\n")
        f.close()

main()