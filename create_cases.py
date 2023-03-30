#!/bin/env python3

import csv
import qrcode

host_name = "https://www.cloudcode.work"
qrcode_dir = 'assets/images/qrcode'


def create_case_page(case_id):
    case_file_name = f'case/{case_id}.html'
    with open(case_file_name, 'w') as case_file:
        case_file.write(f'---\n')
        case_file.write(f'layout: case\n')
        case_file.write(f'---\n')

        print(f'Created {case_file_name}')


def create_qr_code(case_id):
    url = f'https://{host_name}/case/{case_id}.html'
    img = qrcode.make(url)

    qrcode_file_name = f'{qrcode_dir}/{case_id}.png'
    with open(qrcode_file_name, 'wb') as qrcode_file:
        img.save(qrcode_file)

    print(f'Created {qrcode_file_name}')


def create_cases(cases_filename):
    with open(cases_filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:

            chapter_id = row['chapter_id']
            chapter_name = row['chapter_name']
            case_id = row['case_id']
            case_name = row['case_name']

            create_case_page(case_id)
            create_qr_code(case_id)


if __name__ == '__main__':
    create_cases('_data/cases.csv')
