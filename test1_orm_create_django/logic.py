from django.views import View, JsonResponse
from django.contrib.auth import LoginRequiredMixin
from django.urls import reverse

from uuid import uuid4

from .myclass import DocumentCluster, ShareRequest


class DocumentClusterCreateShareView(LoginRequiredMixin, View):

    def post(self, request, pk):
        obj = get_object_or_404(DocumentCluster, active=True, owner=self.request.user, id=pk)

        share_guid = f"{uuid4()}__{uuid4()}".replace("-", "")
        ShareRequest.objects.create(
            owner=self.request.user,
            shared_object='privateuploads.models.DocumentCluster',
            shared_pk=obj.pk,
            share_link=share_guid
        )

        full_share_url = request.build_absolute_uri(reverse("share_landing", kwargs={'guid': share_guid}))
        return JsonResponse({'share': full_share_url})
    