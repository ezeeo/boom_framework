def gen():
    print('load generator...',end='')
    f=open('G:/python/boom_framework/generator/pass.txt','r',encoding='utf-8')
    passw=f.read()
    f.close()
    passw=passw.strip().split('\n')
    print('done')
    num=1
    for p in passw:
        if num%100==0:print('{}|{}'.format(num,len(passw)),end='')
        yield (p,)
        num+=1
        a=yield