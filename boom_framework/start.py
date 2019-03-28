import os
import sys
path=os.path.abspath('.')
if not path+'\\converter' in sys.path:
    sys.path.append(path+'\\converter')
if not path+'\\transmitter' in sys.path:
    sys.path.append(path+'\\transmitter')

class boom_task():

    def __init__(self,c,r,g,re,o,t):
        '''
        converter,request,generator,result_analyzer,obfuscator,transmitter
        '''
        if not c:
            self.converter=None
        elif os.path.exists('./converter/'+c):
            self.converter=c
        else:raise Exception('Parameter error')

        if os.path.exists('./request/'+r):
            self.request='./request/'+r
        else:raise Exception('Parameter error')

        if os.path.exists('./generator/'+g):
            self.generator='./generator/'+g
        else:raise Exception('Parameter error')

        if not re:
            self.result_analyzer=None
        elif os.path.exists('./result_analyzer/'+re):
            self.result_analyzer='./result_analyzer/'+re
        else:raise Exception('Parameter error')

        if not o:
            self.obfuscator=None
        elif os.path.exists('./obfuscator/'+o):
            self.obfuscator='./obfuscator/'+o
        else:raise Exception('Parameter error')

        if not t:
            raise Exception('must have transmitter')
        if os.path.exists('./transmitter/'+t):
            self.transmitter=t
        else:raise Exception('Parameter error')

        self.__check_and_set()
        
    def __check_and_set(self):
        #设置request
        if self.converter:
            exec('from {} import convert'.format(self.converter[:-3]))
            r=eval("convert('"+path.replace('\\','/')+self.request[1:]+"',None)")#返回tuple,(调用语句,函数str)
            if r==False:
                raise Exception('convert request fail')
            else:
                self.request=(r[0],compile(r[1],'<string>', 'exec'))
        else:
            with open(self.request,'r',encoding='utf-8') as f:t=f.read()
            #获取调用str
            self.request=(self.__get_call_str(t.strip().split('\n')[0],True),compile(t,'<string>', 'exec'))
        #设置generator
        with open(self.generator,'r',encoding='utf-8') as f:t=f.read()
        self.generator=(self.__get_call_str(t.strip().split('\n')[0],False),compile(t,'<string>', 'exec'))

        if self.result_analyzer:
            with open(self.result_analyzer,'r',encoding='utf-8') as f:t=f.read()
            self.result_analyzer=(self.__get_call_str(t.strip().split('\n')[0],False),compile(t,'<string>', 'exec'))

        if self.obfuscator:
            with open(self.obfuscator,'r',encoding='utf-8') as f:t=f.read()
            self.obfuscator=(self.__get_call_str(t.strip().split('\n')[0],False).replace('()','({})'),compile(t,'<string>', 'exec'))

    #从首行提取调用字符串
    def __get_call_str(self,first_line,is_request):
        if first_line[:3]!='def' or first_line[-2:]!='):' or first_line.find('(')==-1:
            raise Exception('request method check fail')
        if first_line.count(',')!=0:
            if is_request:
                return first_line[4:first_line.find('(')]+ '('+','.join(['{}' for i in range(first_line.count(',')+1)])+')'
            else:
                return first_line[4:first_line.find('(')]+'({})'
        elif first_line.find('()')!=-1:
            return first_line[4:first_line.find('(')]+'()'
        else:
            return first_line[4:first_line.find('(')]+'({})'


    def run_task(self):
        exec('from {} import get_transmitter'.format(self.transmitter[:-3]))
        with open(path+'/transmitter/'+self.transmitter,'r',encoding='utf-8') as f:t=f.read()
        t=t.strip().split('\n')
        for l in t:
            if l[:4]=='from' or l[:7]=='import':
                eval(l)
            else:
                break
        
        trans=eval('get_transmitter(self.request,self.generator,self.result_analyzer,self.obfuscator)')
        result=trans.run()
        return result

if __name__ == "__main__":
    #设置请求转换器
    #c='rawtorequests.py'
    c=None
    #设置请求
    r='xiangqi.py'
    #设置payload生成器
    g='xiangqi.py'
    #设置请求结果分析器
    re='xiangqi.py'
    #设置混淆器
    #o='testobfu.py'
    o=None
    #设置传输器
    t='muti_thread_http.py'
    #t='single_thread_http.py'


    b=boom_task(c,r,g,re,o,t)
    b.run_task()#启动