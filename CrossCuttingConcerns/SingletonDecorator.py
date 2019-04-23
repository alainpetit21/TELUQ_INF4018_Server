# Singleton/SingletonDecorator.py
class SingletonDecorator:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance == None:
            self.instance = self.klass(*args,**kwds)

        return self.instance

# How to Define the Singleton Class
# @SingletonDecorator
# class ClassToto(...):



# How to use the  Singleton Class
# print(ClassToto().something attribute in the class)
# print(ClassToto().something attribute in the class)


# The first call to ClassToto with parenthesis will get redirected into the decorator, who will then use the __call__
# function and since instance is None, it will create 1 instance of the object with the args and kwds.

# The second time it is called though instance will not be None and it will just return instance.
