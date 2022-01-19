
import datetime
from urllib import response

Days = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')

Months = ('January','February','March','April','May','June','July','August','September',
'October','November','December')

print('Calendar, by Miguel')

while True:
    print('Write the year you want: ')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    
    print('Enter a numeric value to the year, like 2034: ')
    continue
while True:
    print('Chose a month, from 1 to 12: ')
    response = input('> ')

    if not response.isdecimal():
        print('Please, enter a numeric month, like 5 (May): ')
        continue
    
    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12')

def getCalendar(year, month):
    caltext = ''
    caltext = (' '* 34) + Months[month - 1] + ' ' + str(year) + '\n'

    caltext += '...sunday....monday....tuesday....wednesday....thursday....friday....saturday..\n'

    weekseparator = ('+----------' * 7) + '+\n'
    blank = ('|          ' * 7) + '+\n'

    currentDate = datetime.date(year, month, 1)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days = 1)
    
    while True:
        caltext += weekseparator
        daynumrow = ''
        for i in range(7):
            daynumlabel = str(currentDate.day).rjust(2)
            daynumrow += '|' + daynumlabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
        daynumrow += '|\n'
        caltext += daynumrow
        for i in range(3):
            caltext += blank
        if currentDate.month != month:
            break
    caltext += weekseparator
    return caltext

caltext = getCalendar(year, month)
print(caltext)
calendarfilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarfilename, 'w') as file0bj:
    file0bj.write(caltext)

print('Saved to' + calendarfilename)