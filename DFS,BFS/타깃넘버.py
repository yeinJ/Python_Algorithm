def find_answer(sum_num, i):
    global count
    if sum_num == target and i == len(numbers):
        count += 1
        return
    elif i >= len(numbers):
        return
    else:
        k = numbers[i]
        find_answer(sum_num + k, i + 1)
        find_answer(sum_num - k, i + 1)


count = 0
numbers=[1,1,1,1,1]
target = 3
find_answer(0, 0)
print(count)