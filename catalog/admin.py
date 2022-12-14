from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)

class BookAdminInstance(admin.StackedInline):
    model=Book

class AuthorAdmin(admin.ModelAdmin):
    list_display=(
        'last_name',
        'first_name',
        'date_of_birth',
        'date_of_death'
    )
    fields=[
        'first_name',
        'last_name',
        ('date_of_birth','date_of_death')
    ]

    inlines=[BookAdminInstance]

admin.site.register(Author,AuthorAdmin)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter=('status','due_back')
    list_display=(
        'status',
        'due_back',
        'book',
        'borrower'
    )
    fieldsets=(
        (None,{
            'fields':('book','imprint','id')
        }),
        ('Availability',{
            'fields':('status','due_back','borrower')
        })
    )
class BookInstanceInline(admin.TabularInline):
    model=BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=(
        'title',
        'author',
        'display_genre'
    )
    fields=[
        ('title',
        'author'
        ),
        'summary',
        'genre'
    ]
    inlines=[BookInstanceInline]
