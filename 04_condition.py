'''num = int(input('숫자를 입력해주세요:'))

if num % 2 == 1:
    print('홀수입니다.')
else:
    print('짝수입니다.')
 
num = int(input('숫자를 입력해주세요:'))    

if num>=151 :
    print('매우나쁨입니다')
elif num>=81:
    print('나쁨입니다')
elif num>=31:
    print('보통입니다')
else:
    print('좋음입니다.')
    
    #1부터 10사이의 정수중 짝수는 짝수리스트에 홀수는 홀수 리스트출력( range(1,11) )
even_numbers = []
odd_numbers = []

for i in range(1,11):
    if i % 2:
        odd_numbers.append(i)
    else:
        even_numbers(i)
        
print(f'짝수 리스트는 {even_numbers}, 홀수 리스트는 {odd_numbers}')
 '''
 
 #1. 집합처럼 중복을 허용하지 않는 리스트 만들기
 
numbers = [2, 4, 6, 7, 3, 1, 2, 3]
new_numbers=[]

for number in numbers:
    if number not in new_numbers:
        new_numbers.append(number)
        
print(sorted(new_numbers))
 
 
#  2. fizzbuzz
#  조건
#  1.만약 해당숫자가 3으로 나누어지면'Fizz'
#  2.만약 해당숫자가 5로 나누어지면 'Buzz'
#  3.만약 해당 숫자가 3과 5로 모두 나누어지면 'FizzBuzz'
 
# for i in range(1,101):
#      if i % 15 == 0:
#          print('FizzBuzz')
#      elif i % 3 == 0:
#          print('Fizz')
#      elif i % 5 == 0:
#          print('Buzz')
#      else:
#          print(i)
         