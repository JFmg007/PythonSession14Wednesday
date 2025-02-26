from china import cook as china_cook
from senegal import cook as senegal_cook
try:
    from romania import cook as romania_cook
except ModuleNotFoundError:
    print("sorry, there is no cook in romania")
from china import *
import china as prc
from latam.cuba import cook as cuba_cook
from latam.peru import cook as peru_cook
from latam.mexico.jalisco import cook as jalisco_cook
from latam.mexico.yucatan import cook as yucatan_cook

def greet():
    print("hello from Segoland")

def cook():
    print("we are making cochinillo")

senegal_cook()
china_cook()
cook()
print(prc.hello)
cuba_cook()
peru_cook()
yucatan_cook()
jalisco_cook()