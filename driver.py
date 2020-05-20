from direct_map_cache import *
from fully_associative_map_cache import *
from k_associative_map_cache import *
import math

while(True):
    print("What type of mapping do you want for cache?")
    print("1. Direct Mapping")
    print("2. Fully Associative Mapping")
    print("3. k-way Associative memory")
    print("4. Exit")
    a=input("Enter the option:")
    if(a!=""):
        a=int(a)
    if(a==1):
        direct_map_cache()
    elif(a==2):
        fully_associative_map_cache()
    elif(a==3):
        k_associative_map_cache()
    elif(a==4):
        break