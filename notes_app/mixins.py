from django.http import HttpResponseForbidden


class PermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != request.user:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)
