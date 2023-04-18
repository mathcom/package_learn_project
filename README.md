# package_learn_project

This repo is for exercising how to make setup.py.

- Reference: https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/

Scenario
---
This project includes two packages, pklearn and pklearn2.
The directory architecture is as follow:
```
package_learn_project/
├── src/
│  ├── pklearn/
│  │  ├── __init__.py
│  │  ├── interface.py
│  │  └── data/
│  │      └── primes.csv
│  └── pklearn2/
│      ├── __init__.py
│      └── data/
│          └── twopows.csv
├── README.md
└── setup.py
```

Exercise #1 
---
Before executing the followings, you **must** remove a directory named 'build' if it exists.

```bash
python setup.py bdist_wheel
pip install dist/package_learn-0.1-py3-none-any.whl
```
```python
import pklearn # --> OK
import pklearn # --> ModuleNotFoundError: No module named 'pklearn2'
from pkg_resources import resource_stream
with resource_stream('pklearn', 'data/primes.csv') as f:
    lines = f.readlines() # --> OK
with resource_stream('pklearn2', 'data'twopows.csv') as f:
    lines = f.readlines() # --> ModuleNotFoundError: No module named 'pklearn2'
```

Exercise #2
---
Before executing the followings, you **must** remove a directory named 'build' if it exists.

```bash
python setup2.py bdist_wheel
pip install dist/package_learn-0.2-py3-none-any.whl
```
```python
import pklearn # --> OK
import pklearn2 # --> OK
from pkg_resources import resource_stream
with resource_stream('pklearn', 'data/primes.csv') as f:
    lines = f.readlines() # --> FileNotFoundError: No such file or directory
with resource_stream('pklearn2', 'data/twopows.csv') as f:
    lines = f.readlines() # --> OK
```

Contact
---
```
mathcombio@yonsei.ac.kr
```

