# passalt.py

[passalt](https://github.com/anqurvanillapy/passalt) in Python 3.

## Install

```bash
$ pip install passalt
```

## Usage

```py
>>> import passalt
>>> hashstr = passalt.new('foo')
'sha512$oohimsalted$blahblahblah'
>>> passalt.check(hashstr, 'foo')
True
>>> passalt.check(hashstr, 'bar')
False
```

## See also

- `check_password_hash` in
[`werkzeug.security`](http://werkzeug.pocoo.org/docs/0.12/utils/#werkzeug.security.check_password_hash)
- [passalt.js](https://github.com/anqurvanillapy/passalt.js) in Node.js
- [passalt-cli](https://github.com/anqurvanillapy/scripts/blob/master/passalt)
for command-line use

## License

MIT
