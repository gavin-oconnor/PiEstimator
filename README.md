# PiEstimator
# This estimator uses the ratio of the area of a square to the area of a circle in order to estimate PI.
# The area of am inscribed circle is pi*r^2 (r=radius)
# Because the circle is inscribed, the square's area is 2r^2 or d^2 (d=diameter)
# Using these ratios and a circle with radius 2, we get pi*4 : 2(2^2)
# Divide both sides by 4, pi : 4
# Set up ratio circle/square = pi/4
# pi = (4*circle)/square
# We then generate n amount of points between (0,2)
# Every point is in the square, so we always add 1 to square
# For the point to be in the circle, its distance must be less than 2 from the center of the circle: (1,1)
# we then plug the points counts of circle and square into the formula, (4*circle)/square
# This formula should give us a number that is an estimation of pi (3.13-3.15)
