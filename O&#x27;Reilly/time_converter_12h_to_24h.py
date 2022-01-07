#!/home/srini/anaconda3/envs/tfgpu/bin/checkio --domain=py run time-converter-12h-to-24h

# You are the modern man who prefers the 24-hour time format. But the 12-hour format is used in some places. Your task is to convert the time from the 12-h format into 24-h by following the next rules:
# - the output format should be 'hh:mm'
# - if the output hour is less than 10 - write '0' before it. For example: '09:05'
# Here you can find some useful information about the12-hour format.
# 
# 
# 
# Input:Time in a 12-hour format (as a string).
# 
# Output:Time in a 24-hour format (as a string).
# 
# Precondition:
# '00:00' <= time <= '23:59'
# 
# 
# END_DESC

def time_converter(time):
    #replace this for solution
    h = time[0:time.find(':')]
    m = time[time.find(':')+1:time.find(':')+3]
    half = time[time.find(' ')+1:]

    if int(h) == 12 and half[0] == 'a':
        h = '00'
    elif int(h) <10 and half[0] == 'a':
        h = '0'+str(h)
    elif int(h) < 12 and half[0] == 'p':
        h = 12 + int(h)
    return str(h)+':'+m
        


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:50 a.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")