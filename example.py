from anothertimer import Timer
import matplotlib.pyplot as plt

def fib(n:int) -> int:
    assert n > 0 
    if n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return fib(n-1)+fib(n-2)         

# set up the timer        
timer = Timer()

# time the Fibonacci run
for i in range(33):
    timer.tic()
    fib(i+1)
    timer.toc()

print(timer)
# save the time
timer.dump(filename='example.csv',mode='w')

# load all runs to plot
timer.load('example.csv')
fig, ax = timer.plot(plot_start_time=True, plot_avg=False)
plt.savefig('example.pdf')
plt.show()

# set up another Timer object to read a file
timer2 = Timer()

# load the example run
timer2.load('example2.csv')
print(timer2)
fig, ax = timer2.plot(plot_start_time=True, plot_avg=True)
plt.savefig('example2.pdf')
plt.show()
