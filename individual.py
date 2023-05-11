#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    def split_tuple():
        word = input('>>> ')
        result = tuple(value for value in set(word) if word.count(value) < 2)
        print(result)

split_tuple()
