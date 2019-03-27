def gen():
    f=open('G:/python/boom_framework/generator/md5.txt','r',encoding='utf-8')
    md5=f.read()
    f.close()
    md5=md5.strip().split('\n')
    yield ('1','hello')
    a=yield
    for m in md5:
        yield (m,'')
        a=yield