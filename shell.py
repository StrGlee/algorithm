def shell_sort(lists):
    # 希尔排序
    count = len(lists)
    step = 2
    group = count // step
    print(group)
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        print(lists[k],key)
                        lists[k] = key
                    else:
                        print('----',lists[k],key)
                    k -= group
                    print(group)
                print(lists)
                j += group
        group //= step
        print(step,group)
    return lists

def main():
    arr = [661, 10, 666, 511, 20, 555, 444, ]
    print(arr)
    shell_sort(arr)
    print(arr)

if __name__ == '__main__':
    main()
