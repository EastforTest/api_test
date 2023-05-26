import ast
import json

string = input()

print(eval(string))

print(ast.literal_eval(string))

print(json.loads(string))