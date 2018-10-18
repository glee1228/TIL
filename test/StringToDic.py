import re
import ast
oldstr = "{'오윤석': 0, '임혜진': 0, '이동준': 0, '이동훈': 42, '손정효': 0}\n"
newstr = oldstr.replace("\n","")
print(newstr)
dic = ast.literal_eval(newstr)
print(dic)
print(type(dic))