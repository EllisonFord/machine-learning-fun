#!/usr/bin/env python3


def set_difference(a, b):
    new_set = set(a) - set(b)
    return new_set


def set_union(a, b):
    new_set = set(a) | set(b)
    return new_set


def set_intersection(a, b):
    new_set = set(a) & set(b)
    return new_set


def p(event, sample_space):
    return len(event) / sample_space


def p_cond(posterior, prior, sample_space):
    return (len(set_intersection(posterior, prior)) / sample_space) / p(prior, sample_space)


a_set = {1, 4}

b_set = {2, 3, 4, 6}

c_set = {1, 3, 5}

S = 6

a_U_b = set_union(a_set, b_set)


result = p_cond(a_U_b, c_set, S)

print(result)
