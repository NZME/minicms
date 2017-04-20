from django.contrib import admin
from models import *
from django.http import HttpResponseRedirect, HttpResponse

#from tinymce.widgets import AdminTinyMCE

class CustomizedModelAdmin(admin.ModelAdmin):
    
    # def save_model(self, request, obj, form, change):
    #     if request.user.has_perm('minicms.%s_can_edit'%(obj.__class__.__name__,)):
    #         obj.save()
    #     else:
    #         raise Exception('no permission to edit')
    #         return HttpResponse('no permissions to edit')
    pass



class PageContentAdmin(CustomizedModelAdmin):
    list_display = ('page', 'container', 'content')
    list_filter = ('page',)
    search_fields = ['content']

    #formfield_overrides = {
    #    models.TextField: {'widget': AdminTinyMCE},
    #}


class PageContentInlineAdmin(admin.TabularInline):
    model = PageContent
    extra = 0


#admin.site.register(PageContent, PageContentAdmin)


class PageAdmin(CustomizedModelAdmin):
    list_display = ('name', 'url',)
    list_filter = ('url',)
    search_fields = ['name', 'url']
    inlines = [PageContentInlineAdmin]

    fieldsets = (
        (None, {
           'fields': ('name', 'url')
        }),
        ('Meta Content', {
            'fields': ('title', 'keywords', 'description',),
        }),
    )


admin.site.register(Page, PageAdmin)

