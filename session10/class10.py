# xxx.strip()
# msg.strip('*')


# msg.lstrip('*')
# only left 


# msg.replace ('world', 'Ching')

# url = ‘http://www.babson.edu’
# url.startswith ('http')



# url.endswith ('edu')






# s= 'jalapeno'
# s = 'jalape\u00f1o'
# s







# string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# new_string =""
# for letter in string:
#     if letter in ['k','o','e']:
#         letter = chr (ord (letter) + 2)
#         new_string += [letter] 







# fin = open('words.txt')
# line = fin.readline()
# print (line)


# print (repr(line))





fin = open ('words.txt')
for line in fin:
    word = line.strip ()
    print (word)




