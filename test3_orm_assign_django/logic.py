from django.views import View, JsonResponse
from django.contrib.auth import LoginRequiredMixin
from django.urls import reverse

from uuid import uuid4

from .myclass import ShareRequest


class DocumentClusterCreateShareView(LoginRequiredMixin, View):

    def post(self, request, pk):
        obj = get_object_or_404(ShareRequest, active=True, owner=self.request.user, id=pk)

        share_guid = uuid4()
        obj.share_link=share_guid
        obj.save()

        full_share_url = request.build_absolute_uri(reverse("share_landing", kwargs={'guid': share_guid}))
        return JsonResponse({'share': full_share_url})
    