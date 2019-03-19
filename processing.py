__author__ = 'Harsh Patel'
import json
import random

#     * for faculty , + for student


def q1(faculty="Nirali Naik",user="Harsh"):
    file=open('New_APPROACH/Data/greetings.json','r')
    j_file=json.load(file)
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
    if(isinstance(j_file[r_number],list)):   #if it is a list, display all values
        lista=[]
        for j in j_file[r_number]:
            j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
            j=str(j).replace('+',user)
            lista.append(j)
        return lista
    else:
        j_file[r_number]=str(j_file[r_number]).replace('*',faculty)
        j_file[r_number]=str(j_file[r_number]).replace('+',user)
        #print(str(j_file[r_number]))
        return str(j_file[r_number])

def q2(faculty="Nirali Naik",user="Harsh"):    #interrupted bye
    file=open('New_APPROACH/Data/bye.json','r')
    j_file=json.load(file)
    j_file=j_file['interrupted']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
    if(isinstance(j_file[r_number],list)):   #if it is a list, display all values
        lista=[]
        for j in j_file[r_number]:
            j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
            j=str(j).replace('+',user)
            lista.append(j)
            print(j)
        return lista
    else:
        j_file[r_number]=str(j_file[r_number]).replace('*',faculty)
        j_file[r_number]=str(j_file[r_number]).replace('+',user)
        return str(j_file[r_number])

def q3(faculty="Nirali Naik",user="Harsh"):     #good_bye finally
    file=open('New_APPROACH/Data/bye.json','r')
    j_file=json.load(file)
    j_file=j_file['good_bye']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
    if(isinstance(j_file[r_number],list)):   #if it is a list, display all values
        lista=[]
        for j in j_file[r_number]:
            j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
            j=str(j).replace('+',user)
            lista.append(j)
        return lista
    else:
        j_file[r_number]=str(j_file[r_number]).replace('*',faculty)
        j_file[r_number]=str(j_file[r_number]).replace('+',user)
        return str(j_file[r_number])


def q4(faculty="Nirali Naik",user="Harsh"):
    file=open('New_APPROACH/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['course_completion']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
    if(isinstance(j_file[r_number],list)):   #if it is a list, display all values
        lista=[]
        for j in j_file[r_number]:
            j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
            j=str(j).replace('+',user)
            lista.append(j)
        return lista
    else:
        j_file[r_number]=str(j_file[r_number]).replace('*',faculty)
        j_file[r_number]=str(j_file[r_number]).replace('+',user)
        return str(j_file[r_number])


def q5(faculty="Nirali Naik",user="Harsh"):
    file=open('New_APPROACH/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['punctuality']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
    if(isinstance(j_file[r_number],list)):   #if it is a list, display all values
        lista=[]
        for j in j_file[r_number]:
            j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
            j=str(j).replace('+',user)
            lista.append(j)
        return lista
    else:
        j_file[r_number]=str(j_file[r_number]).replace('*',faculty)
        j_file[r_number]=str(j_file[r_number]).replace('+',user)
        return str(j_file[r_number])


def q6(faculty="Nirali Naik",user="Harsh"):
    file=open('New_APPROACH/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['creativity']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
    if(isinstance(j_file[r_number],list)):   #if it is a list, display all values
        lista=[]
        for j in j_file[r_number]:
            j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
            j=str(j).replace('+',user)
            lista.append(j)
        return lista
    else:
        j_file[r_number]=str(j_file[r_number]).replace('*',faculty)
        j_file[r_number]=str(j_file[r_number]).replace('+',user)
        return str(j_file[r_number])

def q7(faculty="Nirali Naik",user="Harsh"):
    file=open('New_APPROACH/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['solving_problems']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
    if(isinstance(j_file[r_number],list)):   #if it is a list, display all values
        lista=[]
        for j in j_file[r_number]:
            j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
            j=str(j).replace('+',user)
            lista.append(j)
        return lista
    else:
        j_file[r_number]=str(j_file[r_number]).replace('*',faculty)
        j_file[r_number]=str(j_file[r_number]).replace('+',user)
        return str(j_file[r_number])

def q8(faculty="Nirali Naik",user="Harsh"):
    file=open('New_APPROACH/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['knowledge']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
    if(isinstance(j_file[r_number],list)):   #if it is a list, display all values
        lista=[]
        for j in j_file[r_number]:
            j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
            j=str(j).replace('+',user)
            lista.append(j)
        return lista
    else:
        j_file[r_number]=str(j_file[r_number]).replace('*',faculty)
        j_file[r_number]=str(j_file[r_number]).replace('+',user)
        return str(j_file[r_number])

def q9(faculty="Nirali Naik",user="Harsh"):
    file=open('New_APPROACH/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['mode_of_teaching']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
    if(isinstance(j_file[r_number],list)):   #if it is a list, display all values
        lista=[]
        for j in j_file[r_number]:
            j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
            j=str(j).replace('+',user)
            lista.append(j)
        return lista
    else:
        j_file[r_number]=str(j_file[r_number]).replace('*',faculty)
        j_file[r_number]=str(j_file[r_number]).replace('+',user)
        return str(j_file[r_number])

def q10(faculty="Nirali Naik",user="Harsh"):
    file=open('New_APPROACH/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['motivate']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
    if(isinstance(j_file[r_number],list)):   #if it is a list, display all values
        lista=[]
        for j in j_file[r_number]:
            j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
            j=str(j).replace('+',user)
            lista.append(j)
        return lista
    else:
        j_file[r_number]=str(j_file[r_number]).replace('*',faculty)
        j_file[r_number]=str(j_file[r_number]).replace('+',user)
        return str(j_file[r_number])

def q11(faculty="Nirali Naik",user="Harsh"):
    file=open('New_APPROACH/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['interaction']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
    if(isinstance(j_file[r_number],list)):   #if it is a list, display all values
        lista=[]
        for j in j_file[r_number]:
            j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
            j=str(j).replace('+',user)
            lista.append(j)
        return lista
    else:
        j_file[r_number]=str(j_file[r_number]).replace('*',faculty)
        j_file[r_number]=str(j_file[r_number]).replace('+',user)
        return str(j_file[r_number])

def q12(faculty="Nirali Naik",user="Harsh"):
    file=open('New_APPROACH/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['pedagogical_effectiveness']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
    if(isinstance(j_file[r_number],list)):   #if it is a list, display all values
        lista=[]
        for j in j_file[r_number]:
            j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
            j=str(j).replace('+',user)
            lista.append(j)
        return lista
    else:
        j_file[r_number]=str(j_file[r_number]).replace('*',faculty)
        j_file[r_number]=str(j_file[r_number]).replace('+',user)
        return str(j_file[r_number])


def q13(faculty="Nirali Naik",user="Harsh"):
    file=open('New_APPROACH/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['classroom_env']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
    if(isinstance(j_file[r_number],list)):   #if it is a list, display all values
        lista=[]
        for j in j_file[r_number]:
            j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
            j=str(j).replace('+',user)
            lista.append(j)
        return lista
    else:
        j_file[r_number]=str(j_file[r_number]).replace('*',faculty)
        j_file[r_number]=str(j_file[r_number]).replace('+',user)
        return str(j_file[r_number])

