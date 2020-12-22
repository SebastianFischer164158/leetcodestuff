#!/usr/bin/python3
import re


def interpret(command: str) -> str:
    resp1 = re.sub(r'\(\)', 'o', command)
    resp2 = re.sub(r'\(al\)', 'al', resp1)
    return resp2


command = "G()(al)"
x = interpret(command)
print(x)
command2 = "G()()()()(al)"
y = interpret(command2)
print(y)
command3 = "(al)G(al)()()G"
z = interpret(command3)
print(z)
