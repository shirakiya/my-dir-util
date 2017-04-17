# my-dir-util
My util tool for directory operations

# Environment
Python==3.6.1


# Usage
- move source files recursively to dest directory as one level.

```
./mvflat {src path} {dest path}
```

- remove image files(such as .jpg|.jpeg|.png)

```
./rmerrimg {target directory path}
```

- zipnize from large number of files with dividing

```
./smartzip {src path} {dest path} {filename} [-m MAX_UNIT]
```


# Development
## Set up
Enable to check coding guideline with [flake8](http://flake8.pycqa.org/en/latest/) at `pre-commit`

```
$ python hooks/setup.py
```
