# passalt.py

[passalt](https://github.com/anqurvanillapy/passalt) in Python 3.

## Install

```bash
$ pip install passalt
```

## Usage

```py
>>> import passalt
>>> hash = passalt.new('foo')
'sha512$oohimsalted$blahblahblah'
>>> passalt.check(hash, 'foo')
True
>>> passalt.check(hash, 'bar')
False
```

## License

MIT
