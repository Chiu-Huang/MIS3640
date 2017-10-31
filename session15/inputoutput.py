import os
import pickle
#synchoronous and asynchoronous
# s: wait to write into harddrive
#'a' means append
# fout = open ('output.txt', 'w')
# line1 = 'How many roads must a man wlak down\n'
# fout.write(line1)
# line2 = 'Before you call him a man?\n'
# fout.write(line1)
# fout.write(line2)
# fout.close()

# replace function
def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.
    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    f_source = open (source)
    f_dest = open (dest, 'w')
    
    for line in f_source:
        line = line.lower()
        new_line = line.replace(pattern.lower(), replace)    
        f_dest.write(new_line)
    
    f_dest.close()    

# pattern = 'Hey Jude'
# replace = 'Hi Donald'
# source = 'sed_tester.txt'
# dest = 'new_' + source
# sed(pattern, replace, source, dest)




# current folder, cwd means current working directory 
cwd = os.getcwd()
print (os.path.abspath('output.txt'))
print (os.path.exists('output.txt'))

print (os.listdir(cwd))


def walk(dirname):
    """Prints the names of all files in 
    dirname and its subdirectories.

    dirname: string name of directory
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)    

# walk(cwd)
def walk2(dirname):
    """Prints the names of all files in 
    dirname and its subdirectories.

    dirname: string name of directory
    """
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))


# walk2(cwd)

try:    
    fin = open('bad_file')
except:
    print('Something went wrong.')





t= [1,2,3]
print (pickle.dumps(t))

t1 = [1, 2, 3]
s = pickle.dumps(t1)
t2 = pickle.loads(s)
print(t2)

t1 == t2
t1 is t2




