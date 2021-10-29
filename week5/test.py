
# a = 5 

# if a > 3 and a < 5:
#     print(True)
# else:
#     print(False)


# l 
# for i in a:
#     print(i)

def func(*a, **kwarqs):
    # print(a)
    print(kwarqs)
    if kwarqs.get('num') > 8 or kwarqs('num5', 4) < 8:
        print(True)
    else:
        print(False)

# try:
#     func(5, 4)
# except TypeError:
#     print('эээ нормально передавай')
func(5, 6,7, 8,9,3,4, num=3, num2=4)


# i = 0

# while i  < len(a):

# a = (7,885,5,6,7,8,2,2,2,3)

# i = False
# while i < len(a):
#     print(a[i])
#     i += 1


# for i in a:
#     print(i)



# a = [x for x in range(100)]
# # print(a)
# b = [x+3 if x > 45 else x + 2 for x in range(100) if x % 2 == 0]
# # print(b)
# # c = {k:k for k in range(5)}
# c = {k:v for k in range(5) for v in range(k, k+1)}
# print(c)


# try: 
#     a = int(input())
#     print(a+5)
# except TypeError:
#     print('нельзя str + int')
# except ValueError:
#     print('test')
    
# print('Все работает')

