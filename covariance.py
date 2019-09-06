#!/usr/bin/env python3


def mean(v):
    return sum(v)/len(v)


def sample_cov(x, y):
    mx = mean(x)
    my = mean(y)
    s = zip(x, y)
    aggregate = 0.
    for i in s:
        aggregate += (i[0] - mx)*(i[1] - my)
    return aggregate/(len(x)-1)


def population_cov(x, y):
    mx = mean(x)
    my = mean(y)
    s = zip(x, y)
    aggregate = 0.
    for i in s:
        aggregate += (i[0] - mx)*(i[1] - my)
    return aggregate/len(x)


def main():

    x = (12, 30, 15, 24, 14, 18, 28, 26, 19, 27)
    y = (20, 60, 27, 50, 21, 30, 61, 54, 32, 57)

    print('Sample Cov:', sample_cov(x, y))

    print('Population Cov:', population_cov(x, y))


if __name__ == '__main__':
    main()
