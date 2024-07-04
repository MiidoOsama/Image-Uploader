from django.shortcuts import render
from .forms import ImageForm
from .models import Image
# Create your views here.
def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    form = ImageForm()
    image = Image.objects.all()
    return render(request, 'html/home.html', {'form': form, 'image': image})