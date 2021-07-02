import setuptools 

setuptools.setup( 
    name='mytool', 
    version='1.0', 
    author='Faris Muhammad Kautsar', 
    author_email='farismuhammad8201@gmail.com', 
    description='log file converter to plaintext and JSON', 
    packages=setuptools.find_packages(), 
    entry_points={ 
        'console_scripts': [ 
            'mytool = mytool.mytool:main' 
        ] 
    }, 
    classifiers=[ 
        'Programming Language :: Python :: 3', 
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent', 
    ], 
)