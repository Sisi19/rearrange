#!/usr/bin/env python3

import re

def rearrange_name(name):
    result = re.search(r'^([\w .-]*), ([\w .-]*)$', name)
    if result == None:
        return result
    return '{} {}'.format(result[2], result[1])

def main():
    return print(rearrange_name('Sisi, Shi'))

main()

