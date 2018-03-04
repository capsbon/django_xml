
import os
import django
from lxml import etree
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from vacancy.models import Vacancies

def parse_xml():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    xmlfile = os.path.join(base_dir,'..','Materials','vacancies.xml')
    f = open(xmlfile,'r')
    xmlread = f.read()
    print(xmlread)
    f.close()
    root = etree.HTML(xmlread)
    vacancies = root.xpath('//vacancy')
    vacancy_len = len(vacancies)
    for i in range(1, vacancy_len+1):
        vacancy_id = root.xpath('//vacancy[%d]/id/text()'%i)
        vacancy_id = ''.join(vacancy_id)
        posted = root.xpath('//vacancy[%d]/posted/text()'%i)
        posted = ''.join(posted)
        description = root.xpath('//vacancy[%d]/description/text()'%i)
        description = ''.join(description)
        location = root.xpath('//vacancy[%d]/location/text()'%i)
        location = ''.join(location)
        v = Vacancies(id=vacancy_id, posted=posted,description=description ,location=location)
        v.save()


if __name__ == "__main__":
    parse_xml()
