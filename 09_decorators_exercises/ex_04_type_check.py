def type_check(valid_type):
    def decorator(function):
        def wrapper(*args, **kwargs):
            valid_args = [x for x in args if isinstance(x, valid_type)]
            valid_kwargs = [x for x in kwargs.values() if isinstance(x, type)]
            if valid_kwargs or valid_args:
                return function(*args, **kwargs)
            else:
                return "Bad Type"
        return wrapper
    return decorator



@type_check(int)
def times2(num):
    return num*2

print(times2(2))
print(times2('Not A Number'))

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
