print('What time is it? (digital form)')

hours = hours_given = int(input('Give hours: '))
while hours > 24 or hours < 0:
    hours = int(input('wrong input. Give hours again: '))

minutes = int(input('Give minutes: '))
while minutes > 60 or minutes < 0:
    minutes = int(input('wrong input. Give minutes again: '))

seconds = int(input('Give seconds: '))
while seconds > 60 or seconds < 0:
    seconds = int(input('wrong input. Give seconds again: '))


if 12 <= hours_given < 24:
    pm = True
else:
    pm = False


if hours == 13:
    hours = 1
if hours == 14:
    hours = 2
if hours == 15:
    hours = 3
if hours == 16:
    hours = 4
if hours == 17:
    hours = 5
if hours == 18:
    hours = 6
if hours == 19:
    hours = 7
if hours == 20:
    hours = 8
if hours == 21:
    hours = 9
if hours == 22:
    hours = 10
if hours == 23:
    hours = 11
if hours == 24:
    hours = 12

if hours < 10:
    hours = ('0' + str(hours))
if minutes < 10:
    minutes = ('0' + str(minutes))
if seconds < 10:
    seconds = ('0' + str(seconds))

if pm == True:
    print('The time is: ' + str(hours) + ':' + str(minutes) + ':' + str(seconds) + ' pm')
else:
    print('The time is: ' + str(hours) + ':' + str(minutes) + ':' + str(seconds) + ' am')