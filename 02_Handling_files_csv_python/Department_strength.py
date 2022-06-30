import csv
import sys
""" give input csv file location as command line arg"""


def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list


def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data


def write_report(dictionary, report_file):
    with open(report_file, "w+") as file:
        for department in sorted(dictionary):
            file.write(str(department) + ':' + str(dictionary[department]) + '\n')
        file.close()


if __name__ == "__main__":
    csv_location = sys.argv[1]
    employee_list = read_employees(csv_location)
    dictionary = process_data(employee_list)
    write_report(dictionary, input('Enter output_file_location> '))
