# TASKS
# reversing the list
# printing elements (odd,even,prime) whether the given range of elements
#LIST=[0,1,2,3,4,5,6]
def odd(ele):
    for element in range (ele):
        #print('element....',element)
        if element % 2 != 0 :
            print('odd element...',element)

def even (ele):
    for element in range(ele):
        #print('element...',element)
        if element % 2 == 0 :
            print('even element...',element)

def prime (ele):#0,1,2,3
    for val in range(ele):#0,1,2,3
        if val > 1:#2,3
            for i in range(2, val):#2,3
                if (val % i) == 0:#2 % 2
                    #print('not a prime element..',val)
                    break

            else:
                print('prime element...',val)




odd(20)
even(20)
prime(20)