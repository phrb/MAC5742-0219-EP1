#!/usr/bin/python2
import matplotlib.pyplot as plt
import numpy as np
import math
import fileinput
import sys
import os

def main():

    power = 4
    x, y, stdev, e = [], [], [], []

    infile = fileinput.input()
    title  = next(infile).replace('\n', '') # Title in the FIRST LINE

    for line in infile:
        line = line.split('\t')
        y.append(float(line[0]))
        stdev.append(float(eval(line[1])))
        x.append(2**power)
        power += 1

    x = map(math.log, x)
    y = map(math.log, y)

    for i in range(len(y)):
        e.append(math.fabs(y[i]*stdev[i]))

    plt.errorbar(x, y, e, linestyle='solid', marker='^')
    plt.xlabel('log N')
    plt.ylabel('log Time  [s] - AVG of 10 runs')
    plt.title(title)
    plt.savefig(os.environ['EP1219'] + '/ploter/pictures/' + title + '.png')

if __name__ == '__main__':
  main()
