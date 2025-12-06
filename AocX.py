def partOne(lines):
    return 0


def partTwo(lines):
    return 0


def runTest():
    testValuesPartOne = """Test data
you can use
for testing purposes
"""

    testlines = testValuesPartOne.splitlines()
    partOneResult = partOne(testlines)
    assert partOneResult == 0, "got result: {}".format(partOneResult)

    partTwoResult = partTwo(testlines)
    assert partTwoResult == 0, "got result: {}".format(partTwoResult)

