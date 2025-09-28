'''The Setup.py is an essential part of packaging and distributing python projects'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """This function will return list of requirements
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            line=file.readlines()
            for line in line:
                requirement=line.strip()
                
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")   

    return requirement_lst  

print(get_requirements())      
        
setup(
    name="Network Security",
    version="0.0.1",
    author="Bhupinder Kaur",
    author_email="bhupinderkaur027@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
            

