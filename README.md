# demoPackages
A collection of python demo packages using .py and C code:

### simplepypkg:
* Contains sample function $demoprint()$ for testing.
* Contains a subpackage $subpypkg$ with sample function $subdemoprint()$
* Contains a subpackage $planetpkg$ which contains:
    * A python script $planet.py$ containing class definition, instance, class and static methods for class $Planet$.
    * A sample function $calc$ to calculate parameters of an instance of $Planet$ class.
    
### fibcpypkg:
* Contains file $fib.c$ with C code for fibonacci sequence.
* Compiled dynamic library file $fib.so$.
* Python file  $fib1.py$ using CTypes to import the compiled dynamic library.

### testPackages.ipynb:
* A Jupyter notebook to test the packages.
