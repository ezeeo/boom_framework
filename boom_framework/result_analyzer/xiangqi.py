def analyzer(payl,resu):
    assert isinstance(payl,tuple)
    if isinstance(resu,str):
        print('\n'+str(payl)+resu)
    elif resu.status_code==404:
        print('\r'+str(payl),end='')
    elif resu.status_code==200:
        print('\n'+str(payl))
    else:
        print('\n'+str(payl)+str(resu))