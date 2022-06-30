## Create a `virtualenv`
```
pip install wheel setuptools 	## Create the wheel file
pip install virtualenv 	 	## Install virtual environment 
virtualenv venv 	 	## Create a virtual environment 
source venv/bin/activate 	## Activate the virtual environment 
```

To deactvate the virtual environment run `deactivate`

## File structure
```
YOUR_ROOT/
  | venv/
  | setup.py
  | my_package/
    | __init__.py
    | the_script.py
    | fp_stuff/
      | __init__.py
      | fp_module.py
```

## The package
Keep in mind that this is a tutorial so nothing fancy or ceremonial here.
This package exposes the following methods:
- `my_package:multiply_by_two`
- `my_package:start_by_five`
- `my_package.the_script:greet`
- `my_package.the_script:my_sum`
- `my_package.fp_stuff.fp_module:adder`
- `my_package.fp_stuff.fp_module:multiplyer`


## Create the wheel
In the directory `YOUR_ROOT` run `python setup.py bdist_wheel --universal`.
After that your wheel file will be created under the `dist/` folder.

## Use the wheel file
Copy the wheel file, and install it in your environment using
`pip install MY_WHEEL_FILE.whl`

## Uninstall wheel
Run `pip uninstall my_package`


## Sources
* https://towardsdatascience.com/how-to-create-a-wheel-file-for-your-python-package-and-import-it-in-another-project-b09f7fbfc466
* https://realpython.com/python-wheels/
