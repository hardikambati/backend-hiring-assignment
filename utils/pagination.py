import math
from rest_framework.pagination import PageNumberPagination


class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'


class PaginationHandlerMixin(object):

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator


    def paginate_queryset(self, queryset):

        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,self.request, view=self)


    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)


    def get_pagination_data(self, qs, limit_val, serializer_class, context:dict = {}):
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_paginated_response(serializer_class(page, many=True, context=context).data)
        else:
            serializer = serializer_class(qs, many=True, context=context)

        data = serializer.data

        if limit_val:
            end_page = math.ceil(len(qs)/int(limit_val))
            total_records = qs.count()
            output = data['results']
        else:
            end_page = None
            total_records = qs.count()
            output = data

        return {
            "last_page_no" : end_page,
            "total_records" : total_records,
            "payload" : output
        }
