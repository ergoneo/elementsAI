# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:41:01 2022

@author: Laurent
"""

def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)
    total_population = sum(populations)

    # write your solution here
    winners_prob = []
    for i in range(0, len(fishers)):
        winners_prob.append((fishers[i]/total_fishers)*100)

    for country, winners_prob in zip(countries, winners_prob):
        print("%s %.2f%%" % (country, winners_prob)) # modify this to print correct results

main()