try:
     a=10
     print(a/0)
except Exception as e:
     print(e)
     print("handle exception")

try:
    f=open("shb.txt","r")
    print("hfjhfhjf")
except Exception as e:
    print(e)
try:
    f= open("shu.txt",'r')
    f.write("this is  suspicious code")
except Exception as e:
    print(e)
    print("this is not suspicious code")


#finaly

try:
    f = open("shu.txt", 'r')
    f.write("this is  suspicious code")
except Exception as e:
    print(e)
    print("this is not suspicious code")
finally:
    print("it is alaways excute either try or except is excute")

'''
def askint():
    try:
        val=int(input("entrr  an integer"))
    except:
        print("entered no is not integer")
        try:
            val = int(input("entrr  an integer"))
        except:
            print("pls enter integer")
    finally:
        print("finally will be ecvuted anyhow")
askint()
'''

def askint():
    while True:
        try:
            val = int(input("please try to input an integer"))
            break
        except:
            print("u are not enter an intger")
            continue
askint()