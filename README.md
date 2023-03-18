Generate Reports on Signal-K Data
==============

A report and diagram generator for [Signal K](https://signalk.org/specification/1.7.0/doc/data_model.html) json forming time-series graphs of
marine reporters reporting their own info as well as that of their nearest
neighbors'.


see: https://signalk.org/specification/1.7.0/doc/data_model.html

Status
----------

* TODO

![Fun Mutation of Dot Output](docs/boats3.png)


Installing
-----------

via [Pypi](https://pypi.org/project/signalkrpt/)

```
python -m pip install signalkrpt
```

Or install with "editing" mode from cloned repo for development of the code.


virtualenv

```
python -m venv venv
source ./venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --upgrade tox
python -m pip install --upgrade matplotlib
python -m pip install -e .
```

Usage
----------

```
cat myfile.json | signalkrpt
```

![Fun Mutation of Dot Output](docs/boats1.png)
