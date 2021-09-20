def compatible(A,B):
    if A == [] or B == []:
        return 'A and B cannot be multiplied'
    try:
        assert len(A[0]) == len(B),'A and B cannot be multiplied'
    except AssertionError as ex:
        return ex
    return 'A and B can be multiplied'