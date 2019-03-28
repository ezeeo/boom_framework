def analyzer(payl,resu):
    assert isinstance(payl,tuple)
    if isinstance(resu,str):
        print('x',end='')
    elif resu.status_code==200:
        if resu.text.find('Password error')!=-1:
            print('.',end='')
        else:
            print('\n'+payl)
            exit()
    else:
        print('-',end='')