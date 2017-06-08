# coding=utf-8
import sys;

# anywhere before print
#   hello world
print "hello world!"
#   print chinese
print "你好"

if True:
    print "true"
else:
    print "false"

print "hello " \
      "world"

print """"hello 
          world"""

''''
print "this is quote"
'''

#   raw_input("\ninput here\n")


x = 'demo';
sys.stdout.write(x + '\n')

data = "hello world"
print data[1:2]
print data[2:]
print data * 2

tupleData = ("hello", "world")
print tupleData
print tupleData[0:1]
print tupleData[0]
print tupleData[1:]

mapData = {"key1": "value1", "key2": "value2"}
print mapData
print mapData["key1"]

intData = 10
print 10 ** 10

if "hello" in tupleData:
    print "yes"

if "hell" not in tupleData:
    print "yes"

if "hello":
    print "yes"

if "hello" and "world":
    print "yes"

if "hello" and "world":
    print "yes"

