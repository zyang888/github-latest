from django.contrib import admin
from myblog.models import Post, Category

class CategoryInline(admin.TabularInline):
	model = Category

class PostAdmin(admin.ModelAdmin):
	inlines = [
		CategoryInline,
		]
# create an InlineModelAdmin to represent Categories on the Post admin view

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

admin.site.register(Post)
admin.site.register(Category)

