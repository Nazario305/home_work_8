
def find_unique_value(some_list):
    unique_list = []
    for i in some_list:
       count_i = some_list.count(i)
       if count_i < 2:
           unique_list.append(i)

    # print(unique_list)
    return unique_list[0]

assert find_unique_value([5, 1, 2, 1, 1]) == 5, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
