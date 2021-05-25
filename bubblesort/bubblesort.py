def bubble_sort(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list) - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

my_list = [90,17,34,1,0,-40,57,40,-1,66]
bubble_sort(my_list)
print(my_list)