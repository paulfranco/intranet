from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
			DeleteView,
			DetailView, 
			ListView, 
			CreateView, 
			UpdateView
			)

from .forms import  PostModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Post


# Create
class PostCreateView(FormUserNeededMixin, CreateView):
	form_class = PostModelForm
	template_name = 'posts/create_view.html'
	success_url = '/post/create/'
	#login_url = '/admin/'

	# def form_valid(self, form):
	# 	if self.request.user.is_authenticated():
	# 		form.instance.user = self.request.user
	# 		return super(PostCreateView, self).form_valid(form)
	# 	else:
	# 		form.errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"])
	# 		return self.form_invalid(form)


# def post_create_view(request): # function based view
# 	form = PostModelForm(request.POST or None)
# 		instance = form.save(commit=False)
# 		instance.user = request.user
# 		instance.save()
# 	context = {
# 		"form": form
# 	}
# 	return render(request, 'posts/create_view.html', context)

# Update

class PostUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	queryset = Post.objects.all()
	form_class = PostModelForm
	template_name = 'posts/update_view.html'
	success_url = '/post/'



# Delete

class PostDeleteView(LoginRequiredMixin, DeleteView):
	model = Post
	template_name = 'posts/delete_confirm.html'
	success_url = reverse_lazy("home")






# Retreive

class PostDetailView(DetailView):
	queryset = Post.objects.all()
	#template_name = "posts/detail_view.html"
	

	# def get_object(self):
	# 	print(self.kwargs)
	# 	pk = self.kwargs.get("pk")
	#	get_object_or_404(Post, pk=pk)
	# 	return obj

class PostListView(ListView):
	#template_name = "posts/list_view.html"
	queryset = Post.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(PostListView, self).get_context_data(*args, **kwargs)
		print(context)
		return context



# def post_detail_view(request, pk=None): # pk == id # function based view
# 	obj = Post.objects.get(pk=pk) # Get from database
#	obj = get_object_or_404(Post, pk=pk)
# 	print(obj)
# 	context = {
# 		"object": obj
# 	}
# 	return render(request, "posts/detail_view.html", context)


# def post_list_view(request):
# 	queryset = Post.objects.all()
# 	print(queryset)
# 	for obj in queryset:
# 		print(obj.content)
# 	context = {
# 		'object_list': queryset
# 	}
# 	return render(request, "posts/list_view.html", context)