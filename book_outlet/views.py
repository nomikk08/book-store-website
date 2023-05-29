from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book
from django.db.models import Avg

# Create your views here.


def index(request):
    books = Book.objects.all().order_by('-rating')
    num_books = books.count()
    avg_ratings = books.aggregate(Avg('rating'))
    return render(request, 'book_outlet/index.html', {
        'books': books,
        'total_num_books': num_books,
        'avg_ratings': avg_ratings,
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk= id)
    # except:
    #     raise Http404
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book-detail.html', {
        'title': book.title,
        'rating': book.rating,
        'author': book.author,
        'is_bestseller': book.is_bestselling,
    })
