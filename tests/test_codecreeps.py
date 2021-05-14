from codecreeps import *


def test_can_successfully_pull_white_color_variable():
    expected = (245, 245, 245)
    actual = WHITE_TEXT
    assert expected == actual

def test_can_successfully_pull_red_color_variable():
    expected = (225, 0, 0)
    actual = RED_TEXT
    assert expected == actual

def test_can_successfully_pull_blue_color_variable():
    expected = (0, 188, 245)
    actual = BLUE_SCORING
    assert expected == actual

def test_can_successfully_pull_green_color_variable():
    expected = (12, 215, 73)
    actual = GREEN_SCORING
    assert expected == actual

def test_can_successfully_pull_pink_color_variable():
    expected = (245, 0, 220)
    actual = PINK_SCORING
    assert expected == actual

def test_can_instantiate_text_formatting():
    expected = "Code Creepers"
    actual = CodeCreeps()
    assert expected == actual