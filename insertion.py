def InsertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            print('----',A[i+1], key)
            i = i-1
        A[i+1] = key
        print(A)

def InsertionSort2(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            print('----',A[i+1], key)
            i = i-1
        A[i+1] = key
        print(A)

def main():
    A = [10, 2, 12, 3, 4]
    print(A)
    InsertionSort(A)
    print(A)

if __name__ == '__main__':
    main()
