
# coding: utf-8

# In[ ]:


import numpy
import sys
import glob
import matplotlib.pyplot

def analyze(filename):
    
    data = numpy.loadtxt(fname=filename, delimiter=',')

    fig = matplotlib.pyplot.figure(figsize=(10.0,3.0))

    axes1 = fig.add_subplot(1,3,1)
    axes2 = fig.add_subplot(1,3,2)
    axes3 = fig.add_subplot(1,3,3)

    axes1.set_ylabel("average")
    axes1.plot(numpy.mean(data,axis=0))

    axes2.set_ylabel("min")
    axes2.plot(numpy.min(data,axis=0))

    axes3.set_ylabel("max")
    axes3.plot(numpy.max(data,axis=0))

    fig.tight_layout()

    matplotlib.pyplot.savefig(filename+'_fig.eps')
    
def detect_problems(f_name):
    data = numpy.loadtxt(fname=f_name, delimiter=',')
    if numpy.max(data, axis=0)[0] == 0 and numpy.max(data, axis=0)[20] == 20:
        print("Suspicous looking maxima")
    elif numpy.sum(numpy.min(data,axis=0)) == 0:
        print("Suspicous looking minima")
    else:
        print("OK")

name = sys.argv[1]
        
filenames = sorted(glob.glob(name+'*.csv'))

for f in filenames:
    print(f)
    analyze(f)
    detect_problems(f)

