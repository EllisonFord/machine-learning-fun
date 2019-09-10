#!/usr/bin/env python3


def set_difference(a: set, b: set) -> set:
    new_set = set(a) - set(b)
    return new_set


def set_union(a: set, b: set) -> set:
    new_set = set(a) | set(b)
    return new_set


def set_intersection(a: set, b: set) -> set:
    new_set = set(a) & set(b)
    return new_set


def p(event, sample_space):
    if isinstance(event, set):
        return len(event) / sample_space
    else:
        return event / sample_space


def p_cond(posterior: set, prior: set, sample_space):
    if isinstance(posterior, set) or isinstance(prior, set):
        return (len(set_intersection(posterior, prior)) / sample_space) / p(prior, sample_space)
    else:
        return -1


A = {1, 4}

B = {2, 3, 4, 6}

C = {1, 3, 5}

S = 6  # Sample Space: 6 sides for a regular dice

A_union_B = set_union(A, B)

result = p_cond(A_union_B, C, S)

print(result)


#  Div ----------------------------

males = 359
females = 164

# Causes
cardiovascular = 353
cerebral = 65
respiratory = 65
other = 40

total = males + females

print(p(cardiovascular, total))


