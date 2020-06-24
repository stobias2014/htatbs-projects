#!/bin/python3

def collatz(number) {
    if(number / 2 == 0) {
        print(number / 2)
    } else if(number / 2 > 0) {
        print(3 * number + 1) 
    }
}
