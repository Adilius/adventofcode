input_file = open('input.txt', 'r')
input_list = input_file.read().split('\n')

def most_common(lst):
    return str(max(set(lst), key=lst.count))

matrix = [[]for _ in range(12)]

for row in input_list:
    for index, column in enumerate(row):
        matrix[index].append(int(column))

bit_string = ""
bit_string_flipped = ""

for column in matrix:
    bit_string += most_common(column)

bit_string_flipped = ''.join('1' if x == '0' else '0' for x in bit_string)
gamma_rate = int(bit_string,2)
epsilon_rate = int(bit_string_flipped,2)
power_comsumption = gamma_rate * epsilon_rate
print(f'Power consumption: {power_comsumption}')
