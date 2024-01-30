import json

def employees_rewrite(sort_type):

    keys = ['firstname', 'lastname', 'department', 'salary']

    if sort_type.lower() not in keys:
        raise ValueError('Bad key for sorting')

    with open('employees.json', 'r') as file:
        data = json.load(file)
        employees = data['employees']

        sorted_employees = []
        for employees in employees:
            if sort_type in employees:
                sorted_employees.append(employees)

        if sort_type.lower() == 'salary':
            sorted_employees.sort(key=lambda x: x[sort_type], reverse=True)
        else:
            sorted_employees.sort(key=lambda x: x[sort_type])

        output_filename = f'employees_{sort_type.lower()}_sorted.json'
        with open(output_filename, 'w') as output_file:
            json.dump({'employees': sorted_employees}, output_file, indent=4)

employees_rewrite('firstName')
employees_rewrite('lastName')
employees_rewrite('department')
employees_rewrite('salary')

