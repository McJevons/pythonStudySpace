import os

# 当前文件的路径
pwd = os.getcwd()
# 当前文件的父路径
father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
# 当前文件的前两级目录
grader_father = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "..")

print(pwd)
print(father_path)
print(grader_father)
