# def get_count(func):
#     def multiply(*args, **kwargs):
#         print(u"Function called::::::::::::  %r" % func.__name__)
#         if args:
#             print("args::::::::::: ",args)
#         if kwargs:
#             print("kwargs::::::::::::: ",kwargs)
#         result = len(args)+len(kwargs.keys())
#         print(func(*args, **kwargs))
#         print("Result -------------------> ", result)
#         return result
#     return multiply

# def logged_func #     def logged(*args, **kwargs):
#         print(u"Function %r called" % func.__name__)
#         if args:
#             print("args: ",args)
#         if kwargs:
#             print("kwargs: ",kwargs)
#         result = func(*args, **kwargs)
#         print("Result --> ", result)
#         return result
#     return logged

# @get_count
# @logged_func
# def add(a, b, c=4, d=1):
#     print("inside add")
#     return a+b+c

# # log_add = logged_func(add)

# print(add(2, 3, c=5, d=6))

def italic(func):
    def wrapper():
        print('italic')
        return '<i>' + func() + '</i>'
    return wrapper
  
def strong(func):
    def wrapper():
        print('strong')
        return '<strong>' + func() + '</strong>' 
    return wrapper
    
@italic
@strong
def introduction():
    return 'This is a basic program'
  
print(introduction())
