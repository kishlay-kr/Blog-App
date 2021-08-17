from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    DeleteView,
    UpdateView,
    )

from .forms import BlogModelForm 

#def home(request):
#    post = Post.objects.all()
#    context = {
#        'post' : post            
#        }
#    return render(request, 'home.html',context)

class BlogListView(ListView):
    template_name = 'home.html'
    queryset = Post.objects.all()

class BlogDetailView(DetailView):
    template_name = 'detail.html'
    queryset = Post.objects.all()
    
    

    #def get_object(self):
    #    id_ = self.kwargs.get('id')
    #    return get_object_or_404(Post, id=id_)

#class BlogCreateView(CreateView):
#    template_name = 'create.html'
#    form_class = BlogModelForm
#    queryset = Post.objects.all() 

def BlogCreateView(request):
    form = BlogModelForm()
    if(request.method == 'POST'):
        form = BlogModelForm(request.POST, request.FILES )    
        print(request.FILES)
        if form.is_valid():
            form.save()
        return redirect('../../')

    context = {
        'form' : form
        }

    return render(request, 'create.html', context )



#class BlogUpdateView(UpdateView):
#    template_name = 'create.html'
#    form_class = BlogModelForm
#    queryset = Post.objects.all() 


def BlogUpdateView(request, pk):
    
    obj = get_object_or_404(Post, id=pk)
    form = BlogModelForm(instance = obj)
    if request.method=='POST':

        form = BlogModelForm(request.POST, request.FILES , instance = obj)
        
        if form.is_valid():
            form.save()
        return redirect('../../')
    
    
    context = {
        'form' : form,
        'obj' : obj
        }
    return render(request, 'update.html', context )
    





def BlogDeleteView(request, pk):
    obj = Post.objects.get(id=pk)
    print('\n\n\n')
    print(obj)
    if(request.method == "POST"):
        obj.delete()
        return redirect('/')
    context = { 
        'obj':obj
        }
    return render(request, 'delete.html', context)

