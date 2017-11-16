def foo(i):

    l = [1,2,3]
    try:
        assert i >= 1
        return l[i]
    except TypeError as e:
        print "Caught TypeError"
    except IndexError as e:
        print "Caught Index Error"
    except:
        print "Not sure about error type"
    else:
        print "no error"
    finally:
        print "End try-catch block!!!"

foo('a')
foo(5)
foo(-1)
foo(1)

# Raise Exception in purpose
if 1:
    raise Exception("Raise Exception in purpose")

#Custom Exception
class OwnException(Exception):

    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)
        # or in Python3
        # super().__init__(self, *args, **kwargs)

class MeaningfullException(Exception):
    
    def __init__(self,error_on):
        Exception.__init__(self, "Exception raised on {0}".format(error_on))


def raise_meaningfull_exception(a,b,c):
    raise MeaningfullException(
        {
            'a':a,
            'b':b,
            'c':c
        }
    )

raise_meaningfull_exception(1,3,5)
