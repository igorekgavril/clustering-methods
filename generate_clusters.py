
import numpy
import matplotlib.pyplot as plt

xmin = 0
xmax = 50
ymin = 0
ymax = 50
nmin = 1
nmax = 100
kmin = 1
kmax = 10
dmin = 1.0
dmax = 7.0

k = round(numpy.random.uniform(kmin, kmax))
print(k)
for i in range(0, k):
    n = round(numpy.random.uniform(nmin, nmax))

    d = numpy.random.uniform(dmin, dmax)
    m = numpy.random.uniform(xmin + d, xmax - d)
    x = numpy.random.normal(m, d, n)

    d = numpy.random.uniform(dmin, dmax)
    m = numpy.random.uniform(xmin + d, xmax - d)
    y = numpy.random.normal(m, d, n)

    plt.plot(x, y, "p")

plt.xlim(xmin - 10, xmax + 10)
plt.ylim(ymin - 10, ymax + 10)

plt.show()
