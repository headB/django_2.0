from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
# Create your views here.

def index(request):

    #使用模板文件
    #1.加载模板文件
    #然后返回一个模板对象
    temp = loader.get_template('register/index.html')
    #2.定义模板上下文
    #context = RequestContext(request,{})
    #3. 模板渲染:生成标准的html内容
    ##说明,上一步的注释了,为了就是说明,和django2.0前面的版本不不是同一个用法
    res_html = temp.render({},request)
    #4. 返回给浏览器
    return HttpResponse(res_html)