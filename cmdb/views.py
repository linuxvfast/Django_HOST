from django.shortcuts import render

# Create your views here.
# import os
# print((os.path.dirname(os.path.abspath(__file__))))
from cmdb.create_table import session
from cmdb.create_table import Userinfo
from django.shortcuts import redirect
from cmdb.create_table import Hostinfo

def detail(request):
    nid = request.GET.get('nid')
    sql_info = read_host_info(nid)
    return render(request,'detail.html',{'detail_info':sql_info})

def read_host_info(nid):
    date = session.query(Hostinfo).filter_by(id=nid).first()
    return date

def read_sql(user):
    '''Through the MySQL access to user data'''
    data = session.query(Userinfo).filter_by(user=user).first()
    return data

def get_host():
    host_list = session.query(Hostinfo).filter_by().all()
    # for row in host_list:
    #     print(row.id,row.ip,row.login_port)
    return host_list

def host_admin(request):
    '''The host management page'''
    HOST_LIST = get_host()
    return render(request,'host_admin.html',{'host_list':HOST_LIST})

def login(request):
    '''Logon authentications jump'''
    error_msg = ''
    if request.method == 'POST':
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        data = read_sql(user)
        if data.pwd == pwd:
            return redirect('/host_admin')
        else:
            error_msg = '用户名或密码错误'
    return render(request,'login.html',{'error_msg':error_msg})

if __name__ == '__main__':
    detail(51)