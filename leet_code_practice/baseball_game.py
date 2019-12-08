# You're now a baseball game point recorder.
# Given a list of strings, each string can be one of the 4 following types:
# Integer (one round's score): Directly represents the number of points you get in this round.
# "+" (one round's score):Represents that the points you get in this round are the sum of the last 2 valid round's points.
# "D" (one round's score):Represents that the points you get in this round are the doubled data of the last valid round's points.
# "C" (an operation,which isn't a round's score):Represents the last valid round's points you get were invalid and should be removed.
# Each round's operation is permanent and could have an impact on the round before and the round after.
# You need to return the sum of the points you could get in all the rounds.


def calculate_points():

    points_scored = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    actual_points = list.copy(points_scored)                 # making a copy of the original scores
    sum = 0
    j = 0

    for i in range(0, len(points_scored)):
            if points_scored[i] == "C":
                sum = sum - int(points_scored[i-1])  # in this case, the last round's score is reduced
                actual_points.remove("C")
                actual_points.remove(points_scored[i-1])

            elif points_scored[i] == "D":
                j = actual_points.index("D")
                actual_points[j] = int(actual_points[j-1]) * 2 # in this case, last valid round's score is doubled
                sum = sum + int(actual_points[j])

            elif points_scored[i] == "+":
                j = actual_points.index("+")
                actual_points[j] = int(actual_points[j-1]) + int(actual_points[j-2]) # in this case, last 2 valid rounds score are added
                sum = sum + int(actual_points[j])

            else:
                sum = sum + int(points_scored[i])

    print("The points scored is: {0}".format(sum))


calculate_points()