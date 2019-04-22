
try:
    #print(10/0)
    if(5<10):
        raise ValueError
except ValueError:
    print("ValueError")
except (TypeError, ZeroDivisionError):
    print("ZeroDivisionError")
finally:
    print("finally")