from django.contrib import admin
from myblog.models import Post, Category

class CategoryInline(admin.TabularInline):
	model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
# create an InlineModelAdmin to represent Categories on the Post admin view
	inlines = [
		CategoryInline,
		]

class CategoryAdmin(admin.ModelAdmin):
	inlines = [
		CategoryInline,
		] 
	exclude = ('posts',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

