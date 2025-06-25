from django.db.models import QuerySet
from django.http import QueryDict

from apps.book.models import BookModel
from apps.book.serializer import BookSerializer


def filter_book(query:QueryDict)->QuerySet:
    qs = BookModel.objects.all()

    for k, v in query.items():
        match k:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_lt':
                qs = qs.filter(price__lt=v)
            case 'price_gte':
                qs = qs.filter(price__gte=v)
            case 'price_lte':
                qs = qs.filter(price__lte=v)
            case 'rating_gt':
                qs = qs.filter(rating__gt=v)
            case 'rating_lt':
                qs = qs.filter(rating__lt=v)
            case 'rating_gte':
                qs = qs.filter(rating__gte=v)
            case 'rating_lte':
                qs = qs.filter(rating__lte=v)

            case 'title_starts':
                qs = qs.filter(title__startswith=v)
            case 'title_ends':
                qs = qs.filter(title__endswith=v)
            case 'title_contains':
                qs = qs.filter(title__contains=v)
            case 'author_starts':
                qs = qs.filter(author__startswith=v)
            case 'author_ends':
                qs = qs.filter(author__endswith=v)
            case 'author_contains':
                qs = qs.filter(author__contains=v)

            case 'order':
                fields = BookSerializer.Meta.fields
                allowed_fields = (*fields, *[f'-{field}' for field in fields])

                if v not in allowed_fields:
                    raise ValueError(f'detail: Only {allowed_fields} are allowed.')

                qs = qs.order_by(v)

    return qs