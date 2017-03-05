from ajax_select import register, LookupChannel

from profiles.models import Profile


@register('postman_users')
class PostmanUsersLookup(LookupChannel):
    model = Profile.user
    min_length = 2

    def check_auth(self, request):
        # Don't raise a PermissionDenied here
        return

    def get_query(self, q, request):
        return self.model.objects.filter(name=q).order_by('name')
