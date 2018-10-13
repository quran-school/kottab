#!/usr/bin/env python

from main import *
from datetime import date

def test():
    print(get_students())
    add_student("afouad@letarada.com", "Ahmed", "Fouad", "010000", date.today(), "M", "EG")
    print(get_students())

test()
print("teeeeeeeeet")
print()
test()