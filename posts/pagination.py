from rest_framework.pagination import PageNumberPagination


class PostPageLimit(PageNumberPagination):
    page_size = 4
