from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT="-e ."
def get_libraries(file_path)->List[str]:
    '''
    :param file_path:
    :return: List[str]
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [line.strip("\n") for line in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)




setup(
    name="Ml Project",
    version="0.0.1",
    author="Rupesh",
    author_email="keesaramrupesh@gmail.com",
    packages=find_packages(),
    install_requires=get_libraries("requirements.txt")

)