def partOne(lines):
    return lines

def partTwo(lines):
    return lines

def runTest():
    testValuesPartOne = """Test data
    you can use
    for testing purposes
    """

    testlines = testValuesPartOne.splitlines()
    partOneResult = partOne(testlines)
    assert partOneResult == 288, "got result: {}".format(partOneResult)

    partTwoResult = partTwo(testlines)
    assert partTwoResult == 71503, "got result: {}".format(partTwoResult)