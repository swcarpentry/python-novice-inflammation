lows = [1, 2, 3]
highs = [40, 50, 60]
for thing in zip(lows, highs):
    print thing

pairs = [ [1, 10], [2, 20], [3, 30] ]
for (left, right) in pairs:
    print 'left:', left, 'and right:', right

canada = [ [1901, -1.0], [1902, -2.0], [1903, -3.0] ]
brazil = [ [1901, 20.0], [1902, 20.0], [1903, 30.0] ]
for ( (left_year, left_value), (right_year, right_value) ) in zip(canada, brazil):
    print 'years are:', left_year, right_year, 'and values are:', left_value, right_value
