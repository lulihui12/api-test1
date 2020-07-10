try:
    num1=int(input("请输入一个被除数"))
    num2=int(input("请输入一个除数"))
    print(num1/num2)
except ZeroDivisionError:  #抛出除数不能为0的异常
    print("除数不能为0")
except ValueError:
    print("字符类型错误咯，需要数值型的整数")  #抛出字符类型错误的异常
#如果不知道异常的名字怎么办呢
except:
    print("不知道什么异常，就是异常了")   #通用型异常
#如果没有发生异常，使用else语句
else:
    print("程序没有发生异常")   #有异常走except，没有异常走else模块
#不管发没发生异常，都走finally的模块
finally:
    print("无论异常与否，都走这里哦")

x=10
if x>5:
    raise Exception("这个一个抛出的异常")