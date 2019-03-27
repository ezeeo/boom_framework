def analyzer(payl,resu):
    assert isinstance(payl,tuple)
    if resu.status_code==200:
        print('\n'+resu.text)
        exit()
    else:
        print('.',end='')