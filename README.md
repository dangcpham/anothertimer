# anothertimer

Just another timer for code timing. anothertimer enables easy timing for code runs, saving timing data, and provide basic plotting capabilities. Example usage:

```python
from anothertimer import Timer
timer = Timer()
timer.tic()
#some code here
timer.toc()
```

Saving and loading the data:
```python
timer.dump('example.csv', mode='a')
timer.load('example2.csv')
```

Plotting can be done via:
```python
timer.plot()
```

Run example.py and see some example plots!

## Installation
Use pip: `pip install anothertimer`

### Dependecies

Standard Python libraries (typing, time, os, csv).
matplotlib (optional) - for plotting.

### Precision

Currently, anothertimer uses the time.time() function keeps track of time elapsed. The precision is in the sub-second range (read more about Python timing at https://www.python.org/dev/peps/pep-0564/,  https://stackoverflow.com/questions/1938048/high-precision-clock-in-python). Currently, It is not a good idea to use this package for high precision applications, consider the timeit module.
