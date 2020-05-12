# Python Advanced Template for CLI projects 

This project was created with the intention of facilitate unique template for development and CI/CD of a complex
python cli apps 


## Where to find some help if issues arise using this template ?

This repo was  folked from "David Gutierrez advanced python cli projects layout. 
A link to this repo is inthe References below [0]


The explanation of each file and their  interaction and how and why we arrive here 
and the solutions to the problems we faced is described in [1]

Any recomendation is appreciated

## Running the CLI application
  
  - Install a virtual enviorement
  - Make your file structure similar to the tree of this app.

  - Running the application
      - python sample/core.py (from outside sample dir)
      - python core.py (from sample dir)
  -Testing the application
      - python -m unittest tests/test_basic.py
      - python -m unittest tests/test_advanced.py
      
  - To understand more about the file composition , please read the GitHUb repo 
 
 
## Use of Linters, Static Code tools and Complexity check for code analysis
 
 We use the tools described in "Python Professional Code Recomedations" in [2]...
 
-Use of Lynters , Static Code tools for Code Quality [2]

    -I use black frecuently for code formatting or stilistic [2.4]
    -I use bandit frecuently that analyzes security errors [2.3]
    -I use pyflakes for Logical errors that Analyzes programs and detects various errors [2.2]
    -For complexity checker I use McCabe [2.1]

## What is that README.rst and why it is added to this repo

Python project could need a web documentation. Usually we use Sphinx . We are just  noticing where the Sphins 
Readme.rst file should go in the Python file structure


## Continuos Integration Continuos Development

For CD/CI we will use GitHub actions 
Actions are in the .github/workflows/pythonapp.yml
The default action we have for this projects do the following

- name: python cli advanced application template action
- works for every push ( not for pulls)
- operating system: ubuntu-latest 
- copy our code to github workspace using actions/checkout@v2.1.0
- install python using actions/setup-python@v2
- select version 3.8 of python
- upgrade pip : python -m pip install --upgrade pip
- install requriements : pip install -r requirements.txt
- install pycode style lynter
- use pycodestyle to stop if there is any pycode style errors:
    pycodestyle . --count --select=E9,F63,F7,F82 --show-source --statistics
- exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide   
- pycodestyle . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
-  install pytest pip install pytest
-  run your test sutites with pytest  python -m pytest


## Other github actions

If your project uses for example conda because it is a ML project, we can use any other actions from my 
repo [3]



### Lis of Projects created with this template 

- Machine Learning Classifier 


  
### References
 
 - [0] [David Gutierrez CLI Project Layout](https://github.com/david68cu/python_cli_template_advanced)
 - [1] [Solving Import Problems by Creating a correct Python CLI project struture ]( https://github.com/david68cu/python_import_issues_project_structure.git)
 - [2] [How to Create Professional Python Code](https://github.com/david68cu/python_professional_code_recomendations)
    - Python Code Quality: Tools & Best Practices
        - [2.1] [McCabe complexity checker](https://github.com/PyCQA/mccabe)
        - [2.2] [PyFlakes for python logical errors ](https://github.com/PyCQA/pyflakes)
        - [2.3] [Python Bandit static code security ](https://github.com/PyCQA/bandit)
        - [2.4] [Black the uncompromised formatter](https://github.com/ambv/black)
 - [3] [GitHub actions and cheat sheet ](https://github.com/david68cu/github_cheat_sheet)
 