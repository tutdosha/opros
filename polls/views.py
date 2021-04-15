from django.shortcuts import render

from django.http import HttpResponse


def index (request):
    return HttpResponse('Это опрос!')


def detail(request, question_id):
    return HttpResponse('Вопрос номер %' % question_id)
