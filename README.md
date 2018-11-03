<a href="/blob/master/LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green.svg"></a> 
<a href=""><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href=""><img alt="Python: 3.6" src="https://upload.wikimedia.org/wikipedia/commons/3/34/Blue_Python_3.6_Shield_Badge.svg"></a>

Simple wrapper for CLI script which can use all advantages of [structlog](http://www.structlog.org/en/stable/index.html) and can work with modules which use old good standard lib `logging` as well

**Q** Why I need it?  
**A** [Write Logs for Machines, use JSON](https://web.archive.org/web/20170801134840/https://journal.paul.querna.org/articles/2011/12/26/log-for-machines-in-json/)

### Usage
By default [script](/examples/app.py) behave like a proper [12 factor](https://12factor.net/logs) app that outputs only JSON to `stdout` and leave the logs of libraries that use `logging` unchanged  

`python ./examples/app.py`

```
Boom!!!!
Bang!
Wow, exception
Traceback (most recent call last):
  File "/home/mirror/PycharmProjects/structlog-boilerplate/examples/libs/sdt_lib.py", line 14, in f
    1 / 0
ZeroDivisionError: division by zero
{'event': 'Boom!!!!', 'logger': 'libs.structlog_lib', 'level': 'critical', 'timestamp': '2018-11-03T09:25:19.002335Z'}
{'event': 'Bang!', 'logger': 'libs.structlog_lib', 'level': 'error', 'timestamp': '2018-11-03T09:25:19.002424Z'}
{'event': 'Wow, exception', 'logger': 'libs.structlog_lib', 'level': 'error', 'timestamp': '2018-11-03T09:25:19.002550Z', 'exception': 'Traceback (most recent call last):\n  File "/home/mirror/PycharmProjects/structlog-boilerplate/examples/libs/structlog_lib.py", line 15, in f\n    1 / 0\nZeroDivisionError: division by zero'}
{"event": "result", "timestamp": "2018-11-03T09:25:19.002736Z", "value": 42}
```


But if verbosity level escalates, script produces developer friendly colored output  

`python ./examples/app.py -vv`

![colored output](https://user-images.githubusercontent.com/9788811/47950630-a8f5f500-df4c-11e8-9375-b61a83844dd8.png)
