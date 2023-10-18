from django.http import HttpResponseForbidden
from django.shortcuts import redirect
class StaffAccessMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        if not request.user.is_staff and 'staff' in request.path:
            return HttpResponseForbidden("you are not permitted to access this page")
        return self.get_response(request)
        