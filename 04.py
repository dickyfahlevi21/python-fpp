import requests



r = requests.get('https://mul14.github.io/data/employees.json')
r_json = r.json()
sep = ', '


def find_salary(value):
    if (int(value['salary']) > 15000000): return value['first_name']


def find_location(value):
    def locations(val): return val['city']
    location = list(map(locations, value['addresses']))
    if 'DKI Jakarta' in location: return value['first_name']


def find_birthday(value):
    april = int(value['birthday'].split('-')[1]) == 4
    return value['first_name'] if april else False


def find_dept(value):
    if value['department']['name'] == 'Research and development':
        return value['first_name']


def find_absences(value):
    def count(val): return int(val.split('-')[1]) == 10 and int(val.split('-')[0]) == 2019
    oktober = filter(count,value['presence_list'])
    return {"name":value['first_name'],"absent":len(list(oktober))}


employee_location = filter(None,map(find_location, r_json))
employee_salary = filter(None,map(find_salary, r_json))
employee_birthday = filter(None,map(find_birthday, r_json))
employee_dept = filter(None,map(find_dept, r_json))
employee_absences = filter(None,map(find_absences, r_json))

# print(sep.join(list(employee_salary)))
# print(sep.join(list(employee_location)))
# print(sep.join(list(employee_birthday)))
# print(sep.join(list(employee_dept)))
# print(list(employee_absences))


# Kalau tidak pakai filter hasilnya jadi seperti ini
# ['Sloane Newman', None, None]
# richEmployee = map(findRich,r_json)
# print(list(richEmployee))