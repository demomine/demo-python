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