garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message=garbled[::-1]
message=message.split('X')
message="".join(message)
print message

garbled2 = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message2=filter(lambda x: x!= "X", garbled2)
print message2
