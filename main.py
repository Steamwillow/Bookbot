def main():
    path = "books/frankenstein.txt"
    d = {}
    script = get_text(path)
    count = get_word_count(script)
    lower_script = script.lower()
    d = get_char_count(lower_script)
    print(f"--- Begin report of books/frankenstein.txt --- \n {count} words found in the document \n")
    print_dict(d)
    print("--- End report ---")
    #print (d)
    
    #print(count)
    #print(type(words).__name__)

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(str):
    words = str.split()
    return len(words)

def get_str_count(script, s):
    return script.count(s)

def get_char_count(script):
    #abcs = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
    dict = {}
    abcs = list("abcdefghijklmnopqrstuvwxyz")
    for val in abcs:
        count = get_str_count(script,val)
        dict[val] = count
    return dict

def print_dict(d):
    for key, value in d.items():
        print(f"The '{key}' character was found {value} times.")

main()
# print("hello world")