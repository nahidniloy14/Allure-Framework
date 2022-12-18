import pytest


def testOne():
    print("I am method one")


def testTwo():
    print("I am method two")


@pytest.mark.skip
def testThree():
    print("I am method three")


def testFour():
    print("I am method four")
    assert False
