<a href="/blob/master/LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green.svg"></a> 
<a href=""><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href=""><img alt="Python: 3.6" src="https://upload.wikimedia.org/wikipedia/commons/3/34/Blue_Python_3.6_Shield_Badge.svg"></a>

Simple wrapper for CLI script which can use all advantages of [structlog](http://www.structlog.org/en/stable/index.html) and can work with modules which use old good standard lib `logging` as well

**Q** Why I need it?  
**A** [Write Logs for Machines, use JSON](https://web.archive.org/web/20170801134840/https://journal.paul.querna.org/articles/2011/12/26/log-for-machines-in-json/)

### Usage
By default [script](/examples/app.py) behave like a proper [12 factor](https://12factor.net/logs) app that outputs only JSON to `stdout`

```
python ./examples/app.py
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


If verbosity level escalates by `-v` argument, script produces developer friendly colored output

```
python ./examples/app.py -vv
2018-11-03T09:22:20.438945Z [critical ] Boom!!!!                       [libs.sdt_lib] 
2018-11-03T09:22:20.439067Z [error    ] Bang!                          [libs.sdt_lib] 
2018-11-03T09:22:20.439278Z [warning  ] Winter is coming 0.309546      [libs.sdt_lib] 
2018-11-03T09:22:20.439391Z [info     ] Knock, knock                   [libs.sdt_lib] 
2018-11-03T09:22:20.439464Z [debug    ] Beer detected                  [libs.sdt_lib] 
2018-11-03T09:22:20.439543Z [error    ] Wow, exception                 [libs.sdt_lib] 
Traceback (most recent call last):
  File "/home/mirror/PycharmProjects/structlog-boilerplate/examples/libs/sdt_lib.py", line 14, in f
    1 / 0
ZeroDivisionError: division by zero
2018-11-03T09:22:20.439818Z [critical ] Boom!!!!                       [libs.structlog_lib] 
2018-11-03T09:22:20.439917Z [error    ] Bang!                          [libs.structlog_lib] 
2018-11-03T09:22:20.440009Z [warning  ] Winter is coming               [libs.structlog_lib] then=0.310436
2018-11-03T09:22:20.440102Z [info     ] Knock, knock                   [libs.structlog_lib] 
2018-11-03T09:22:20.440188Z [debug    ] Beer detected                  [libs.structlog_lib] 
2018-11-03T09:22:20.440275Z [error    ] Wow, exception                 [libs.structlog_lib] 
Traceback (most recent call last):
  File "/home/mirror/PycharmProjects/structlog-boilerplate/examples/libs/structlog_lib.py", line 15, in f
    1 / 0
ZeroDivisionError: division by zero
{
 "event": "result",
 "timestamp": "2018-11-03T09:22:20.440519Z",
 "value": 42
}
```
