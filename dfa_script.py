__author__ = 'Harsh Patel'

def tabbing(i):
    tab=""
    for i in range(i+1):
        tab=tab + "   "
    return tab
def make_script(list):
    text=""
    print(len(list[0]))
    for i in range(len(list[0])-1):
        tab=tabbing(i)
        text=text+"""if("""+str(list[0][i])+"""()==yes):\n"""+tab
    text=text+str(list[0][-1])+"()\n"

    for i in range(len(list[1])):
        tab=tabbing(len(list[1])-(i+2))
        tab1=tabbing(len(list[1])-(i+1))
        print(tab)
        text= text + tab + """else:\n""" + tab1 +str(list[1][i])+"""()\n"""
    print(text)


i=raw_input("Enter your Script:")

split1=i.split(';')
split1[0]=split1[0].split(",")
split1[1]=split1[1].split(",")
print(split1)
make_script(split1)



