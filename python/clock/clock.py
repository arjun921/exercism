def Clock(hh,mm):
    count=0
    while mm<0:
        mm=60-(abs(mm))
        count+=1
    hh=hh-count
    while mm>=60:
        mm-=60
        hh+=1
    while hh>24:
        hh-=24
    if mm==60:
        mm=0
        hh+=1
    while hh<0:
        hh=24-(abs(hh))
    if hh==24:
        hh=0

    hh = ("{0:0=2d}".format(hh))
    mm = ("{0:0=2d}".format(mm))
    return (hh)+":"+str(mm)

# print(Clock(0, 1723))
# print('04:43')
