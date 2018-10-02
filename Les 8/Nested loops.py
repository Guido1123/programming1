list=[1,2,3,4,5,6,7,8,9,10]
list1=[1,2,3,4,5,6,7,8,9,10]
inc=0
inc1=0
for number in list:
    print((list[inc]), (list1[0]), list[inc]*list1[0])
    for number in list1:
        print((list[inc]), (list1[inc1]), list[inc] * list1[inc1])
        inc1+=1
        if inc1==10:
            inc1=0
    inc += 1
    if inc == 10:
        inc=0