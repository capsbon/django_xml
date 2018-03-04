import os
import csv
from django.shortcuts import render
from vacancy.models import Vacancies
from django.http import HttpResponse
from django.contrib.auth import views
# Create your views here.


def vacancy_index(request):
    vacancies_data = Vacancies.objects.all()
    context = {
        'vacancies':vacancies_data,
    }
    return render(request, 'vacancy_index.html', context)


def vacancy_edit(request, id):
    if request.method == "GET":
        all_v = Vacancies.objects.all()
        max_id = len(all_v)
        if int(id) > max_id:
            return HttpResponse(" edit id is wrong,Please check it")
        vacancies_data = Vacancies.objects.get(id=id)
        context = {
            'v':vacancies_data
        }
        return render(request, 'vacancy_edit.html', context)
    if request.method == "POST":
        v = Vacancies.objects.get(id=id)
        v.posted = request.POST.get('posted')
        v.save()
        vacancies_data = Vacancies.objects.all()
        context = {
            'vacancies':vacancies_data,
        }
        return render(request, "success.html",context)


def login(request):
    # extra_context是一个字典，它将作为context传递给template，这里告诉template成功后跳转的页面将是/index
    template_response = views.login(request, extra_context={'next': '/vacancies'})
    return template_response


#用户退出
def logout(request):
    #logout_then_login表示退出即跳转至登陆页面，login_url为登陆页面的url地址
    template_response = views.logout_then_login(request,login_url='/vacancies')
    return template_response

def export_csv(request):
    all_v = Vacancies.objects.all()
    base_dir = os.path.abspath(os.path.dirname(__file__))
    csvpath = os.path.join(base_dir,'..','csv_file','vacancies.csv')
    with open(csvpath,'w') as csvfile:
        writer = csv.writer(csvfile)
        #先写入columns_name
        writer.writerow(["id","posted","description","location"])
        for v in all_v:
            single_list = []
            single_list.append(v.id)
            single_list.append(v.posted)
            single_list.append(v.description)
            single_list.append(v.location)
            writer.writerow(single_list)
        csvfile.close()
    with open(csvpath) as f:
        c = f.read()
    response = HttpResponse(c)
    filename = os.path.basename(csvpath)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename={0}'.format(filename)
    return response


