from django.contrib import admin

from bookmanager.models import Author, Book

class BookAdmin(admin.ModelAdmin):
	fields = ('ISBN', 'Title', 'AuthorID', 'Publisher', 'PublishDate', 'Price')
	
class AuthorAdmin(admin.ModelAdmin):
	fields = ('AuthorID', 'Name', 'Age', 'Country')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
# Register your models here.