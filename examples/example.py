from anothertimer import Timer
import matplotlib.pyplot as plt
import gc

# a Fibonacci function to test our timer
def fib(n:int) -> int:
    assert n > 0 
    if n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return fib(n-1)+fib(n-2)         

######################### BASIC TIMER ##########################################

# set up the timer        
timer = Timer()

# time the Fibonacci run
for i in range(29):
    timer.tic()
    fib(i+1)
    timer.toc()

# print all results
print(timer)

# plot the results
fig, ax = timer.plot()
plt.savefig('example.pdf')
plt.show()

########################### STOPWATCH ##########################################

# set up stopwatch (one tic to start --> multiple tics --> toc)
timer2 = Timer()
timer2.tic()
for i in range(29):
    print(fib(i+1), timer2.tic())

timer2.toc()

fig, ax = timer2.plot(plot_start_time=False, plot_avg=False)
plt.show() 

############################ SECTIONS ##########################################

# Timer with sections
timer3 = Timer()
# Setup the sections

timer3.tac('Fib')
timer3.tac('Fib 1')
timer3.tac('Fib 2')

# try the stopwatch mode with sections
timer3.tic()
for i in range(11):
    fib(i+1)

    if i < 5:
        timer3.tic('Fib 1')
    elif i >= 5:
        timer3.tic('Fib 2')

timer3.toc('Fib')

# let's make another section
timer3.tac('Fib 3')
timer3.tic()
for i in range(11):
    fib(i+1)
    timer3.tic('Fib 3')
timer3.toc('Fib')

# print the summary
print(timer3)

# plotting
timer3.plot(plot_start_time=True, plot_avg=False)
plt.show()

########################### SAVING AND LOADING #################################

# save the run from above
timer3.dump('example.csv', mode='w')


# set up another Timer object to read a file
timer4 = Timer()

# load the example run
timer4.load('example.csv')
fig, ax = timer4.plot(plot_start_time=True, plot_avg=True)
plt.savefig('example.pdf')
plt.show()