newFile = open("__func_.py", "r")

for line in newFile.readlines():
    print line


try:
    fileError = open("__no_.py")
    fileError.write("aaa")
except IOError:
    print("IO error")
else:
    print("file open success")


try:
    print "ready"
    raise Exception("raise exception")
except Exception:
    print "get exception"
else:
    print "no error"
finally:
    print "finish"
