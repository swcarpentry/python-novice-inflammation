import numpy
from scipy.stats import truncnorm

def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

data = numpy.zeros([60, 40])
for day in numpy.arange(2, 38):
    offset = numpy.abs(day - 20)
    randomNums = get_truncated_normal(mean=16-offset, sd=2, low=0, upp=19)
    randomInts = numpy.round(randomNums.rvs(60))
    data[:, day] = randomInts

numpy.savetxt("inflammation-05.csv", data, fmt='%i', delimiter=',')
