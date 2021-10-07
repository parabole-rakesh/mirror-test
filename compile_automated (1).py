from setuptools import setup
from setuptools.extension import Extension

from Cython.Build import cythonize
from Cython.Distutils import build_ext
import os

name1 = input("Enter the name\n")
extension_list = []
for file1 in os.listdir():
	if(file1[-3:]==".py"):
		extension_list.append([file1[:-3],[file1]])

for i in range(len(extension_list)):
	extension_list[i] = Extension(extension_list[i][0],extension_list[i][1])
print(extension_list)
setup(
    name=name1,
   
    ext_modules=cythonize(
        extension_list,
        build_dir="build",
        compiler_directives=dict(
        always_allow_keywords=True
        )),
    cmdclass=dict(
        build_ext=build_ext
    ),
    packages=[]
)
'''[
           Extension("Combiner_cartesian", ["Combiner_cartesian.py"]),
           Extension("Difference_checker", ["Difference_checker.py"]) ,
           Extension("api_server", ["api_server.py"]) ,
           Extension("Filtering_using_dataconcept_map", ["Filtering_using_dataconcept_map.py"]) ,
           Extension("getting_ouptut", ["getting_output.py"]) , 
           Extension("input_manipulator", ["input_manipulator.py"]), 
           Extension("Loading_Dataframes", ["Loading_Dataframes.py"]), 
           Extension("suggestion_driver", ["suggestion_driver.py"]), 
           Extension("trimming_suggestions_user_learning", ["trimming_suggestions_user_learning.py"]), 
           Extension("trimming_using_wordspace_greedy", ["trimming_using_wordspace_greedy.py"]),
           Extension("wordspace_work", ["wordspace_work.py"])
        ]'''
