x,y = 1,1
m_count = [31,28,31,30,31,30,31,31,30,31,30,31]
d_count = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
mon_day = 0
for j in range(0,int(x)-1) :
    if x == 1 :
        mon_day = 0
    else : 
        mon_day = mon_day + m_count[j]
total_day = mon_day + int(y)
s_s = total_day % 7
print(d_count[s_s])