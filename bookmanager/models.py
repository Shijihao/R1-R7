from django.db import models

class Author(models.Model):
	AuthorID = models.CharField(max_length=30, primary_key=True)
	Name = models.CharField(max_length=30)
	Age = models.IntegerField()
	Country = models.CharField(max_length=30)
	def __str__(self):
		return self.AuthorID


class Book(models.Model):
	ISBN = models.CharField(max_length=30, primary_key=True)
	Title = models.CharField(max_length=200)
	AuthorID = models.ForeignKey(Author)
	Publisher = models.CharField(max_length=100)
	PublishDate = models.DateField()
	Price = models.IntegerField()
	def __str__(self):
		return self.ISBN