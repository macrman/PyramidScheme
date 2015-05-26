#!/usr/bin/python3

from PyramidScheme.GeneratedParser import parse
from PyramidScheme.runtime import evaluate
from PyramidScheme.Environment import BaseEnv

if __name__ == "__main__":
    env = BaseEnv()
    while True:
        try:
            line = input("pysc>>>")
            if not line:
                break
            print(evaluate(parse("expression", line),env))
        except:
            print("You fucked up. A very useful error message.")
