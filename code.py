import json

with open("details.json","r")as f:
    json_str=f.read()
    json_val=json.loads(json_str)
d=json_val

#alphabetical order

def alorder(a):
    for key,value in sorted(a.items()):
        print(key,value)

#ranks to students

def ranks(a):
    i=1
    for key,value in sorted(a.items(),key=lambda x:x[1]['maths']+x[1]['physics']+x[1]['chemistry'],reverse=True):
        print("rank for {}:{} is {}".format(key,value,i))
        i+=1


#length of the dictinoary
def length(arg):
    count=0
    for i in arg.items():
        count+=1
    return count

#avg marks in each subject

def avg_marks(a):
    m_marks=p_marks=c_marks=0
    for i in dict(a.items()):
        m_marks+=a[i]['maths']
        p_marks+=a[i]['physics']
        c_marks+=a[i]['chemistry']
    tot_marks=m_marks+p_marks+c_marks
    l=length(a)
    avg_m=m_marks/l
    avg_p=p_marks/l
    avg_c=c_marks/l
    tot_avg=tot_marks/3
    print(avg_m)
    print(avg_p)
    print(round(avg_c,3))
    print(round(tot_avg,3))
 
    #above average

    def above_avg(a):
        for key,value in a.items():
            if((a[key]['maths']+a[key]['physics']+a[key]['chemistry'])>tot_avg):
                print(key,value)
    above_avg(d)
    
    # Show students who scored 10% above/below average (total) marks

    def above_below_avg(a):
        for key,value in a.items():
            sum1=a[key]['maths']+a[key]['physics']+a[key]['chemistry']
            if sum1>(11*tot_avg)/10 or sum1<(9*tot_avg)/10 :
                print(key,value)
    above_below_avg(d)

    #Show students who scored above average scores in maths but below average in physics

    def above_avg_maths_below_avg_physics(para):
        for key,value in para.items():
            if para[key]['maths']>avg_m and para[key]['physics']<avg_p:
                print(key,value)
    above_avg_maths_below_avg_physics(d)

    #Number of students who scored above average in all subjects

    def above_avg_mpc(para):
        for key,value in para.items():
            if para[key]['maths']>avg_m and para[key]['physics']>avg_p and para[key]['chemistry']>avg_c:
                print(key,value)
    above_avg_mpc(d)

#ranking based on subject

def subject(a):
    print("1 for maths,2 for physics,3 for chemistry")
    ch=int(input())
    while(True):
        if ch==1:
            for key,value in sorted(a.items(),key=lambda x:x[1]['maths'],reverse=True):
                print(key,value)
            break
        elif ch==2:
            for key,value in sorted(a.items(),key=lambda x:x[1]['physics'],reverse=True):
                print(key,value)
            break
        elif ch==3:
            for key,value in sorted(a.items(),key=lambda x:x[1]['chemistry'],reverse=True):
                print(key,value)
            break
        else:
            print("enter correct one")



alorder(d)
ranks(d)
subject(d)
avg_marks(d)

