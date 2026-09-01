#!/usr/bin/env python3
"""
Generate figures used in the lesson episodes.
Usage: ./generate_figures.py
"""

try:
    import numpy
    import matplotlib.pyplot
except ImportError:
    print("Failed to load NumPy and/or Matplotlib", file=sys.stderr)
    exit(1)

# Configure Matplotlib to not convert text to outlines
# All settings: matplotlib.rcParams or matplotlib.pyplot.rcParams
matplotlib.pyplot.rcParams['svg.fonttype'] = 'none'

# Load data
data = numpy.loadtxt(fname="../data/inflammation-01.csv", delimiter=",")

# Episode 1
## Visualizing data

matplotlib.pyplot.imshow(data)
matplotlib.pyplot.savefig("inflammation-01-imshow.svg")
matplotlib.pyplot.close()

matplotlib.pyplot.plot(numpy.mean(data, axis=0))
matplotlib.pyplot.savefig("inflammation-01-average.svg")
matplotlib.pyplot.close()

matplotlib.pyplot.plot(numpy.max(data, axis=0))
matplotlib.pyplot.savefig("inflammation-01-maximum.svg")
matplotlib.pyplot.close()

matplotlib.pyplot.plot(numpy.min(data, axis=0))
matplotlib.pyplot.savefig("inflammation-01-minimum.svg")
matplotlib.pyplot.close()

## Grouping plots
fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=0))

fig.tight_layout()
matplotlib.pyplot.savefig("inflammation-01-group-plot.svg")
matplotlib.pyplot.close(fig)


## Exercise: Drawing Straight Lines
fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0), drawstyle='steps-mid')

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis=0), drawstyle='steps-mid')

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=0), drawstyle='steps-mid')

fig.tight_layout()
matplotlib.pyplot.savefig("inflammation-01-line-styles.svg")
matplotlib.pyplot.close(fig)
