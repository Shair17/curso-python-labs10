from django.shortcuts import render

def home(request):
  return render(request, 'blog/index.html')

def my_posts(request):
  return render(request, 'blog/my-posts.html')

def account(request):
  return render(request, 'blog/account.html')
