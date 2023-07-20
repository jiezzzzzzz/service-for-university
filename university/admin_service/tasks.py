import xlsxwriter
from celery import shared_task
from .models import DirectionOfTraining
from service.models import Student
from django.db.models import When, Count, IntegerField, Case, Sum
import datetime


@shared_task
def generate_report():
    workbook = xlsxwriter.Workbook(filename=f'Отчет за {datetime.date.today().strftime("%d-%m-%y")}.xlsx', options={'in_memory': True})

    merge_format = workbook.add_format({'align': 'center'})
    cell_format = workbook.add_format()
    cell_format.set_text_wrap()
    cell_format.set_align('center')
    cell_format.set_align('vcenter')

    sheet_labels_directions = [
        ('A1:A2', 'Направления'),
        ('B1:B2', 'Дисциплины'),
        ('C1:E1', 'Куратор'),
        ('C2', 'Фамилия-Имя'),
        ('D2', 'Пол'),
        ('E2', 'Возраст')
    ]
    directions_sheet = workbook.add_worksheet(name='Directions')

    for column, label in sheet_labels_directions:
        if ':' in column:
            directions_sheet.merge_range(column, label, merge_format)
            directions_sheet.set_column(column, 30)
            continue
        directions_sheet.write(column, label, merge_format)

    directions_data = DirectionOfTraining.objects.select_related('curator').prefetch_related('disciplines').all()

    def translate_gender_arg(gender_value: str) -> str:
        gender_dict = {'Man': 'Мужчина', 'Woman': 'Женщина'}
        try:
            gender = gender_dict.get(gender_value)
        except Exception:
            gender = 'не указано'
        return gender

    for number, direction in enumerate(directions_data, start=1):
        disciplines = '\n'.join(f'{num}. {obj.title}' for num, obj in enumerate(direction.disciplines.all(), start=1))
        row_data = [
                    direction.name, disciplines, direction.curator.__str__(),
                    translate_gender_arg(direction.curator.gender), direction.curator.age
        ]
        for column, value in enumerate(row_data):
            directions_sheet.write(number, column, value, cell_format)

    groups_data = Student.objects.prefetch_related('group').all()
    groups_sheet_labels = [
        ('A1', 'Группа'),
        ('B1', 'Студенты'),
        ('C1', 'Мужчин'),
        ('D1', 'Женщин'),
        ('E1', 'Свободных мест')
    ]
    groups_sheet = workbook.add_worksheet(name='Groups')
    groups_sheet.set_column('A1:E2', 30)

    for col_param, label in groups_sheet_labels:
        groups_sheet.write(col_param, label, merge_format)

    for i, group in enumerate(groups_data, start=1):
        students = group.students.all()
        if students.exists():
            students_list = '\n'.join(f'{num}. {obj.get_full_name()}' for num, obj in enumerate(students, start=1))
            count_students = students.annotate(
                is_man=Count(Case(When(gender='Man', then=1), output_field=IntegerField())),
                is_woman=Count(Case(When(gender='Woman', then=1), output_field=IntegerField()))
            ).aggregate(
                men=Sum('is_man'),
                women=Sum('is_woman')
            )
            free_places = 20 - group.students_count
            row_data = [group.name, students_list, count_students.get('men'), count_students.get('women'), free_places]
            for col, value in enumerate(row_data):
                groups_sheet.write(i, col, value, cell_format)
            continue
        row_data = [group.name, 'Студентов нет', 0, 0, 20]
        for col, value in enumerate(row_data):
            groups_sheet.write(i, col, value, cell_format)

    workbook.close()
    return workbook.filename
