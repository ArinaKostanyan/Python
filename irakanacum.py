"""
def capitalize(string_name):

    string_name2=''

    if 97<=ord(string_name[0])<=122:
        string_name2+=(chr(ord(string_name[0])-32))
    else:
        string_name2+=string_name[0]

    for letter in string_name[1:]:
        
        if 65<=ord(letter)<=90:
            string_name2+=chr(ord(letter)+32)
        else:
            string_name2+=letter          
    
    return string_name2

string_name='amenayn hayoc'

print(capitalize(string_name))
"""

def find(string,value):
    for i in range(len(string)-len(value)+1):
        if string[i:len(value)+i].lower() == value.lower():
            return i
    return 0
""" 
string = 'I Love gata'
value = 'l'

print("Find Function:",find(string,value))
"""

"""

def count(string,value):
    if value not in string:
        return 'none'
    
    q=0

    while value in string:
        q+=1
        string=string[find(string,value)+len(value):]

    return q

string="i love shawarma"

print(count(string,'i'))
"""

""" 
def endswith(string,suffix,end):
    return string[end-len(suffix):end:] == suffix

string = 'mamba'
suffix = 'ba'
start = 0
end = len(string)

print(endswith(string,suffix,end))
"""

def join(iterable,separator):
    string=''
    for i in iterable:
        string+=i+separator
    return string

"""
iterable=['1','2','3']
separator = ' '

print(join(iterable, separator))
"""

def replace(string, old, new):
    
    """lst = string.split()
    for i in lst:
        if i == old:
            lst[find(string, old)-1] =  new
    return join(lst,' ')"""

    string2=''
    i=0

    while i< len(string):
        if string[i:i+len(old)] == old:
            string2 += new
            i+=len(old)
        else:
            string2 += string[i]
            i += 1

    return string2

"""string = ' i hate gata'
print("Replace Function \n", replace(string, 'hate', 'love'))"""

def rfind(string,sub):
    index = -1
    for i in range(len(string)-len(sub)+1):
        if string[i:len(sub)+i] == sub:
            index = i
    return index

string = 'i lovve gata'
#print(rfind(string,'v'))

def startswith(string,sub):
    return string[:len(sub)] == sub

#print(startswith(string,'i'))

def strip(str1, str2):
    string = list(str1)
    t = True
    while t:
        if string[0] in str2:
            string.remove(string[0])
        else:
            t = False
            break
    t = True
    while t:
        item = string[-1]
        if item in str2:
            string.remove(string[-1])
        else:
            t = False
            break
    return join(string, ' ')

string='A London is the capital of the'
#print(' "strip"\n ',strip(string, 'the'))

def lower(string):
    str=''
    for i in string:
        if 65<=ord(i)<=90:
            str+=chr(ord(i)+32)
        else:
            str+=chr(ord(i))

    return str
#string = 'MISIPISI aa'
#print(lower(string))