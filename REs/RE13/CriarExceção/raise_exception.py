def raise_exception(alist,value):
    result = []
    for element in alist:
        try:
           if element <= value:
               raise ValueError('{0} is not greater than {1}'.format(element,value))
        except Exception as ex:
            result.append(ex)
    return result