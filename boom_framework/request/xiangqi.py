def GET(A):
    url='http://471e43500d924b1db674337b2718929b317387663d814be6.changame.ichunqiu.com/js/'+A+'.js'
    return requests.get(url)