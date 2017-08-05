garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message=garbled[::-1]
message=message.split('X')
message="".join(message)
print message
