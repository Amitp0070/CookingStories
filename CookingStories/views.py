from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
# pagination
from django.core.paginator import Paginator
from .models import Article, Topic
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home_view(request):
    # get all articles
    article_list = Article.objects.order_by('-created_at')[:3]
    topic_list = Topic.objects.all()
    latest_article = Article.objects.order_by('-created_at')[:4]
    # pagination
    paginator = Paginator(article_list, 8)
    page = request.GET.get('p',1)
    # get articles for this page
    articles = paginator.get_page(page)
    ctx = {
        'articles': articles,
        'topics': topic_list,
        'latest_article': latest_article,
    }
    return render(request, 'Cookingstories/home.html', ctx)






@login_required
def add_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        topic_id = request.POST.get('topic')
        topic = Topic.objects.get(id=topic_id) # get topic object from id
        image = request.FILES.get('image')
        author = request.user
        if len(title) < 10:
            messages.error(request, 'Title must be at least 3 characters.')
            return redirect('add') 
        if len(content) < 50:
            messages.error(request, 'Content must be at least 50 characters.')
            return redirect('add')
        if not image:
            messages.error(request, 'Image is required.')
            return redirect('add')
        # create article
        article = Article(title = title, image = image,
                        content = content, topic = topic, author = author)
        article.save()
        messages.success(request, 'Article created successfully.')
        return redirect('my_articles')
    
    else:
        form = ArticleForm()
    
    return render(request, 'Cookingstories/add.html', {
        'form': form,
        'topics': Topic.objects.all()
    })


@login_required
def my_articles(request):
    # get user articles
    article_list = Article.objects.filter(author = request.user)
    paginator = Paginator(article_list, 8)
    page = request.GET.get('p',1)
    ctx = {'articles' : paginator.get_page(page)}
    return render(request, 'Cookingstories/my_articles.html', ctx)

@login_required
def inc_like(request, id):
    article = Article.objects.get(id=id)
    article.likes += 1
    article.save()
    return redirect('detail', id=id)

def detail_view(request, id):
    ctx = {'article': Article.objects.get(id=id)}
    return render(request, 'Cookingstories/detail.html', ctx)

@login_required
def edit_view(request, id):
    if request.method == "POST":
        article = Article.objects.get(id=id) 
        title = request.POST.get('title')
        content = request.POST.get('content')
        topic_id = request.POST.get('topic')
        topic = Topic.objects.get(id=topic_id) # get topic object from id
        image = request.FILES.get('image')
        author = request.user
        if len(title) < 3:
            messages.error(request, 'Title must be at least 3 characters.')
            return redirect('edit', id=id) 
        if len(content) < 50:
            messages.error(request, 'Content must be at least 50 characters.')
            return redirect('edit', id=id) 
        if not image: # if no image is uploaded, use the old one
            image = article.image
        # edit article
        article.title = title
        article.content = content
        article.topic = topic
        article.image = image
        article.save()
        messages.success(request, 'Article updated successfully.')
        return redirect('my_articles')
    else:
        form = ArticleForm()
    return render(request, 'Cookingstories/add.html',{
        'article': Article.objects.get(id=id),
        'form': form,  # current article
        'topics': Topic.objects.all()           # all topics
    })

@login_required
def delete_view(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    messages.success(request, 'Article deleted successfully.')
    return redirect('my_articles')



def register_view(request):
    # agar form submit ho to
    if request.method == "POST":
        # form se data alag alag variable me store karo
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        cpassword = request.POST.get('cpass')
        if password != cpassword or len(password) == 0 or len(cpassword) == 0:
            messages.error(request, "Passwords do not match")
            return redirect('register')
        # more validation can be added here
        # check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')
        # user create karo
        user = User.objects.create_user(username, email, password)
        messages.success(request, "Account created successfully")
        return redirect('login')
    else:
        return render(request, 'accounts/register.html')

    
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        if len(username) == 0 or len(password) == 0:
            messages.error(request, "Bad Login details!")
            return redirect('login')
        # user authenticate karo
        user = authenticate(request,username=username, password=password)
        if user is not None:
            messages.success(request, "Logged in successfully")
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')


# def profile(request):
#     return render(request, 'accounts/profile.html')
# def profile_view(request):
#     return render(request, 'accounts/profile.html')



def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Send an email (optional)
        send_mail(
            subject,
            f'Message from {name} <{email}>:\n\n{message}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        messages.success(request, 'Your message has been sent successfully!')
    
    return render(request, 'Cookingstories/contact.html')






def topic_articles(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    articles = Article.objects.filter(topic=topic)
    return render(request, 'Cookingstories/articles_by_topic.html', {'topic': topic, 'articles': articles})




@require_POST
@csrf_exempt
def rate_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        rating = int(request.POST.get('rating', 0))

        if 1 <= rating <= 5:  # Ensure rating is between 1 and 5
            article.update_rating(rating)
            return JsonResponse({'success': True, 'new_rating': article.rating})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid rating value.'})

    except Article.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Article not found.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})



def about_view(request):
    return render(request, 'Cookingstories/about.html')