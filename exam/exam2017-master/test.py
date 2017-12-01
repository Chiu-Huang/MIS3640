def create_moved_dict(move):
    '''
    Creates a dictionary that maps every letter to a
    character moved down the alphabet by the input move. 

    move: an integer, 0 <= move < 26

    Returns: a dictionary

    Example: an_instance_of_Text.create_moved_dict(2) would generate
    {'a': 'c', 'b': 'd', 'c':'e', ...}  
    '''
    d = {}
    apl = []
    for i in range (97,123,1):
        apl.append(chr(i))
    for i in apl:
        if (ord(i) + move) > 122:
            d[i] = chr (ord(i) + move - 26)
        else:
            d[i] = chr (ord(i) + move)
    return d

def apply_move(string, move):
    diction = create_moved_dict(move)
    newtext = ""
    for character in string:
        newtext += diction.get(character, character)
    return newtext

def load_wordlist(file_name):
    print('Loading word list from file...')
    in_file = open(file_name, 'r')
    line = in_file.readline()
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


### DO NOT MODIFY THIS FUNCTION ###
def is_a_valid_word(word_list, word):
    '''    
    Returns: True if word is in word_list, False otherwise
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

WORDLIST_FILENAME = 'words.txt'
k = load_wordlist(WORDLIST_FILENAME)
def decrypt_text(string):
    helperlist = []
    for i in range (1, 27, 1):
        helpelement = 0
        p = apply_move(string, i)
        newp = p.split()
        # print (type(newp))




        # if type(p) == str:
        #     if is_a_valid_word(k, p):
        #         helpelement += 1
        #     helperlist.append(helpelement)
            
        # if type(p) == list:
        #     pass
        
        for word in newp:
            if is_a_valid_word(k, word):
                # print (word)
                helpelement += 1
        helperlist.append(helpelement)
    
    
    
    return 
joke = "X'kt vxktc je hdrxpa btsxp udg iwt Ctl Ntpg pcs pb ignxcv id bpzt ugxtcsh djihxst Uprtqddz lwxat peeanxcv iwt hpbt egxcrxeath. Tktgn spn, X lpaz sdlc iwt higtti pcs itaa ephhtghqn lwpi X'kt tpitc, wdl X utta, lwpi X sxs iwt cxvwi qtudgt, pcs lwpi X lxaa sd idbdggdl. Iwtc X vxkt iwtb exrijgth du bn upbxan, bn sdv, pcs bt vpgstcxcv. X pahd axhitc id iwtxg rdcktghpixdch pcs itaa iwtb X adkt iwtb. Pcs xi ldgzh. X pagtpsn wpkt iwgtt etdeat udaadlxcv bt-ild edaxrt duuxrtgh pcs p ehnrwxpigxhi."

li = decrypt_text ("jgnnq")
jo = decrypt_text (joke)
print (jo)