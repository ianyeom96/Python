# x = 4 숫자 int
# y = "4" 문자 str

# # print(str(x) + y) #44 숫자를 문자로
# print(x + int(y)) #8 문자를 숫자로

#슬라이싱, 인덱싱
#a = "python"
# print(a[0:1] + "y" + a[2:]) #python 슬라이싱 0부터시작하며 직전까지 출력. -1은 n임
#print(a[2]) #t 인덱싱 0부터 시작.

#포매팅
#print("i have %d apples" %3) #i have 3 apples     (숫자는 d, 문자는 s)
#print("i eat %s apples" %"five") #i eat five apples

# a = "i eat {0} apples. so i was sick for {1} days."
# print(a.format(3,"five")) #format함수를 사용.


# n = 3
# days = "five"
# a = "i eat {0} apples. so i was sick for {1} days."
# print(a.format(n+1, days)) #format함수를 변수와 함께 그리고 숫자를 더할 수 도 있다.


#문자열 함수
#a = "python"
#print(a.count('y'))
#print(a.find('t')) #존재하지 않으면 -1출력
#print(a.upper()) # 대문자, 소문자는 lower
#print(','.join(a)) #각 문자 사이에 ,를 삽입
#print(a.replace('y','i'))


# a = int(input("첫번째 숫자를 입력하세요:"))
# b = int(input("두번째 숫자를 입력하세요:"))
# c = a + b
# print("두 수의 합은 {0}입니다.".format(c))


#집합 자료형
#set는 순서가 없고 중복이 안된다. 때문에 인덱싱을 적용하려면 리스트나 튜플로 전환해야함.
#x = set([1,2,3])
#print(x[0]) #일반 인덱싱..오류

# y = list(x) #세트변수 x를 리스트화함. tuple도 가능함.
# print(y[0]) # 1이 출력됨.

# x = set([1,2,3,4,5,6])
# y = set([4,5,6,7,8,9])
#print(x & y) #교집합임. 4,5,6 출력
#print(x.intersection(y)) #교집합. 4,5,6

#print(x|y) #합집합임. 중복은 제외하고 1,2,3,4,5,6,7,8,9 출력
#print(x.union(y))#동일

#x.add(7) #요소 1개 추가.
#x.update([7,8,9]) #여러 개 추가.
# x.remove(6)
# print(x) 


#불리안 : true / false
# if 2 > 1:
#     print("hello")
# if 0 > 0 and 2 > 1:
#     print("hallo")
# else:
#     print("hi")  #elif 도 있음.

# pocket = ['card', 'money']
# if 'card' not in pocket:
#     print("walk")
# else:
#     print("bus")


#function 함수
# def dsum(a, b):     #def 함수이름(매개변수)
#     result = a + b  #수행할 문장
#     return result   #출력값
# d = dsum(1,5)       #변수 = 함수이름(인수)
# print(d)

# def is_odd(numbers):
#     if numbers % 2 == 1:
#         return True
#     else:
#         return False
# d = is_odd(3)
# print(d)

# def avg_numbers(*args): #(*매개변수)는 개수가 정해져 있지 않은 것.
#     result = 0
#     for i in args:
#         result += i # 0+3+4+5
#     return result / len(args) # 12 / 3 == 4
# v = avg_numbers(3,4,5)
# print(v)

#이름과 나이를 받아라 나이가 10살 미만이면 "안녕", 
# 10살에서 20살 사이면  "안녕하세요" 그외에는 "ㅎㅇ"

# def sayHello(name, age):
#     if age < 10:
#         print("안녕" + name)
#     elif 10 <= age <= 20:
#         print("안녕하세요" + name )
#     else:
#         print("ㅎㅇ" + name)

# sayHello("ian", 20)
# sayHello("kill", 30)
# sayHello("john", 9)


#반복문 (for, while)

# i = 0
# while i < 3: # i가 3보다 작으면 코드를 실행시킴.
#     print(i) # 처음엔 0
#     print("철수: 안녕 영희야 뭐해?")
#     print("영희: ㅎㅇ철수 그냥 있어.")
#     i = i + 1 # i = 0 + 1 = 1 + 1 = 2 + 1 = 3

# a = 0
# i = 1
# while i <= 1000:
#     if i % 3 == 0:
#         a += i  # i%3이 0일때, 즉 3의 배수일 때 a에 해당 i를 더함.
#     i += 1
# print(a) #166833, 1부터 1000까지 모든 3의 배수를 더한 값임.

# i = 0
# while True:
#     i += 1
#     if i > 5 :break
#     print("*" * i) 
           

# i = 0
# for i in range(10): #range는 0부터 9까지임. 10번 반복함. 
#     print(i) # 0부터 시작하고 9로 끝남.
#     print("철수: 안녕 영희야 뭐해?")
#     print("영희: ㅎㅇ철수 그냥 있어.")

# score = [60,70,55,80,45]
# s = 0 #학생번호
# for mark in score: #리스트의 요소들이 차례대로 변수 mark에 대입되며 반복해서 출력.
#     s += 1
#     if mark >= 60:
#         print("{0}번 학생은 합격".format(s))
#     else:
#         print("{0}번 학생은 불합격".format(s))

# a = 0
# for i in range(1,101): #1부터 100까지 다 더함.
#     a += i
# print(a) #5050

#break 탈출
# i = 0
# while True:  #무한루프 (break, continue)
#     print(i)
#     print("철수: 안녕 영희야 뭐해?")
#     print("영희: ㅎㅇ철수, 그냥 있어.")
#     i = i + 1
#     if i > 2:
#         break

# coffee = 10
# money = 300
# while money:
#     print("커피가 나옵니다. 잔여커피는 {0}잔 입니다.".format(coffee))
#     coffee -= 1
#     if coffee == 0:
#         print("매진입니다.")
#         break


#continue 반복문을 탈출하지 않고 처음으로 돌아감. 조건에 부합하지 않는 것 만 출력.
# a = 0
# while a < 10:
#     a += 1 
#     if a % 2 == 0: continue #a를 2로 나눠서 0이면 짝수이므로 처음으로 올라감. 홀수는 출력.
#     print(a) #1,3,5,7,9

# a = 0
# while a < 10:
#     a += 1
#     if a % 3 == 0: continue #3의 배수 제외
#     print(a) #1,2,4,5,7,8

# for i in range(3): 
#     print(i) 
#     print("철수: 안녕 영희야 뭐해?")
#     print("영희: ㅎㅇ철수 그냥 있어.")
#     continue #동주의 대화를 포함하지 않음.
#     print("동주: 낄끼")



#자료구조 (리스트[], 튜플(), 딕셔너리{:})
#1.리스트(elements 변경 가능.) mutable
# x = list
# y = [] #두가지로 표시가능.

#x = [1,2,4,3] #리스트 예시

# print(x[0]) # 1 (인덱싱)

#x[1] = 5 #리스트 요소 변경.
#del x[2] #리스트 요소 삭제.
#x.append(6) #리스트 추가.
#x.sort() #순서정렬 : [1,2,3,4] 알파벳도 ㄱㄴ
#x.reverse() #반대로 : [3,4,2,1]
#print(x.index(4)) #4의 위치 2번째 find와 같음. index는 값이 없으면 오류남.
#x.insert(3,5) #[1,2,4,5,3] 5을 3번째자리에 추가
# x.extend([7,8]) #[1,2,4,3,7,8] 리스트확장 리스트만 입력가능함. + x += [7,8]과 같음.
# print(x)

# print(x.pop()) #3 리스트의 마지막 값을 출력. + 마지막 외에도 값을 입력하면 입력값이 출력됨. ㅎ
# print(x)       #한번 더 출력하면 마지막 값을 제외한 리스트를 출력

# num_elements = len(x) #리스트의 길이 : 4, (=리스트 요소의 갯수)
# print(num_elements)

# for n in x:
#     print(n)

# a = [1, 2, 3, ['q', 'w', 'e']] #리스트속 리스트 가능.
# print(a[-1][0]) # q 

# b = [1,2,3,4,5] #리스트 슬라이싱
# print(b[1:3]) #2,3

#2.튜플 (튜플은 한번 지정해놓은 elements들을 변경 못함.) immutable
# x = tuple
# y = () #두 가지 방식

#x = (1,2,3)
# y = ('a','b','c')
# print(x + y)

#3.딕셔너리 (key와 value로 이루어짐.)
# x = dict()
# y = {} #두 가지 방식

# x = {0:"hello", 1:"hi", "age":25,}

# print (x[0])       #해당 value를 가져옴."hello"
# print (x["age"])   #25

# print("age" in x) #딕셔너리 속에 age가 있는가? true
#print(x.values()) #딕셔너리 속에 모든 value 나타냄. keys는 모든 키. itens는 둘다.

# x[0] = "동주" #0의 value를 바꿈.
# print(x) #"동주"

# x["hobby"] = "coding" #새로운 key 와 value 추가함.
# print(x)


#연습
#fruit = ["apple", "apple","banana","banana","kiwi", "peach", "peach", "peach", "melon"]

#d = {}

#for f in fruit: 
#      f = "apple" 
#if f in d: # apple이란 key가 d 라는 딕셔너리에 들어있어?
#         d[f] = d[f] + 1 #그렇다면 apple 갯수를 하나 올려
#else:
#        d[f] = 1 #apple이라는 애가 없으면, 그걸 딕셔너리에 널고 value는 1로 만들어줘.

#print(d) # {'apple':1}, 딕셔너리{}에는 아무것도 없기 때문에 추가했음.



#클래스(==빵틀), 객체(오브젝트(==빵))
# class FoulCal:
#     def setdata(self, first, second): #setdata는 클래스 내부의 함수이므로 메서드라고 부름. 이는 두 숫자를 입력받는 함수임.
#         self.first = first            #(메서드의 첫번째 매개변수인 self는 호출한 객체 자신이 전달됨(ex)self = a). 관례상 쓰임)
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result # 빼기, 나누기 등 새로운 함수를 똑같이 적용 하면 됨.
# #객체 1개
# a = FoulCal()   #객체 = 클래스()
# a.setdata(4,2)  #객체.메서드(매개변수(4는 first 2는 second)) 이때 self는 생략한다. 해당 메서드의 매개변수는 객체a로 전달된다.
# # print(a.first)  #4
# # print(a.second) #2
# print(a.add())    #6
# print(a.mul())    #8
# #객체 2개
# a = FoulCal()
# b = FoulCal()
# a.setdata(3,6)
# b.setdata(5,6)
# print(a.first)  #3
# print(b.second) #6


#생성자(constructor), __init__(객체에 초깃값을 설정해야 할 때) 
# class FoulCal:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#          result = self.first + self.second
#          return result
#     def mul(self):
#          result = self.first * self.second
#          return result
#     def div(self):
#          result = self.first / self.second
#          return result     
# a = FoulCal(4,2) #차이점은 이것이다. setdata메서드에서는 객체 = 클래스() 에서 클래스의 ()는 비어있고 객체.메서드()의 ()는 매개변수로 채워져 있다.
# print(a.first)   #생성사를 사용할 때는 객체 = 클래스()에서 ()를 해당하는 값으로 채워준다.
# print(a.add())
# print(a.mul())

#상속 (기존 클래스는 유지하고 새로운 클래스의 기능을 확장시킬 때 사용.)
# class MoreFoulCal(FoulCal): #()안에 상속할 클래스만 적으면 댐.
#     def pow(self): #상속한 클래스에서 새로운 함수를 만들기.
#         result = self.first ** self.second
#         return result
# a = MoreFoulCal(8,4)
# print(a.add()) #12가 나옴. 위의 FoulCal의 함수를 상속받았다.
# print(a.pow()) #4096

#메서드 오버라이딩 ,덮어쓰기(상속한 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것)
# class SafeFoulCal(FoulCal):
#     def div(self):
#         if self.second == 0:
#             return 0 #원래 0으로 나누게 되면 오류가 발생한다. 이 오류를 0으로 반환함.
#         else:
#             return self.first / self.second
# a = SafeFoulCal(4,0)
# print(a.div()) # 0


# class person:
#     def __init__(self, name, age): #__init__:person이라는 class를 만들 때 name이라는 인자를 만들어 밑에 위치한 name이라는 변수안에 넣어라는 의미.
#         self.name = name
#         self.age = age

#     def say_hello(self, to_name):
#         print("안녕! "+ to_name + " 나는 " + self.name)
    
#     def introduce(self):
#         print("내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + " 살이야")

# ian = person("이안", 25) #여기서 ian이 객체 person이 클래스
# ian.introduce()

# #상속 (위 코드를 밑에서 새로쓰지않고 밑에서 상속받아 쓸 수 있다.)
# class police(person): #police라는 클래스가 person이라는 클래스를 상속함.
#     def arrest(self, to_arrest):
#         print("넌 체포됐다. " + to_arrest)

# class programmer(person):
#     def program(self, to_program):
#         print("다음엔 뭘 만들지? 아 이걸 만들어야지: " + to_program)

# ian = person("이안", 25)
# jenny = police("제니", 23)
# john = programmer("존", 27)

# ian.introduce()
# jenny.introduce() # police라는 클래스에는 introduce가 없지만 상속받아 사용가능함.
# jenny.arrest("이안")
# john.program("python")
# #ian.arrest("제니") #이안은 직업이 없어서 불가능. + 제니 또한 프로그래밍을 못함.


#모듈(변수나 클래스를 모아놓은 파일)
# import mod1 #import는 이미 생성된 모듈을 사용하게 해줌.
# print(mod1.add(3,4))
# print(mod1.sub(4,2))

# from mod1 import add, sub #모듈이름없이 함수만 써서 출력하고 싶을 때. (import * 이라고 적으면 모든 함수를 가져온다.)
# print(add(3,4))
# print(sub(4,2))

# import sys #파이썬 라이브러리 설치 경로, 디렉터리를 알 수 있다.
# print(sys.path)

#패키지(모듈들의 합, 라이브러리 = 다른 개발자가 패키지를 공개한 것), 모듈(코드들이 모여있는 파일)
# from animal import dog #animal 패키지에서 dog라는 모듈을 갖고와줘.
# from animal import cat

# d = dog.Dog()
# d.hi()

# c = cat.Cat()
# c.hi()
# from animal import * # animal 패키지 안에 모든 모듈을 불러옴.


#파일 읽고 쓰기
# f = open("C:/Python39/goose.txt", 'w') #C드라이브 Python39파일안에 goose라는 텍스트파일을 쓰기모드로 생성. 쓰기모드는 존재하는 파일을 열면 내용이 모두 지워짐.
# for i in range(1,11):
#     data = "{0}번째 줄입니다.\n".format(i) #\n은 줄바꿈.
#     f.write(data) #date를 객체f에 써라. 이는 goose.txt파일에 바로 입력된다.
# f.close()

# for i in range(1,11):
#     data = "{0}번째 줄입니다.".format(i)
#     print(data) #프린트는 터미널에 바로 출력.

# f = open("C:/Python39/goose.txt", "r") #위에서 생성한 파일을 읽기모드로 오픈
# line = f.readline() #readline함수는 해당 파일의 첫번째줄을 불러옴.
# print(line) 
# f.close()

# f = open("C:/Python39/goose.txt", "r")
# while True:
#     line = f.readline() #무한루프와 readline함수를 이용해서 모든 라인을 불러옴.
#     if not line: break
#     print(line)
# f.close()

#f = open("C:/Python39/goose.txt", "r")
# print(f.readlines()) #readlines함수는 해당파일에 있는 모든 줄을 읽어서 하나의 리스트에 넣는다.['1번째 줄입니다.\n', '2번째 줄입니다.\n', '3번째 줄입니다.\n'...]
# f.close()

# f = open("C:/Python39/goose.txt", "r")
# print(f.read()) #파일의 전체 내용을 문자열로 불러옴.
# f.close()

#추가모드
# f = open("C:/Python39/goose.txt", "a") #a는 추가모드 존재하던 내용을 유지하면서 내용을 추가하는 것.
# for i in range(11,20): #11번째부터 19번째를 goose파일에 추가.
#     data = "%d 번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

#연습 (test.txt의 java를 python으로 변경.)
# f = open('test.txt','w') #바로 test.txt추가 됨.
# f.write("Life is too short you need java") #txt에 바로 작성
# f.close()

# f = open('test.txt','r') #읽기모드로 열어서 b변수에 내용을 저장.
# b = f.read()
# f.close()

# b = b.replace('jave', 'python') #b변수의 내용을 바꿈.

# f = open('test.txt','w') #다시 쓰기모드로 엶.
# f.write(b) #바뀐 b를 다시 작성함.
# f.close()


#오류 처리기법
# try:
#     4 / 0
# except:                       #except: 만 적으면 모든 오류 제거
#       print() 
# except ZeroDivisionError:     #except 오류명: 까지 적으면 미리 정한 오류가 나타날 때만 except를 수행.
#     print("0으로 나눌 수 없음")

# except ZeroDivisionError as e:  #except 오류명 as 변수: 두번째 + 오류내용확인 , 2개 이상의 오류는 (오류명1, 오류명2)처럼 괄호에 넣으면 동시에 가능.
#     print(e)              #division by zero   +오류회피는 print 대시 pass를 적으면 댐.

#filter, lambda 로 음수제거.
#print(list(filter(lambda x:x>0,[1,-2,3,-5,8,-3])))

# print(list(map(lambda x:x*3,[1,2,3,4])))

# def gugu(n): #구구단 2단 in List
#     result = []
#     i = 1
#     while i < 10:
#         result.append(n * i)
#         i += 1
#     return result
# print(gugu(2))


# result = 0
# for n in range(1, 1000):
#     if n % 3 == 0 or n % 5 == 0:
#         result += n
# print(result)
    
# a = [20,55,67,82,45,33,90,87,100,25]
# result = 0
# while a:
#     m = a.pop()
#     if m >= 50:
#         result += m
# print(result)

# user = input("숫자를 입력해라")
# num =user.split(',')
# total = 0
# for n in num:
#     total += int(n)
# print(total)

user = input('구구단을 출력할 숫자를 입력해라')
gugu = int(user)
for i in range(1,10):
    print(i*gugu, end= " ")

# class cal:
#     def __init__(self, numberlist):
#         self.numberlist = numberlist
#     def add(self):
#         result = 0 
#         for num in self.numberlist:
#             result += num
#         return result
#     def avg(self):
#         total = self.add()
#         return total / len(self.numberlist)
# cal1 = cal([1,2,3,4,5])
# print(cal1.add())
# print(cal1.avg())

#패키지 이미 설치되었지만 실행 안될 때 인터프리터 ctrl + shift + p로 콘다 적용
