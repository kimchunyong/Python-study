# age = input('당신의 나이는?')
# print(age)
import random
my_int = 1
print(my_int)
print(type(1))


my_list = []

my_list = [1, 2, 3]
print(my_list)

for list in my_list:
    print(list)

print(random.choice(my_list))

my_list.append('5')

print(my_list)

# 튜플

my_tuple = ('요거트', '이에스', '레이')

# my_tuple[0] = '소나타

print(my_tuple)

my_dict = {'헤흐': '남', 'Meta': '남', '김왼손': '여'}

print(my_dict['김왼손'])

print(int('33'))

my_str = """김씨가족
토미
메타"""

print(my_str)

print(type(my_str))

# 포멧팅

my_str = 'My name is %s' % 'Young Choi'  # %s 는 문자열

print(my_str)

print('%d %d' % (1, 2))  # 정수 여러개일 경우 괄호 사용


print('%f' % 3.14)  # 실수


# {} format();

# test = 'My name is {}'.format('조희진')

# print(test)


# gugudan = '{} x {} = {}'.format(2, 3, 2*3)

# print(gugudan)

# gugudan2 = '{1} x {0} = {2}'.format(2, 3, 2*3)

# print(gugudan2)

# 인덱싱

my_name = "김왼손의 왼손코딩"

print(my_name[3])  # '의'
print(my_name[-1])

fruits_str = '거봉,수박,사과,배,딸기'

fruits_arr = fruits_str.split(',')

print(fruits_arr)  # ['거봉', '수박', '사과', '배', '딸기']


my_list = []

print(type(my_list))


my_list = [1, 2, 3]

print(my_list)


my_list.append(5)

print(my_list)

animals = []

animals.append('코알라')
animals.append('하이에나')
animals.append('바다소')
animals.append('땅다람쥐')

print(animals, end="\n")

print(len(animals))

my_tuple = 1, 2, 3

print(my_tuple)


num1, num2, num3 = my_tuple

print(num1)
print(num2)
print(num3)

num1, num2 = num2, num1

print(num1)
print(num2)


for a in [1, 2, 3, 4]:
    print(a)
    print(a + 2)


for test in range(10):
    print(test)

for j in range(2, 10):
    for i in range(1, 10):
        print('{}x{}={}'.format(j, i, j*i))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = []

for num in numbers:
    if num % 2 == 1:
        odd_numbers.append(num)

print(odd_numbers)


print([number for number in numbers if number % 2 == 1])


member = ['가', '나', '다', '라', '마', '바', '사']

print(member)

print('가' in member)

my_dict = {'학생1': '호박', '학생2': 'kim', '학생3': 'lee'}

for std in my_dict.values():
    print(std)


for key in my_dict.keys():
    print(key)


for key, val in my_dict.items():
    print(key, val)


def add(num1, num2):
    return num1 + num2


print(add(1, 2))


students = ['망고', '배', '사과', '딸기', '포도']


print(random.choice(students))

print(random.sample(students, 2))
