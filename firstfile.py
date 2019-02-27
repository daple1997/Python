#this is the back-end for the bus tracking app
#Author: Daniil Pleskach


from array import *
from random import *

#this is an array of 20 bus stops from 0 to 19

busStops = [0, 1, 2, 3, 4, 5,
 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ,18, 19]

#this is a variable of random numbers of passngers from 100 to 200
#printed for example

numberPassengers = randint(100, 200)

print(numberPassengers)

#passengers array is created alongside it so that the sum adds up to numberPassengers
passengers = []
for i in range(len(busStops)):

    dummy = randint(0, numberPassengers)
    passengers.append(dummy)
    numberPassengers -= dummy

#whole array is printed to show that randozing went well
print(passengers)

#Print out the bus stop numbers and correspoding passenger data
for index in range(len(busStops)):
    print ("Bus Stop Number: ")
    print ( busStops[index] )
    print ("Number of Passengers: ")
    print ( passengers[index])

