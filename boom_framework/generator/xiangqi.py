def gen():
    print('load generator...',end='')
    words='abcmlyx'
    nums='0123456789'
    print('done')
    num=1
    #skip=30145
    skip=0

    for w1 in words:
        for w2 in words:
            for n1 in nums:
                for n2 in nums:
                    for n3 in nums:
                        if skip>0:
                            skip-=1
                            continue
                        #if num%100==0:print('{}|{}'.format(num,len(words)*len(nums)),end='')
                        yield (w1+w2+'ctf'+n1+n2+n3,)
                        num+=1
                        a=yield
        
if __name__ == "__main__":
    'xyctf861'
    num=0
    for p in gen():
        if p==None:continue
        if p[0]=='xyctf861':
            print(num)
            break
        else:
            num+=1
        
    