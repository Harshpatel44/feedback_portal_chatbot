__author__ = 'Harsh Patel'



def function(*argv):
    for arg in argv[1:]:
        print(arg[0])


function(['harsh',1],['annu',2])