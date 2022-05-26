from django.urls import path
from .views import   HomeCreateView, HomeUpdateView, HomeListView, HomeDetailView, HomeDeleteView
urlpatterns = [
    path('',HomeListView.as_view(), name='home'),
    path('detail/<int:pk>',HomeDetailView.as_view(), name='detail'),
    path('edithome/',HomeCreateView.as_view(), name='add'),
    path('delete/<int:pk>',HomeDeleteView.as_view(), name='delete'),
    path('update/<int:pk>',HomeUpdateView.as_view(), name='update'),
    path('search/', HomeListView.as_view(), name="search"),
  
    
    

    # path('admin/'),
    # path('', BookListView.as_view(), name = 'books'),
    # path('search', BookListView.as_view(), name = 'search'),

    # path('edit-book/<int:id>/', BookUpdateView.as_view()),
    # path('delete-book/<int:id>/', BookDeleteView.as_view()),
    # path('edit-book/', BookCreateView.as_view(), name='add'),

    # path('publishers/', PublisherListView.as_view(), name="publishers"),
    # path('authors/', AuthorListView.as_view(), name="authors"),
    # path('books/<title>/', BookListView.as_view(), name="books"),
    # path('authors/create', AuthorCreateView.as_view()),
    # path('authors/update/<pk>/', AuthorUpdateView.as_view()),
    
    
]
