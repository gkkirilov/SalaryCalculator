import requests
from bs4 import BeautifulSoup
import re

form = {
    'calc_id': 47,
    'form_type': 'calculator',
    'payroll': 13728,
    'payroll_mod': '',
    'payroll_type': 'budget',
    'payroll_cat': 'cat3',
    'born_year': 1961,
    'practice': 0,
    'payroll_extra_p': 0.6,
    'fond_tzpb': 0.4,
    'bonus': '',
    'bonus_type': 1,
    'payroll_month': 10,
    'payroll_year': 2019,
    'osig_dohod': '',
    'txt_field': ''
}

print('Salary per hour in euro')
salary_per_hour = float(input())
# salary_per_hour = float(30)
working_hours_per_day = 8
euro_to_bgn = 1.95583
work_days_in_month = 22
salary_per_month = salary_per_hour * working_hours_per_day * euro_to_bgn * work_days_in_month
form['payroll'] = salary_per_month
response = requests.post('https://www.kik-info.com/kalkulatori/zaplata.php', form)
soup = BeautifulSoup(response.text, 'lxml').prettify()
# print(soup)
f =open('response.html', 'w+')
f.write(response.text)
position = soup.find('Нетна заплата')
allInfo = soup[position:position + 250]
allNumbers = re.findall('(\d+\.\d+)', allInfo)
salary_to_get = float(allNumbers[0])
danak1 = float(allNumbers[1])
danak2 = float(allNumbers[2])
danak3 = float(allNumbers[3])
danak4 = float(allNumbers[4])
print("{:.2f}".format(salary_per_month))
print(salary_to_get)
print("{:.2f}".format(salary_per_month - salary_to_get ))
