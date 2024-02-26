from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class PostLimitOffsetPagination(LimitOffsetPagination):
    # Тесты без этого не проходят
    def get_paginated_response(self, data):
        if (self.request.GET == {}):
            return Response(data)
        return super().get_paginated_response(data)
