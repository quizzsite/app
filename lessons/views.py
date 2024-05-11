from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_http_methods

from .models import Course

def view_course(request, id):
    course = get_object_or_404(Course, id=id)
    context = {"course": course}
    return render(request, "courses/course.html")

@csrf_exempt
@require_POST
def rtmp_stream(request):
    # Получение данных потока RTMP
    stream_data = request.body
    with open('stream.flv', 'wb') as f:
        f.write(stream_data)
    return HttpResponse('Stream received')

def lesson_video(request, id):
    stream_key = f"course_{id}"
    context = {
        'stream_key': stream_key,
        'rtmp_server': 'rtmp://localhost/live'
    }
    return render(request, 'lessons/video.html', context)
