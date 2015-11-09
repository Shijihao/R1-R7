from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Book, Author
# Create your views here.


def index(request):
	book_list = Book.objects.all()
	if request.method == 'POST':
		search_name = request.POST.get('author_name','')
		try:
			author = Author.objects.get(Name=search_name)
			book_list_of_author = Book.objects.filter(AuthorID=author.AuthorID)
			context = {'book_list': book_list,'author_lib':book_list_of_author,'author_name':author.Name}
		except:
			book_list_of_author = ['empty']
			context = {'book_list': book_list,'author_empty':book_list_of_author,'author_name':search_name}
	else:
		context = {'book_list': book_list}
	return render(request, 'bookmanager/index.html', context)

def detail(request, book_ISBN):
	book_detail = get_object_or_404(Book, ISBN=book_ISBN)
	author_detail = get_object_or_404(Author, AuthorID=book_detail.AuthorID)
	context = {'book_detail': book_detail,'author_detail':author_detail}
	return render(request, 'bookmanager/detail.html', context)

def delete(request):
	try:
		Book.objects.get(ISBN=request.GET.get('delete_book_ISBN')).delete()
	except:
		pass
	return HttpResponseRedirect('/')

update_book=[]
def update(request):
	if request.method=='GET':
		book_detail=Book.objects.get(ISBN=request.GET.get('update_book_ISBN'))
		update_book.append(book_detail)
		context = {'book_detail': book_detail}
		return render(request, 'bookmanager/update.html', context)
	else:
		try:
			book_detail=update_book[-1]
			author=Author.objects.get(AuthorID=request.POST.get('update_AuthorID'))
		 	book_detail.AuthorID = author
			book_detail.Publisher = request.POST.get('update_Publisher')
			book_detail.PublishDate = request.POST.get('update_PublishDate')
			book_detail.Price = request.POST.get('update_Price')
			book_detail.save()
			return HttpResponseRedirect('/')
		except:
			return render(request, 'bookmanager/fail.html')

def addbook(request):
	if request.method=='POST':
		try:
			add_book = Book(ISBN = request.POST.get('add_ISBN'),
			Title = request.POST.get('add_Title'),
			AuthorID = Author.objects.get(AuthorID=request.POST.get('add_AuthorID')),
			Publisher = request.POST.get('add_Publisher'),
			PublishDate = request.POST.get('add_PublishDate'),
			Price = request.POST.get('add_Price'),)
			add_book.save()
			return render(request, 'bookmanager/success.html')
		except:
			return render(request, 'bookmanager/fail.html')
	return render(request, 'bookmanager/addbook.html')

def addauthor(request):
	if request.method=='POST':
		try:
			add_author = Author(AuthorID = request.POST.get('add_AuthorID'),
			Name = request.POST.get('add_Name'),
			Age = request.POST.get('add_Age'),
			Country = request.POST.get('add_Country'),)
			add_author.save()
			return render(request, 'bookmanager/success.html')
		except:
			return render(request, 'bookmanager/fail.html')
	return render(request, 'bookmanager/addauthor.html')