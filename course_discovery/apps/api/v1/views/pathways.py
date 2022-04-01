""" Views for accessing Pathway data """
from rest_framework import viewsets

from course_discovery.apps.api import serializers
from course_discovery.apps.api.cache import CompressedCacheResponseMixin
from course_discovery.apps.api.permissions import ReadOnlyByPublisherUser


class PathwayViewSet(CompressedCacheResponseMixin, viewsets.ReadOnlyModelViewSet):
    permission_classes = (ReadOnlyByPublisherUser,)
    serializer_class = serializers.PathwaySerializer

    def get_queryset(self):
        lms_id = self.request.query_params.get("lms_id")
        if lms_id is not None:
            queryset = self.get_serializer_class().prefetch_queryset(partner=self.request.site.partner, lms_id=lms_id)
        else:
            queryset = self.get_serializer_class().prefetch_queryset(partner=self.request.site.partner)
        return queryset.order_by('created')
