#!/usr/local/bin/python3
#-*- encoding=utf-8 -*-

def two_sum(nums, target):
    for idx_a, number_a in enumerate(nums):
        for idx_b, number_b in enumerate(nums):
            if idx_a == idx_b:
                continue

            if number_a + number_b == target:
                return [idx_a, idx_b]

    return []


def two_sum_fast(nums, target):
    targets = {}
    for i,n in enumerate(nums):
        t = targets.get(n)
        if t is not None:
            return [t, i]
        targets[target - n] = i
        
    return []


def two_sum_find_all(nums, target):
    results = []
    targets = {}
    for i,n in enumerate(nums):
        t = targets.get(n)
        if t is not None:
            results.append([t, i])
        targets[target - n] = i
        
    return results


def two_sum_allow_duplicate(nums, target):
    results = []
    targets = {}
    for i,n in enumerate(nums):
        t = targets.get(n)
        if t is not None:
            results.append([t, i])
        targets[target - n] = i
        
        if n * 2 == target:
            results.append([i, i])
        
    return results
