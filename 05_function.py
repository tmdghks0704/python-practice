#1.함수를 왜 써야 하는가?

'''height = 30
width = 20

area = height * width
perimeter = 2 * (height + width)
print(f'직사각형의 넓이는 {area}이고, 둘레는  {perimeter}입니다.')


def triangle(height, width):
    area = height * width
    preimeter = 2 * (height * width)
    
    print(f'삼각형의 넓이는 {area}이고, 둘레는 {perimeter}입니다')
    

#2 함수의 개념

def greeting():
    print('안녕하세요')
    
greeting() 

#3. 함수의 4가지 종류
#3-1. 인자/리턴0
def sum(a,b):
    result = a+ b
    return result
sum(2,4)

C = sum(2,4)
print(C)

   
#3-2. 리턴 0

def say():
    print('hi')
    return 'hi'
    
a= say()
print(a)

#3-3. 인자 0
def say(name, age):
    print(f'제 이름은 {name}이고 나이는 {age}입니다.')
    
a= say('justin',19)
print(a)
 
#3-4. 인자/리턴 X
def say():
    print('안녕하세요')
    
a = say()
print(a)




# new_numbers = numbers.sort() #sort에는  return값이 존재x
# print(new_numbers)
# print(numbers)

numbers = [5,4,3,2,1]
new_numbers = sorted(numbers) #sorted 안에는 return값이 존재하고 있을 것이다.
print(new_numbers)
print(numbers)


def my_max(a,b):
    if a>b:
        return  a
    else:
     return  b
result = my_max(2,4)

print(result)


def my_func(a, b, c):
    print(f'첫번째는 {a}야, 두번째는 {b}야, 세번짼는 {C}야')
    
    my_func(2,4,5)
  

def greeting(name='justin'):
    print(f'{name} 안녕?')
    
greeting()
greeting('김승환')

  
# 1. 인자로 두수를 넘겨서 곱한 값을 return 하는 함수

# def num(a,b):
#     c = a * b
#     return c
# print(num(2,4)) 

# 2. 원의 면적을 구하는 함수 만들기(return)

# def circle_area(r):
#     return 3.14*(r**2)
# print(circle_area(4))

# 3. 주민번호를 가지고 남자인지 여자인지 판단하는 함수
number1 = '530821-1050339'
number2 = '530821-2050339'
def male_female(num):
    if num[7] == '1' :
        print('남자입니다.')
    else:
        print('여자입니다')
        
male_female(number1)
male_female(number2)



def greeting(age, name='jeju'):
    print(f'{name}은 {age}살 입니다')

greeting(19)
greeting(19,'justin')
greeting(age=19, name='bob')
greeting(name='bob', age=19)
greeting(name='철수',19)


print('hi','hi', sep='-')
print(sep='-', 'hi', 'hi')


def my_func(*args): #*은 튜플로 만들어줌
    print(args)
    print(type(args))
    return args
    
my_func(1,2,3)
my_func(1,2,3,4,5)
my_func(1,'a',[1,2,3],(1,2,3),{'a':1,'b':2})

def my_dict(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
my_dict(한국어 = '안녕하세요', 영어='hi', 중국어 = '니하오')
my_dict(한국어= '안녕하세요', 영어='hi', 중국어 = '니하오', 스페인어 = '아디오스')


#1. 사용자의 입력값(정수)를 받아서 그수가 짝수인지 홀수인지 구분하는 함수를 작성
num = int(input('숫자를 입력하세요:'))

def even_odd(num): 
    if num % 2 == 0:
        print('짝수입니다')
    else:
        print('홀수입니다')
even_odd(num)

#2. 리스트 안의 가장 작은 요소를 출력하세요
items = [1,2,-8,0]
def smallest_num_in_list(items):
     min_num = items[0]
     for item in items:
         if item < min_num:
             min_num = item
     return min_num
print(smallest_num_in_list(items))     



#3. 양의정수의 합을 구하세요.(*args)
#positive_sum(1,-4,7,12)--> 20

def positive_sum(*args):
    std_num = 0
    for number in args:
        if number > 0 :
            std_num += number
    return std_num
    
print(positive_sum(1,-2,7,12))
print(positive_sum(1,2,3))
'''




def maxFunc(A):
    max = 0
    for i in A: 
        if max < i:
           max == i
        else
           max == max
    return max

A = [1, 2, 3, 4, 5, 6, 73, 8, 10, 54] 
maxNum = maxFunc(A)
print(maxNum)

