import sys

import matplotlib.pyplot
import numpy
from matplotlib.figure import Figure
from numpy import ndarray


def main():
  output_type = sys.argv[1]
  input_csv = sys.argv[2]

  print("loading data...")
  data = numpy.loadtxt(input_csv, delimiter=',')

  if output_type == "--figure":
    figure = make_figure(data)
    print("writing figure to output.png ...")
    figure.savefig("output.png")
  elif output_type == "--stats":
    stats = make_stats(data)
    print("writing stats to output.csv ...")
    numpy.savetxt("output.csv", stats, header="mean,max,min", delimiter=",")
  else:
    raise ValueError(f"Unsupported output type: {output_type}")
  print("done!")


def make_figure(data: ndarray) -> Figure:
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
  return fig

def make_stats(data: ndarray) -> ndarray:
  return numpy.column_stack([
    numpy.mean(data, axis=0),
    numpy.max(data, axis=0),
    numpy.min(data, axis=0)
  ])

main()