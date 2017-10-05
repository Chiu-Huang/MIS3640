l1 = 'bananas'
l2 = 'rice'
l3 = 'paprika'
l4 = 'potato chips'


def pricetag ():
    list1 = l1, l2, l3, l4
    list2 = []
    t = 0
    for word in list1:
        p = 0
        for letter in word:
            p  += ord(letter)-97
        list2 += [p]
        t+= p
    i = 0
    while i < len(list1):
        print ('{:<15}${:<8}'.format(list1[i],list2[i]))
        i += 1
    print ('-------------------------')
    print ('Total    ${:>8}'.format(t))


def pr ():
    list1 = l1, l2, l3, l4
    list2 = []
    t = 0.0
    for word in list1:
        p = 0
        for letter in word:
            p  += ord(letter)-97
        list2 += [float(p)]
        t+= float(p)
    i = 0
    while i < len(list1):
        print ('{0:<15}${1:.02f}'.format(list1[i],list2[i]))
        i += 1
    print ('-------------------------')
    print ('{0:<15}{1:.02f}'.format("Total: ",t))



