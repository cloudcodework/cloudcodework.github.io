#!/bin/env python3

import csv

with open('_data/cases.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:

        chapter_id = row['chapter_id']
        chapter_name = row['chapter_name']
        case_id = row['case_id']
        case_name = row['case_name']

        case_file_name = f'case/{case_id}.html'
        with open(case_file_name, 'w') as case_file:
            case_file.write(f'---\n')
            case_file.write(f'layout: case\n')
            case_file.write(f'---\n')


