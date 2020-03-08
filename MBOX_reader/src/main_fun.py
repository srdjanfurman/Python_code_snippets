#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Nov 6, 2015

@author: sfurman


The program finds the number of messages and percentages for every domain in the MBOX file.

Example usage
  Run script:
  python main_fun.py mbox_file
  Watch the output.
"""

import io
import re
import sys


def message_start(f_line):
    return f_line.startswith("From ")


def mbox_read(mbox_file):
    message_count = 0
    sum_percentage = 0
    sum_all_domain_number = 0
    li = list()
    domain_number = list()
    percentage_number = list()

    with io.open(mbox_file, "r", encoding='ISO-8859-1') as f:
        for file_line in f:
            # Get domain.
            domain = re.search("@[\w.]+", file_line)
            if domain is not None:
                li.append(domain.group())
            # Number of messages.
            if message_start(file_line):
                message_count += 1

    li_out = list(set(li))

    # Find percentage.
    for i in range(0, len(li_out)):
        domain_number.append(li.count(li_out[i]))
        sum_all_domain_number += domain_number[i]

    for i in range(0, len(li_out)):
        a = sum_all_domain_number - domain_number[i]
        a = (a / float(sum_all_domain_number)) * 100
        a = 100 - a
        percentage_number.append(a)
        sum_percentage += percentage_number[i]

    # Print results.
    print("+----+-Domain--------------------------------+-Msg--+-Percentage--+")
    for i in range(0, len(li_out)):
        print("| {:<3}| {:<38}| {:<5}| {:8.4f}    |".format(
            i, li_out[i], domain_number[i], percentage_number[i]))
    return


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python %s <mbox_file_name>" % sys.argv[0])
        sys.exit(0)
    else:
        mbox_read(sys.argv[1])
