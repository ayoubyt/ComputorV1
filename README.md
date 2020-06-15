# ComputorV1

ComputorV1 is a program that solves degree 2 or less equations with rational numbers and coefficients.

### Instalation

```sh
    git clone https://github.com/ayoubyt/ComputorV1.git
```
### usage

```sh
    python computor.py "3x^2 + 2x + 5 = x4 + 2"
```

or on linux and mac

```sh
    ./computor.py "3x^2 + 2x + 5 = x4 + 2"
```
Warning : python 3.7 or higher must be already install it in the system,if its not installed already go to : https://www.python.org/downloads/

### Features!

  - it supports ahuman friendly mathematical synthacs
    - all the following formats are supported 
        ```sh
        python computor.py "3x^2 + 2x + 5 = x4 + 2"
        python computor.py "3 * x^2 + 2 * x + 5 = x * 4 + 2"
        python computor.py "3 * x^2 + 2 * x + 5 = x * 4 + 2"
        python computor.py "(x + 1)(x + 2) = (x + 1)^2"
        ```
### Examples

```sh
python computor.py "3x^2 + 2x + 5 = x4 + 2"
3 + x + 3x^2 = 0
delta : -35.000000
delta is positive, so there are two complex solutions :
z1 = -0.166667 + -0.986013i
z2 = -0.166667 + 0.986013i
```

```sh
python computor.py "(x + 1)(x + 2) = (x + 1)^2"
1 + x = 0
a first degree equation with one solution :
x = -1.000000
```

```sh
python computor.py "2x = 4x - 2x" 
all numbers are solutions to this eqation
```
### contributors
    just me :)
