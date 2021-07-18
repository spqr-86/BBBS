from ..models.place import Place


def tags_by_city_filter(request):
    if not request.user.is_anonumous:
        user_city = request.user.city
        places_by_city = list(Place.objects.filter(city=user_city))
        tags_queryset = [places_by_city.tags.all() for places_by_city in places_by_city]
        tags = [tag for tag_queryset in tags_queryset for tag in tag_queryset]
        return tags
    city = request.data.get('city')
    if city is not None:
        return request.queryset.filter(city=city)
