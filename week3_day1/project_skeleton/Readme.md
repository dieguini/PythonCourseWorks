# project_skeleton

- [project_skeleton](#project_skeleton)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
  - [Debugging](#debugging)


## Prerequisites
**Install Docker**
  - These tests have been packaged to run with all dependencies
    installed within a Docker container. Due to the use of f-strings,
    this must be run with python 3.6+. The Docker image is based on python 3.9


## Usage
**To run tests open a shell**

  ```bash

  $ cd /path to/project_skeleton
  ```


  *Run the entire test suite*
    
  ``` bash
  $ pytest 
  ```

  *Run the tests for a certain file matching a keyword*
    
  ``` bash
  $ pytest -k <test_file_name>
  ```

  *Run tests while printing all variables and verbose output*

  ``` bash
  $ pytest -vvl
  ```

**To run the app open a shell**

  ```bash

  $ cd /path to/project_skeleton/src
  ```

  *Run the app*
    
  ``` bash
  $ python3 main.py 
  ```


## Debugging

1. If you page up `(ctrl + fn)` within the debug output when running `pytest -vvl` or
when encountering test errors, your cursor may stick and be unable to continue 
writing in the docker shell. You can get past this by typing `q` to return to
entry mode in the docker container.


1. If you'd like to debug a piece of code, you can add either of the following built-in functions
   to a section of the code to enter into the pdb debugger while running pytest. 
   * `breakpoint()` (python 3)
