from django.shortcuts import render

from .services import FakePostService


def posts_list(request):
    posts = FakePostService.list()

    return render(
        request=request, 
        template_name="blog/list.html",
        context={"posts":posts}
    )

def post_detail(request, id):
    pass