import os, sys

def entrypoint():
    '''
    Use os.system to load four functions in CWD
    '''
    a = os.system("python3 ./aaa.py")
    b = os.system("python3 ./bbb.py")
    c = os.system("python3 ./ccc.py") 
    d = os.system("python3 ./ddd.py")
    return entrypoint  

if __name__ == "__main__":
    entrypoint()




