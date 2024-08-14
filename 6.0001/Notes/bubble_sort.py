def bubble_sort(L):
    swap = True
    while  swap:
        swap = False
        for j in range(1, len(L)):
            if L[j] < L[j-1]:
                swap = True
                L[j], L[j-1] = L[j-1], L[j]
    return L

if __name__ == "__main__":
    print(bubble_sort([i for i in range(10,0,-1)])) 