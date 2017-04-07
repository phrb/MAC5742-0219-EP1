#!/usr/bin/python2
import matplotlib.pyplot as plt
import numpy as np
import math
import fileinput
import sys

def main():

    i = 4
    x, y, stdev, e = [], [], [], []

    for line in fileinput.input():
        line = line.replace(',', '.')
        line = line.replace('%', '/100')
        line = line.replace('\n', '')
        line = line.split('\t')
        y.append(float(line[0]))
        stdev.append(float(eval(line[1])))
        x.append(2**i)
        i += 1

    x = map(math.log, x)
    y = map(math.log, y)

    for i in range(len(y)):
        e.append(math.fabs(y[i]*stdev[i]))

    plt.errorbar(x, y, e, linestyle='solid', marker='^')
    plt.xlabel('log N')
    plt.ylabel('log Time  [s] - AVG of 10 runs')
    plt.title('Sequential ')
    plt.show()

if __name__ == '__main__':
  main()
