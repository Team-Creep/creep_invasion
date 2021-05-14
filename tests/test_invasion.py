from creep_invasion.codecreeps import BadaBingBadaBoom, CodeCreeps, DEFAULT_MOVE_SPEED, EducationTeam, GREEN_SCORING, Game_Text_Format, IMAGE, IMAGE_NAMES, INSTRUCTOR_POSITION, Instructor, InstructorExplode, Just_John, Lives, MIN_HEIGHT, MIN_WIDTH, STARTING_PATH, Shield, Shoot_Laser, WHITE_TEXT
import pytest 
from pygame import * 
from os.path import * 
import sys

def test_window_width():
    actual = MIN_WIDTH
    expected = 800
    assert actual == expected 

def test_window_height():
    actual = MIN_HEIGHT
    expected = 600
    assert actual == expected 

def test_instructor_position():
    actual = INSTRUCTOR_POSITION
    expected = 65
    assert actual == expected 

def test_text_color():
    actual = WHITE_TEXT
    expected = (245, 245, 245)
    assert actual == expected 

def test_score_color():
    actual = GREEN_SCORING
    expected = (12, 215, 73)
    assert actual == expected 

def test_image_names():
    actual = IMAGE_NAMES[0]
    expected = "blue_explode"
    assert actual == expected 

def test_image_john():
    actual = IMAGE_NAMES[4]
    expected = "john"
    assert actual == expected 

shield = Shield()
def test_shield_rect_x():
    actual = shield.rect.x
    expected = 400
    assert actual == expected

def test_shield_rect_y():
    actual = shield.rect.y
    expected = 550
    assert actual == expected

def test_shield_speed():
    actual = DEFAULT_MOVE_SPEED + shield.rect.x
    expected = 405
    assert actual == expected

john = Just_John(5,200000,1)
def test_john_image():
    actual = str(IMAGE['john'])
    expected = '<Surface(3420x1927x32 SW)>'
    assert actual == expected    

def test_john_speed():
    actual = john.move_speed
    expected = 200000
    assert actual == expected 

lives = Lives(2,4)
def test_lives_rect_x():
    actual = lives.rect.x
    expected = 2
    assert actual == expected 

def test_lives_rect_y():
    actual = lives.rect.y
    expected = 4
    assert actual == expected 

laser = Shoot_Laser(4,2,3,10)
def test_laser_rect_x():
    actual = laser.rect.x
    expected = 4
    assert actual == expected 

def test_laser_rect_y():
    actual = laser.rect.y
    expected = 2
    assert actual == expected 

def test_laser_direction():
    actual = laser.direction
    expected = 3
    assert actual == expected 

def test_laser_speed():
    actual = laser.speed
    expected = 10
    assert actual == expected 



