#!/usr/bin/env python
import argparse, random

grades = ['A', 'B', 'C', 'D']
default_subjects = [
    'B1 - Anglais',
    'B1 - C - Prog Elem',
    'B1 - Mathematiques',
    'B1 - Igraph',
    'B1 - Expression Ecrite',
    'B1 - Systeme Unix'
]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Epitech's grade generator.")
    parser.add_argument('subjects', type = str, nargs = '*',
                        help = 'List of subjects.')
    parser.add_argument('--defaults', default = False,
                        action = "store_true",
                        help = 'Set defaults subjects.')

    args = parser.parse_args()
    subjects = args.subjects
    if len(subjects) == 0 and args.defaults == False:
        parser.print_help()
        exit(1)
    if args.defaults:
        subjects = default_subjects
    print "Tes grades:"
    for subject in subjects:
        grade = random.choice(grades)
        print '%s : %s' % (subject, grade)
