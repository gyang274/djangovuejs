# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Job
from .serializers import JobSerializer


# Create your views here.
class JobViewSet(viewsets.ModelViewSet):
    """API endpoint that allows job to be viewed or edited.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobCountView(APIView):
    """A view that returns the count of job in JSON.
    """
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        count = Job.objects.count()
        content = {
            'count': count
        }
        return Response(content)
