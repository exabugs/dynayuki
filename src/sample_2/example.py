# -*- coding: utf-8 -*-

import sys

print(sys.version)


def greater_than_5(a: int):
    if a > 5:
        print("%sは、5より大きい" % a)
        return True
    else:
        return False
