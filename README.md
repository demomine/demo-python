# demo-python
#   基础
##  Python有五个标准的数据类型：
1.  Numbers（数字）
    *   int（有符号整型）
    *   long（长整型[也可以代表八进制和十六进制]）
    *   float（浮点型）
    *   complex（复数）
2.  String（字符串）
    *   从左到右索引默认0开始的，最大范围是字符串长度少1
    *   从右到左索引默认-1开始的，最大范围是字符串开头
3.  List（列表）
4.  Tuple（元组）
5.  Dictionary（字典）

##  判断
1.  指定任何非0和非空（null）值为true，0 或者 null为false
2.  在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
3.  import的时候会运行module


##  系统相关的信息模块: import sys
1.  sys.argv 是一个 list,包含所有的命令行参数.    
2.  sys.stdout sys.stdin sys.stderr 分别表示标准输入输出,错误输出的文件对象.    
3.  sys.stdin.readline() 从标准输入读一行 sys.stdout.write("a") 屏幕输出a    
4.  sys.exit(exit_code) 退出程序    
5.  sys.modules 是一个dictionary，表示系统中所有可用的module    
6.  sys.platform 得到运行的操作系统环境    
7.  sys.path 是一个list,指明所有查找module，package的路径.  
8.  操作系统相关的调用和操作: import os
9.  os.environ 一个dictionary 包含环境变量的映射关系   
10.  os.environ["HOME"] 可以得到环境变量HOME的值     
11.  os.chdir(dir) 改变当前目录 os.chdir('d:\\outlook')   
12.  注意windows下用到转义     
13.  os.getcwd() 得到当前目录     
14.  os.getegid() 得到有效组id os.getgid() 得到组id     
15.  os.getuid() 得到用户id os.geteuid() 得到有效用户id     
16.  os.setegid os.setegid() os.seteuid() os.setuid()     
17.  os.getgruops() 得到用户组名称列表     
18.  os.getlogin() 得到用户登录名称     
19.  os.getenv 得到环境变量     
20.  os.putenv 设置环境变量     
21.  os.umask 设置umask     
22.  os.system(cmd) 利用系统调用，运行cmd命令   
23.  内置模块(不用import就可以直接使用)常用内置函数：
24.  help(obj) 在线帮助, obj可是任何类型    
25.  callable(obj) 查看一个obj是不是可以像函数一样调用    
26.  repr(obj) 得到obj的表示字符串，可以利用这个字符串eval重建该对象的一个拷贝    
27.  eval_r(str) 表示合法的python表达式，返回这个表达式    
28.  dir(obj) 查看obj的name space中可见的name    
29.  hasattr(obj,name) 查看一个obj的name space中是否有name    
30.  getattr(obj,name) 得到一个obj的name space中的一个name    
31.  setattr(obj,name,value) 为一个obj的name   
32.  space中的一个name指向vale这个object    
33.  delattr(obj,name) 从obj的name space中删除一个name    
34.  vars(obj) 返回一个object的name space。用dictionary表示    
35.  locals() 返回一个局部name space,用dictionary表示    
36.  globals() 返回一个全局name space,用dictionary表示    
37.  type(obj) 查看一个obj的类型    
38.  isinstance(obj,cls) 查看obj是不是cls的instance    
39.  issubclass(subcls,supcls) 查看subcls是不是supcls的子类  
40.  
##################    类型转换  ##################

chr(i) 把一个ASCII数值,变成字符    
ord(i) 把一个字符或者unicode字符,变成ASCII数值    
oct(x) 把整数x变成八进制表示的字符串    
hex(x) 把整数x变成十六进制表示的字符串    
str(obj) 得到obj的字符串描述     
list(seq) 把一个sequence转换成一个list    
tuple(seq) 把一个sequence转换成一个tuple    
dict(),dict(list) 转换成一个dictionary    
int(x) 转换成一个integer    
long(x) 转换成一个long interger    
float(x) 转换成一个浮点数    
complex(x) 转换成复数    
max(...) 求最大值    
min(...) 求最小值  

##  文件处理
1.  file.close()
关闭文件。关闭后文件不能再进行读写操作。
2.  file.flush()
刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
3.  file.fileno()
返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
4.  file.isatty()
如果文件连接到一个终端设备返回 True，否则返回 False。
5.  file.next()
返回文件下一行。
6.  file.read([size])
从文件读取指定的字节数，如果未给定或为负则读取所有。
7.  file.readline([size])
读取整行，包括 "\n" 字符。
8.  file.readlines([sizehint])
读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比sizhint较大, 因为需要填充缓冲区。
9.  file.seek(offset[, whence])
设置文件当前位置
10. file.tell()
返回文件当前位置。
11. file.truncate([size])
截取文件，截取的字节通过size指定，默认为当前文件位置。
12. file.write(str)
将字符串写入文件，没有返回值。
13. file.writelines(sequence)
向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。


##  python标准异常
|异常名称|描述| 备注 |
|---|---|---
| BaseException | 所有异常的基类 |-|
| SystemExit | 解释器请求退出 |-|

|KeyboardInterrupt|	用户中断执行(通常是输入^C)||
|Exception	常规错误的基类
|StopIteration	迭代器没有更多的值
|GeneratorExit	生成器(generator)发生异常来通知退出
|StandardError	所有的内建标准异常的基类
|ArithmeticError	所有数值计算错误的基类
|FloatingPointError	浮点计算错误
|OverflowError	数值运算超出最大限制
|ZeroDivisionError	除(或取模)零 (所有数据类型)
|AssertionError	断言语句失败
|AttributeError	对象没有这个属性
|EOFError	没有内建输入,到达EOF 标记
|EnvironmentError	操作系统错误的基类
|IOError	输入/输出操作失败
|OSError	操作系统错误
|WindowsError	系统调用失败
|ImportError	导入模块/对象失败
|LookupError	无效数据查询的基类
|IndexError	序列中没有此索引(index)
|KeyError	映射中没有这个键
|MemoryError	内存溢出错误(对于Python 解释器不是致命的)
|NameError	未声明/初始化对象 (没有属性)
|UnboundLocalError	访问未初始化的本地变量
|ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
|RuntimeError	一般的运行时错误
|NotImplementedError	尚未实现的方法
|SyntaxError	Python 语法错误
|IndentationError	缩进错误
|TabError	Tab 和空格混用
|SystemError	一般的解释器系统错误
|TypeError	对类型无效的操作
|ValueError	传入无效的参数
|UnicodeError	Unicode 相关的错误
|UnicodeDecodeError	Unicode 解码时的错误
|UnicodeEncodeError	Unicode 编码时错误
|UnicodeTranslateError	Unicode 转换时错误
|Warning	警告的基类
|DeprecationWarning	关于被弃用的特征的警告
|FutureWarning	关于构造将来语义会有改变的警告
|OverflowWarning	旧的关于自动提升为长整型(long)的警告
|PendingDeprecationWarning	关于特性将会被废弃的警告
|RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
|SyntaxWarning	可疑的语法的警告
|UserWarning	用户代码生成的警告

