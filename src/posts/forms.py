from django import forms

from .models import Post

class PostModelForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			#"user",
			"content"
		]
		#exclude = ["user"]

	# def clean_content(self, *args, **kwargs):
	# 	content = self.cleaned_data.get("content")
	# 	if content == 'abc':
	# 		raise: forms.ValidationError("Cannot be ABC")
	# 	return content 