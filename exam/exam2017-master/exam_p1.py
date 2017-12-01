trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', 
         '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi', '100': 'bai'}

# trans = {'0':'零', '1':'一', '2':'二', '3':'三', '4': '四', '5':'五', 
#          '6':'六', '7':'七', '8':'八', '9':'九', '10': '十', '100': '百'}


# def speak_Chinese(x):
#     '''
#     number: an integer, 0<=number<=999

#     Returns: a string that is the number in Chinese
#     '''
#     if x <= 10:
#         return trans[x] 

def speak_Chinese(x):
    if 0 <= x <= 10:
        return trans[str(x)]
    elif x <= 19:
        return trans["10"] + " " + trans[str(x-10)]
    elif x <= 99:
        if x % 10 != 0:
            return trans[str(x//10)] + " " + trans["10"] + " " + trans[str(x%10)]
        else: 
            return trans[str(x//10)] + " " + trans["10"]
    elif x <= 999:
        if x % 100 == 0:
            return trans[str(x//100)] + " " + trans["100"] 
        elif x % 10 == 0:
            return trans[str(x//100)] + " " + trans["100"] + " " + trans[str((x//10) %10)] + " " + trans["10"]
        else:
            if (x//10) %10 !=0:
                return trans[str(x//100)] + " " + trans["100"] + " " + trans[str((x//10) %10)] + " " + trans["10"] + " " + trans[str(x%10)]
            else:
                return trans[str(x//100)] + " " + trans["100"] + " " + trans[str((x//10) %10)] + " " + trans[str(x%10)]
# For testing
def main():
    # y = 399
    # print(speak_Chinese(y+9))
    # print(speak_Chinese(y+8))
    # print(speak_Chinese(y+7))
    # print(speak_Chinese(y+6))
    # print(speak_Chinese(y+5))
    # print(speak_Chinese(y+4))
    # print(speak_Chinese(y+3))
    # print(speak_Chinese(y+2))
    # print(speak_Chinese(y+1))
    # print(speak_Chinese(y+0))


    print(speak_Chinese(36))
    print('In Chinese: 36 = san shi liu')
    print(speak_Chinese(20))
    print('In Chinese: 20 = er shi')
    print(speak_Chinese(16))
    print('In Chinese: 16 = shi liu')
    print(speak_Chinese(200))
    print('In Chinese: 200 = er bai')
    print(speak_Chinese(109))
    print('In Chinese: 109 = yi bai ling jiu')
    print(speak_Chinese(999))
    print('In Chinese: 999 = jiu bai jiu shi jiu')

if __name__ == '__main__':
    main()
