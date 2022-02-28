
a=1
def check_connect():

    if a >=1:
        is_connect = True
    else:
        is_connect = False



def excute_times(num):
    def decorator(func):
        def wrapper(*args, **kw):
            i = 0
            while  i <num:
                func(*args, **kw)
                i+=1
        return wrapper
    return decorator


@excute_times(2)
def check_adb(host):
    check_connect()
    return is_connect
    print('----------'+host)




if __name__ == '__main__':
    result = check_adb('aaaa')
    print(result)
