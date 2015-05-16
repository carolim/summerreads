from django.contrib import admin
from .models import Book, Quote

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author')

admin.site.register(Book, BookAdmin)
admin.site.register(Quote)
