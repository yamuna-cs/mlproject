from setuptools import find_packages, setup


def get_requirements(file_path:str)->list[str]:
    '''This function will return the list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        '''to replace new line in requirements.txt file'''
        requirements=[req.replace('\n','') for req in requirements]
        
        '''to remove -e . from requirements.txt file(it is only to call setup.py file)'''
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='yamuna',
    author_email='ai.yamunavr@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)