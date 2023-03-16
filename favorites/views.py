import json

from django.contrib import auth
from django.http import HttpResponse
from django.views import View
from .models import FavoriteProduct


class FavoriteView(View):
    model = None

    def post(self, request, pk):
        user = auth.get_user(request)
        favorite, created = self.model.objects.get_or_create(user=user, obj_id=pk)
        if not created:
            favorite.delete()

        return HttpResponse(
            json.dumps({
                "result": created,
                "count": self.model.objects.filter(obj_id=pk).count()
            }),
            content_type="application/json"
        )
