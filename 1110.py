first_num = int(input())
num_list = [0] * 4
count = 0
num_list[0] = first_num // 10
num_list[1] = first_num % 10

while True:
    count += 1
    num_list[3] = (num_list[0] + num_list[1]) % 10
    num_list[2] = num_list[1]
    if first_num == int(str(num_list[1]) + str(num_list[3])):
        break
    num_list[0] = num_list[2]
    num_list[1] = num_list[3]
print(count)