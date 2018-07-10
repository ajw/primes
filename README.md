# primes
Generates a multiplication table of primes.

Usage:
```sh
primes.py <n>
```
where n is number of primes.

Run doctest using:
```sh
python -m doctest primes.py
```
For verbose output use:
```sh
python -m doctest -v primes.py
```

TODO:
* Verify input
* Make table formatting and output more elegant
* Evaluate improvements to prime algorithm

Performance results for 20000 primes:
* output via string: 35m25.177s
* output direct to stdout: 25m8.090s