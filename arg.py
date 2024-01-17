def student(name, age, **marks):

    print("Name : ", name)
    print("Age : ", age)
    # print("Marks: ", marks)
    for key, values in marks.items():
        print(key,': ', values)


student("Ishan", 20, Eng=85, Phy=70, Chem=80, Math=90, Comp=88)
# *arg - For tuples
# **arg - For Dictionary
