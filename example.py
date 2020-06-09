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
for i in range(29):
    timer.tic()
    fib(i+1)
    end_time = timer.toc()
    print(end_time)

#print all results
print(timer)
# save the time
timer.dump(filename='example.csv',mode='w')

# load all runs to plot
timer.load('example.csv')
fig, ax = timer.plot(plot_start_time=True, plot_avg=False)
plt.savefig('example.pdf')
plt.show()

# set up stopwatch (one tic to start --> multiple tics --> toc)
timer2 = Timer()
timer2.tic()
for i in range(29):
    print(fib(i+1), timer2.tic())
timer2.toc()
fig, ax = timer2.plot(plot_start_time=False, plot_avg=False)
plt.show() 
    

# set up another Timer object to read a file
timer3 = Timer()

# load the example run
timer3.load('example2.csv')
print(timer3)
fig, ax = timer3.plot(plot_start_time=True, plot_avg=True)
plt.savefig('example2.pdf')
plt.show()