# -*- coding: utf-8 -*-
import json
from abc import ABC, abstractmethod
from typing import Any, Dict

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin

from ..mixins import ShowDetailMixin, ThisShowDetailMixin, TwitterUserDetailMixin
from ..models import APIModel, Track
from ..views import Search


class APIView(View, ABC):
    model: APIModel

    def get_api_stuff(self) -> Dict[str, Any]:
        return self.get_object().api_dict(verbose=True)

    @abstractmethod
    def get_object(self) -> APIModel:
        raise NotImplementedError()

    def get(self, request, *args, **kwargs):
        resp = HttpResponse(
            json.dumps(self.get_api_stuff(),
                       cls=DjangoJSONEncoder,
                       indent=2),
            content_type='application/json',
        )
        resp['Access-Control-Allow-Origin'] = '*'
        return resp


class ShowAPI(ThisShowDetailMixin, APIView):
    pass


class PrevShowAPI(ShowDetailMixin, APIView):
    view_name = 'vote:api:show'


class TrackAPI(SingleObjectMixin, APIView):
    model = Track


class SearchAPI(APIView, Search):
    def get_api_stuff(self, *a, **k):
        return [t.api_dict() for t in self.get_queryset()]


class TwitterUserAPI(TwitterUserDetailMixin, APIView):
    pass
