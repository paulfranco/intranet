from django.shortcuts import render

from .models import Post

# Create your views here.
# Retreive
def post_detail_view(request, id=1):
	obj = Post.objects.get(id=id) # Get from database
	print(obj)
	context = {
		"object": obj
	}
	return render(request, "posts/detail_view.html", context)


def post_list_view(request):
	queryset = Post.objects.all()
	print(queryset)
	for obj in queryset:
		print(obj.content)
	context = {
		'object_list': queryset
	}
	return render(request, "posts/list_view.html", context)