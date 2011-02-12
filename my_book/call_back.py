# -*- coding:UTF-8 -*-
def right(values, oracle = None):
    if(oracle !=  None):
        oracle.commit()
    return values
def error(failure, oracle = None):
    if(oracle !=  None):
        oracle.rollback()
    return failure
