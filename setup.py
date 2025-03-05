from setuptools import setup, find_packages
from typing import List

hyphen_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function reads the requirements.txt file and returns a list of requirements
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements

setup(
    name='stud_performance_pred',
    version='0.1.0',
    description='End-to-end Prediction of Student Performance',
    author='Asura',
    author_email='suryakantpandidhar@gmail.com',
    url='https://github.com/sukhi-03/Student-Performance-Prediction-E-to-E',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'))