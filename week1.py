# x = 1
# print(x)

# x = x + 1
# print(x)

# # 변수의 이름은 고유한 값이 된다
# xq = 35.0
# x1q3 = 12.5
# df = xq * x1q3
# print(df)

# # 단, 변수 지정시 좀 더 친화적으로 작성해보자 
# # 위와 아래 코드는 동일하지만, Nmoic을 고려해서 변수 이름을 짓자
# a = 35.0
# b = 12.5
# c = a * b
# print(c)

# # 2일차
# # Operator Precedence Rules
# # parenthesis --> Power --> Multiplication --> Addition --> Left to Right

# # Type matters
# letter = 'Hello'
# print(letter)
# new_letter = letter + str(1)
# print(new_letter)

# sval = '123'
# print(type(sval))
# isval = int(sval)
# print(type(isval))

# print(isval + 1)

# name = input("What is your name thou?")
# print('Welcome, ', name)

## 1st Project convert European floor into US floor system
# euf = input('What is the your floor in Europe? write digit only!')
# usf = 1 + int(euf)
# print('In The States, you are on the ', usf , 'floor. Bro!')
# num1 = int(98.6)
# num2 = int(98.4)

# print(num1)
# print(num2)

# x = input('put any num between 1 to 5: ')
# if int(x) == 2:
#     print('your num is 2!')
# elif int(x) > 2:
#     print('Bigger')
# else:
#     print('Not Bigger')
# print('All done')

# try / except 
# astr = 'Bog'
# try:
#     print('Hello')  # try 중간에 문제가 생겨도, 정상작동한 코드까지는 실현한 뒤 except로 넘어감. 
#     istr = int(astr)
#     print('there')
# except:
#     istr = -1

# print('Done', istr)


# num Game
num = input("put the num you like! but only digit, i am watching you!: ")
try:
    x = int(num)
except:
    x = -1

if x > 0:
    print('Nice work!')
else:
    print('it is not a number! ')