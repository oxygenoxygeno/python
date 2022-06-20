# -*- coding: utf-8 -*-


def circle_length(radius: int):
    return 2 * 3.14159 * radius


def circle_area(radius: int):
    return 3.14159 * radius ** 2


def main():
    radius = input()
    print(circle_length(radius))
    print(circle_area(radius))