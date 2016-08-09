def build_max_heap(to_build_list):
    for i in range(len(to_build_list)//2-1, -1, -1):
        max_heap(to_build_list, len(to_build_list), i)

def max_heap(to_adjust_list, heap_size, index):
    left_child = 2 * index + 1
    right_child = left_child + 1

    if left_child < heap_size and to_adjust_list[left_child] > to_adjust_list[index]:
        largest = left_child
    else:
        largest = index

    if right_child < heap_size and to_adjust_list[right_child] > to_adjust_list[largest]:
        largest = right_child

    if largest != index:
        to_adjust_list[index] ,to_adjust_list[largest] = to_adjust_list[largest], to_adjust_list[index]
        max_heap(to_adjust_list, heap_size, largest)

def heap_sort(to_sort_list):

    build_max_heap(to_sort_list)
    # print(to_sort_list)

    heap_size = len(to_sort_list)

    for i in range(len(to_sort_list) - 1, 0, -1):
        to_sort_list[i], to_sort_list[0] = to_sort_list[0],to_sort_list[i]
        heap_size -= 1
        max_heap(to_sort_list,heap_size, 0)
if __name__ == '__main__':
    to_sort_list = []
    for x in range(2000000):
        to_sort_list.append(x)
    to_sort_list.reverse()
    heap_sort(to_sort_list)
    # print(to_sort_list)
    print('ok')
