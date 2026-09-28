"""the setup.py file is an essential part of packaging and 
distrubuting python projects.It is used by setuptools
(or distutils in old python verisons) to define the configuration 
of your project ,such as its metadata,dependencies and more
"""
from setuptools import find_packages,setup
from typing import List

def get_requirement() -> List[str]:
        """
        This function will return list of requirements

        """
        requirement_lst:List[str]=[]
        try:
                with open ('requirement.txt','r') as file:
                        #REad lines from the files
                        lines=file.readlines()
                        #process the each line
                        for line in lines:
                                requirement=line.strip()
                                ## ignore the empty lines and -e .
                                if requirement and requirement!='-e .':
                                        requirement_lst.append(requirement)
        except FileNotFoundError:
                print("requirement .txt file not found")  
        return requirement_lst
print(get_requirement())
setup(
        name="Network Security",
        version="0.0.1",
        author="Tania Perween",
        author_email="taniaisrail96@gmail.com",
        packages=find_packages(),
        install_requires=get_requirement()
        
)
                                      

                                

