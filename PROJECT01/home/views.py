from django.shortcuts import render, HttpResponse
from datetime import datetime
import random
import requests

# Create your views here.
def index(request):
    return render(request, 'home/index.html')  #render(request가 반드시 와야한다.)
    
    
# 자기소개 hola
def hola(request):
    return render(request, 'home/hola.html')
    
# 야식메뉴
def midnight(request):
    menu = ['라면', '떢볶이', '피자', '치킨']
    yasik = random.choice(menu)
    return render(request, 'home/midnight.html', {'menu':menu, 'yasik':yasik})

# 로또 - 6개 --> range(1, 46) & random.sample(interable, 몇개뽑을지)
def lotto(request):
    numbers = range(1, 46)
    lottos = random.sample(numbers,6)
    return HttpResponse(f'오늘의 로또번호는 {lottos}입니다.')
    
def dinner(request):
    menus = ['pizza', 'bob', 'chicken', 'sushi']
    picked = random.choice(menus)
     
    return render(request, 'home/dinner.html', {'menus':menus, 'picked':picked})

# def lottos1(request):
#     numbers = range(1, 46)
#     lottos2 = random.sample(numbers,6)
#     real_lottos = [6, 19, 28, 39, 20, 33]
#     return render(request, 'lottos1.html', {'lottos2':lottos2, 'real_lottos':real_lottos})
    
def hello(request, name):
    return render(request, 'home/hello.html', {'name':name})
    
    
def cube(request, num):
    nums = num ** 3
    return render(request, 'home/cube.html', {'num':num, 'nums': nums})
    
#이름/나이를 받아 template에서 (name)의 나이는 (age)입니다. 
def dlsk(request, name, age):
    return render(request, 'home/dlsk.html', {'name':name, 'age':age})

def times(request, num1, num2):
    num3 = num1 * num2
    return render(request, 'home/times.html', {'num3':num3, 'num1':num1, 'num2':num2})
    
def area(request, r):
    a = (r **2)*3.14
    return render(request, 'home/area.html', {'r':r, 'a':a})
    
#isbirth 예라고 출력 아니면 아니오
def isbirth(request):
    today = datetime.now()
    if today.month == 7 and today.day == 4:
        result = True
    else:
        result = False
    return render(request, 'home/isbirth.html', {'result':result})
    
    
def template_example(request):
    my_list = ['짜장면', '탕수육', '짬뽕', '양장피']
    messages = ['apple', 'cucumber', 'mango', ' watermelon']
    empty_list = []
    
    return render(request, 'home/template_example.html', {'messages':messages, 'my_list':my_list, 'empty_list':empty_list})
    
    
def ping(request):
    return render(request, 'home/ping.html')
    
def pong(request):
    data = request.GET.get('data')
    return render(request,'pong.html', {'data':data})
    
def catch(request):
    return render(request, 'home/catch.html')

# artii API를 통해 ascii 아트로 변환하여 보여주는 페이지    (form에는 항상 action이 들어가야함)
def result(request):
    #1. form 태그로 날린 데이터를 받는다. (GET방식)
    word = request.GET.get('word')
    
    #2. ARTII api로 보낸 응답 결과를 text로 fonts라는 변수에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    
    #3. fonts(str)를 fonts(list)로 바꿔준다.
    fonts = fonts.split('\n')
    
    #4. fonts(list)안에 들어잇는 요소중 하나를 선택해서 font라는 변수에 저장한다.
    font = random.choice(fonts)
    
    #5. 위에서 우리가 만든 word와 fonts를 가지고 다시 artii로 요청을 보낸 후에 해당 응답 결과를 result라는 변수에 저장한다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    
    return render(request, 'home/result.html', {'result':result})
    
def throw(request):
    return render(request, 'home/throw.html')
    
    
def get(request):
    name = request.GET.get('name')
    lottos = range(1,46)
    picked = random.sample(lottos, 6)
    return render(request, 'hoem/get.html', {'name':name, 'picked':picked})
    
def user_new(request):
    return render(request, 'home/user_new.html')
    
def user_creative(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    return render(request, 'home/user_creative.html', {'name':name, 'pwd':pwd})
    
    
def static_example(request):
    return render(request, 'home/static_example.html')