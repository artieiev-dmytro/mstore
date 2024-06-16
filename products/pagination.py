from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 100
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 100

    def get_paginated_response(self, data):
        return Response(data)
