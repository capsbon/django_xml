from django.shortcuts import render
from vacancy.models import Vacancies

# 接收POST请求数据
def post_mysql(request):
    id = request.POST.get('id')
    v = Vacancies.objects.get(id=id)
    v.posted = request.POST.get('posted')
    v.save()
    return render(request, "success.html")
