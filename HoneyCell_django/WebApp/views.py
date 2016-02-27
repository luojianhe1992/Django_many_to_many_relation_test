from django.shortcuts import render

# allow us to redirect
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.template import RequestContext, loader

# import the User class in models.py
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# import the auth.models User
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from WebApp.models import *


@login_required
def index(request):
    print("in the index function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/index.html', context)



# registration is normal route, and login is login is "django.contrib.views.login"
def registration(request):
    errors = []
    context = {}
    if request.method == "GET":
        return render(request, 'WebApp/register.html', context)

    # add 'errors' attribute to the context
    context['errors'] = errors

    password1 = request.POST['password']
    password2 = request.POST['password_confirmation']

    if password1 != password2:

        print("Passwords did not match.")

        # error1 happens
        errors.append("Passwords did not match.")

    if len(User.objects.all().filter(username = request.POST['user_name'])) > 0:
        print("Username is already taken.")

        # error2 happens
        errors.append("Username is already taken.")

    if errors:
        return render(request, 'WebApp/register.html', context)

    # create a new user from the valid form data, using create_user function with 2 arguments, 'username' and 'password'
    new_user = User.objects.create_user(username=request.POST['user_name'], password=request.POST['password'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    new_user.save()

    # using 'authenticate' function
    new_user = authenticate(username = request.POST['user_name'], password = request.POST['password'])

    # using 'login' function
    login(request, new_user)

    # using 'redirect' function
    return redirect(reverse('message'))

@login_required
def message(request):
    print("in the message function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/message.html', context)

@login_required
def upload(request):
    print("in the upload function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/upload.html', context)

@login_required
def preprocess(request):
    print("in the preprocess function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/preprocessing.html', context)

@login_required
def visualization(request):
    print("in the visualization function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/knnresult.html', context)

# def logout view
def my_logout(request):
    logout(request)
    return redirect(reverse('index'))

@login_required
def honeycell(request):
    print("in the honeycell function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/honeycell.html', context)

@login_required
def honeycomb(request):
    print("in the honeycomb function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/honeycomb.html', context)

@login_required
def analytics(request):
    print("in the analytics function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/analytics.html', context)


@login_required
def add_publication(request):
    print("in the add_publication function.")

    context = {}
    context['user'] = request.user

    errors = []
    context['errors'] = errors

    if request.method == "GET":
        print("in the GET method of add_publication function.")

        return render(request, 'WebApp/add_publication.html', context)

    else:
        print("in the POST method of show_publications function.")

        publication_name = request.POST['publication_name']

        if not publication_name:
            print("Please type in publication_name.")
            errors.append("Please type in publication name.")

            context['publication_name'] = publication_name

            return render(request, 'WebApp/add_publication.html', context)

        if len(Publication.objects.filter(publication_name=publication_name)):
            print("The publication_name already exist.")
            errors.append("The publication_name already exist.")

            context['publication_name'] = publication_name

            return render(request, 'WebApp/add_publication.html', context)

        new_publication_instance = Publication(publication_name=publication_name)
        new_publication_instance.save()
        print("Already save new_publication_instance.")

        return render(request, 'WebApp/add_publication.html', context)


@login_required
def show_publications(request):
    print("in the function of show_publications.")

    context = {}
    context['user'] = request.user

    data = []
    context['data'] = data

    publications = Publication.objects.all()

    for each_publication in publications:
        each_publication_data = {}
        data.append(each_publication_data)

        each_publication_data['publication'] = each_publication

        if len(FavoritePublication.objects.filter(publication=each_publication)) > 0:
            print("Set to be True.")
            each_publication_data['is_favorite'] = True
        else:
            print("Set to be False.")
            each_publication_data['is_favorite'] = False

    return render(request, 'WebApp/show_publications.html', context)


@login_required
def add_article(request):
    print("in the function of add_article.")

    context = {}
    context['user'] = request.user

    errors = []
    context['errors'] = errors

    if request.method == "GET":
        print("in the GET method of add_article function.")

        return render(request, 'WebApp/add_article.html', context)

    else:
        print("in the POST method of add_article function.")

        article_headline = request.POST['article_headline']
        article_content = request.POST['article_content']
        publication = request.POST['publication']


        if not (article_headline and article_content and publication):
            print("There are some fields which are None.")
            errors.append("There are some fields which are None.")

            context['article_headline'] = article_headline
            context['article_content'] = article_content
            context['publication'] = publication

            return render(request, 'WebApp/add_article.html', context)

        if len(Publication.objects.filter(publication_name=publication)) == 0:
            print("The Publication object does not exist.")
            errors.append("The publication object does not exist.")

            context['article_headline'] = article_headline
            context['article_content'] = article_content
            context['publication'] = publication

            return render(request, 'WebApp/add_article.html', context)

        publication_object = Publication.objects.get(publication_name=publication)

        if len(Article.objects.filter(headline=article_headline)):
            print("The article_headline already exist.")
            errors.append("The article_headline already exist.")

            context['article_headline'] = article_headline
            context['article_content'] = article_content
            context['publication'] = publication

            return render(request, 'WebApp/add_article.html', context)

        if len(Article.objects.filter(content=article_content)):
            print("The article_content already exist.")
            errors.append("The article_content already exist.")

            context['article_headline'] = article_headline
            context['article_content'] = article_content
            context['publication'] = publication

            return render(request, 'WebApp/add_article.html', context)

        # using Publication object to get back all the article linked to it.
        if len(publication_object.article_set.filter(headline=article_headline, content=article_content)):
            print("The publication already publish this article.")
            errors.append("The publication already publish this article.")

            context['article_headline'] = article_headline
            context['article_content'] = article_content
            context['publication'] = publication

            return render(request, 'WebApp/add_article.html', context)

        new_article_instance = Article(headline=article_headline,
                                       content=article_content,
                                       )
        new_article_instance.save()
        print("Already save the new_article_instance.")

        new_article_instance.publications.add(publication_object)
        new_article_instance.save()

        print("Already add the Publication object to the publications attribute of Article object.")

        return render(request, 'WebApp/add_article.html', context)

@login_required
def show_articles(request):
    print("in the function of show_articles.")

    context = {}
    context['user'] = request.user

    data = []
    context['data'] = data

    articles = Article.objects.all()

    for each_article in articles:
        each_article_data = {}
        data.append(each_article_data)

        each_article_data['article'] = each_article
        if len(FavoriteArticle.objects.filter(article=each_article)):
            each_article_data['is_favorite'] = True
        else:
            each_article_data['is_favorite'] = False

    print("%" * 30)
    print(data)
    print("%" * 30)

    return render(request, 'WebApp/show_articles.html', context)


@login_required
def add_favorite_publication(request, publication_id):
    print("in the function of add_favorite_publication.")

    print(request)
    print(publication_id)

    context = {}
    context['user'] = request.user

    publication = Publication.objects.get(id=publication_id)

    new_favorite_publication_instance = FavoritePublication(user=request.user,
                                                            publication=publication)
    new_favorite_publication_instance.save()
    print("Already save new_favorite_publication_instance.")

    return HttpResponseRedirect(reverse("show_publications"))

@login_required
def cancel_favorite_publication(request, publication_id):
    print("in the function of cancel_favorite_publication.")

    print(request)
    print(publication_id)

    context = {}
    context['user'] = request.user

    publication = Publication.objects.get(id=publication_id)

    selected_favorite_publication = FavoritePublication.objects.get(user=request.user,
                                                                    publication=publication)
    selected_favorite_publication.delete()
    print("Already delete selected_favorite_publication.")

    return HttpResponseRedirect(reverse("show_publications"))


@login_required
def add_favorite_article(request, article_id):
    print("in the function of add_favorite_article.")

    print(request)
    print(article_id)

    context = {}
    context['user'] = request.user

    article = Article.objects.get(id=article_id)

    new_favorite_article_instance = FavoriteArticle(user=request.user,
                                                    article=article)
    new_favorite_article_instance.save()
    print("Already save new_favorite_publication_instance.")

    return HttpResponseRedirect(reverse("show_articles"))


@login_required
def cancel_favorite_article(request, article_id):
    print("in the function of cancel_favorite_article.")

    print(request)
    print(article_id)

    article = Article.objects.get(id=article_id)

    selected_favorite_article = FavoriteArticle.objects.get(user=request.user,
                                                            article=article)
    selected_favorite_article.delete()
    print("Already delete selected_favorite_article.")

    return HttpResponseRedirect(reverse("show_articles"))



@login_required
def show_favorite_publications(request):
    print("in the function of show_favorite_publications.")

    context = {}
    context['user'] = request.user

    publications = Publication.objects.all()

    favorite_publications = []
    context['favorite_publications'] = favorite_publications

    for publication in publications:
        if len(FavoritePublication.objects.filter(publication=publication)):
            favorite_publications.append(publication)

    return render(request, 'WebApp/show_favorite_publications.html', context)


@login_required
def show_favorite_articles(request):
    print("in the function of show_favorite_articles.")

    context = {}
    context['user'] = request.user

    articles = Article.objects.all()

    favorite_articles = []
    context['favorite_articles'] = favorite_articles

    for article in articles:
        if len(FavoriteArticle.objects.filter(article=article)):
            favorite_articles.append(article)

    return render(request, 'WebApp/show_favorite_articles.html', context)


from WebApp.forms import *

@login_required
def add_article_using_modelform(request):
    print("in the function add_article_using_modelform.")

    context = {}
    context['user'] = request.user

    errors = []
    context['errors'] = errors

    if request.method == "GET":
        print("in the GET method of add_article_using_modelform function.")

        form = ArticleModelForm()
        context['form'] = form
        return render(request, 'WebApp/add_article_using_modelform.html', context)

    else:
        print("in the POST method of add_article_using_modelform function.")

        form = ArticleModelForm(request.POST, request.FILES)
        context['form'] = form


        if not form.is_valid():
            print("The form is not valid.")
            return render(request, 'WebApp/add_article_using_modelform.html', context)

        if len(Article.objects.filter(headline=form.clean_headline())):
            print("The headline already exist.")
            errors.append("The headline already exist.")

            return render(request, 'WebApp/add_article_using_modelform.html', context)

        if len(Article.objects.filter(content=form.clean_content())):
            print("The content already exist.")
            errors.append("The content already exist.")

            return render(request, 'WebApp/add_article_using_modelform.html', context)

        form.save()
        print("The form already save.")
        return render(request, 'WebApp/add_article_using_modelform.html', {'user': request.user, 'form': ArticleModelForm()})


@login_required
def publication_detail(request, publication_id):
    print("in the function publication_detail.")

    context = {}
    context['user'] = request.user

    publication = Publication.objects.get(id=publication_id)
    context['publication'] = publication

    print("%" * 30)
    print(publication)
    print("%" * 30)

    optional_articles = []
    context['optional_articles'] = optional_articles

    for each_article in Article.objects.all():
        if each_article in publication.article_set.all():
            print("each_article is in the publication's article_set.")
        else:
            print("each_article is not in the publication's article_set.")
            optional_articles.append(each_article)

    return render(request, 'WebApp/publication_detail.html', context)


@login_required
def article_detail(request, article_id):
    print("in the function article_detail.")

    context = {}
    context['user'] = request.user

    article = Article.objects.get(id=article_id)
    context['article'] = article

    print("%" * 30)
    print(article)
    print("%" * 30)

    optional_publications = []
    context['optional_publications'] = optional_publications

    for each_publication in Publication.objects.all():
        if each_publication in article.publications.all():
            print("each_publication is in this article's publications list.")
        else:
            print("each_publication is not in this article's publication list.")
            optional_publications.append(each_publication)

    return render(request, 'WebApp/article_detail.html', context)

@login_required
def add_article_to_publication(request, article_id):
    print("in the function add_article_to_publication.")

    context = {}
    context['user'] = request.user

    article = Article.objects.get(id=article_id)
    context['article'] = article

    # To get multi-value list from request POST
    selected_publications = request.POST.getlist('selected_publications')

    print("%" * 30)
    print(selected_publications)
    print("%" * 30)

    for each_selected_publication in selected_publications:
        print("*" * 20)
        print(each_selected_publication)
        each_selected_publication_object = Publication.objects.get(publication_name=each_selected_publication)
        print(each_selected_publication_object.publication_name)
        print(each_selected_publication_object.publication_time_created)
        print(each_selected_publication_object.publication_time_changed)
        print("*" * 20)

        article.publications.add(each_selected_publication_object)
        print("Already add one Publication object to article's publications.")

    return HttpResponseRedirect(reverse("show_articles"))


@login_required
def add_publication_to_article(request, publication_id):
    print("in the function add_publication_to_article.")

    context = {}
    context['user'] = request.user

    publication = Publication.objects.get(id=publication_id)
    context['publication'] = publication

    # To get multi-value list from request POST
    selected_articles = request.POST.getlist('selected_articles')

    print("%" * 30)
    print(selected_articles)
    print("%" * 30)

    for each_selected_article in selected_articles:
        print("*" * 20)
        print(each_selected_article)
        each_selected_article_headline = each_selected_article.split(',')[0]
        each_selected_article_object = Article.objects.get(headline=each_selected_article_headline)
        print(each_selected_article_object.headline)
        print(each_selected_article_object.content)
        print(each_selected_article_object.article_time_created)
        print(each_selected_article_object.article_time_changed)
        print(each_selected_article_object.publications)
        print("*" * 20)

        publication.article_set.add(each_selected_article_object)
        print("Already add one Article object to publication's article_set.")

    return HttpResponseRedirect(reverse('show_publications'))

