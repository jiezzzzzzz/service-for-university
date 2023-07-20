import os
from django.conf import settings
from django.http import HttpResponse
from django_celery_results.models import TaskResult
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import DirectionOfTraining, TrainingDiscipline
from service.models import Curator
from .serializers import TrainingDisciplineSerializer, DirectionOfTrainingSerializer
from service.serializers import CuratorSerializer
from .tasks import generate_report
from celery.result import AsyncResult


class StudyDisciplineViewSet(ModelViewSet):
    queryset = TrainingDiscipline.objects.all()
    serializer_class = TrainingDisciplineSerializer
 #   permission_classes = (IsAdminUser,)


class CuratorViewSet(ModelViewSet):
    queryset = Curator.objects.all()
    serializer_class = CuratorSerializer
  #  permission_classes = (IsAdminUser,)


class StudyDirectionViewSet(ModelViewSet):
    queryset = DirectionOfTraining.objects.all()
    serializer_class = DirectionOfTrainingSerializer
   # permission_classes = (IsAdminUser,)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def start_generate_report(request):
    task = generate_report.delay()
    return Response({'message': 'Generation report has been started.', 'task_id': task.id}, status=202)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def show_generate_report_status(request, task_id):
    task = AsyncResult(task_id)
    if task.state == 'PENDING':
        return Response({'message': 'No task found with the given task_id.'}, status=404)
    else:
        return Response({'task': task_id, 'status': task.state}, status=200)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_report(request, task_id):
    task_result = TaskResult.objects.filter(task_id=task_id, status='SUCCESS')
    if task_result.exists():
        result = task_result.first().result
        filename = result.replace('"', '')
        with open(os.path.join(settings.BASE_DIR, filename), 'rb') as file:
            report = file.read()
        response = HttpResponse(report, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = "attachment; filename=UniversityReport.xlsx"
        return response
    cur_status = AsyncResult(task_id).state
    return Response({'message': 'The report has not been generated yet.', 'generation_status': cur_status})