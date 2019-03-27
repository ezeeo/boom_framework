def obfu(payload):
    assert isinstance(payload,tuple)
    r=[]
    for p in payload:
        r.append(str(p)+"hahha")
    return tuple(r)