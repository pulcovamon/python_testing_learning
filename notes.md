###**Notes**  

[I am using this tutorial](https://realpython.com/python-testing/)  

#**Manual testing**  
  - exploratory testing  

#**Automated testing**  
  - **Integration test** &rarr; more components  
    - testing, if components work well witch eaach other  
    - cannot find, where is the error  
  - **Unit test** &rarr; single component  
    - testing, if the component works well  
    - can find the place, which doesn't work well  
  
#**terminology**  
  - ***test step***: trying to perform some action  
  - ***test assertion***: evaluating, if it works well  
  - ***test case***: one of the tests   
  - ***side effect***: altering atribute, class, file, database, etc.   
  - ***fixture***: data created as an inputs  
  - ***parametrization***: running same test with various inputs  

#**test runners**    
  - **unittest**: builtin library  
    - requires using classes and methods   
    - can run using command `python -m unittest test` (file is `test.py`)    
    - or using command line entry point: `unittest.main()` in the code   
  - **nose** or **nose2**  
    - compatible with **unittest** tests  
    - running from command line  
      - to all files called `test*.py`  
      - tests cases inheriting from **unittest**  
      - command: `python -m nose2`  
  - **pytest**  
    - supports execution of unittest cases  
    - executing all tests in python file  
      - all functions starting with `test_`  
    - great features  
      - using builtin `assert` instead of `self.assert*()`  
      - supports filtering for test cases  
      - ability to rerun from the last failing test  
      - huge ecosystem (hundreds of plagins)  
  
#**some useful info**  
  - create `__init__.py` in the project directory &rarr; package (it can be imported)  
  - `__import__()` &rarr; target doesn't have to be package  
  - **tox**: for testing in mutliple versions of Python or package   
    - automates testing in mutliple environemnts    
    - for creating config file: `tox-quickstart`  
      - requires setup.py file in my app folder (steps to install packege)  
    - executing   
      - `tox -e py36`: runs a single environment  
      - `tox -r`: recreates the virtual environments (if dependencies have changed)  
      - `tox -q`: les verbose output   
      - `tox -v`: more verbose output   
  - **Linters**: evaluates code quality
    - **flake8**: comments code style &rarr; configuration from command line of file
  - keeping testing code clean
    - **DRY**: (*don't repeat yourself*)
  - **timeit**: library for evaluating performace of individual functions
  - **bandit**: for security testing
  
#**Automating the execution**   
  - **Ci/CD** tools (*continous integration/continous deployment*)   
  - **Git**: executing automatically &rarr; `commit`   
  - using file `travis.yml`:  
    ```yaml
    language: python
    python:
      - "2.7"
      - "3.7"
    install:
      - pip install -r requirements.txt
    script:
      - python -m unittest discover
  
#**Mocking**  