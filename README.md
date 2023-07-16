Generate Reports on Signal-K Data
==============

A report and diagram generator for [Signal K](https://signalk.org/specification/1.7.0/doc/data_model.html) json forming time-series graphs of
marine reporters reporting their own info as well as that of their nearest
neighbors'.


see: https://signalk.org/specification/1.7.0/doc/data_model.html

Status
----------

* UNDER CONSTRUCTION
* basic dot and scatter diagram output - NOT USEFUL yet

Installing
-----------

via [Pypi](https://pypi.org/project/signalkrpt/)

```
python -m pip install signalkrpt
```

Developing
-----------

Install with "editing" mode from cloned repo for development of the code.

```
python -m venv venv
source ./venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

Usage
----------

```
signalkrpt -h

cat myfile.json | signalkrpt --gen-dot
cat myfile.json | signalkrpt --gen-scatterplot
```

