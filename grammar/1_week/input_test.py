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
