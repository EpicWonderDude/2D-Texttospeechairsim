string = "Turn right 40 degrees"


def stringparse(string):
    splitspring = string.split()

    degrees = splitspring[1]
    direction = splitspring[2]

    print("The direction is", degrees, "the degrees are:", direction)

stringparse("error up 70 sthis")
stringparse("error down 60 sthis")