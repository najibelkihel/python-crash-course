squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

# ln.1 defining a empty list called 'squares'.
# ln.2 setting up a loop, with following operations applied to each number.
# Rough translation: "for each value in range (1,11): [do the following
# operations].

# ln.3 each value in range (1 to 10) gets squared.
# ln.4 each SQUARED value of square is added to the variable SQUARES.

# ln.6 print all values included in square.

lbj_points = []
for value in range(20, 56, 4):
    lbj_points.append(value+2)

print(lbj_points)
print(sum(lbj_points))

# by using LIST COMPREHENSION, one can attach a loop to an operation.

lbj_points = [value+2 for value in range(20, 56, 4)]
print(lbj_points)

# ln.27 translation = for variable lbj_points, execute operation "value+2" for
# each value in range(20,56,4). The .append() function was not necessary as
# the operation + loop was included between brackets.
