from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     inlines = [ScopeInline]
#     #pass

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_num = 0
        for form in self.forms:
            if 'is_main' in form.cleaned_data:
                if form.cleaned_data['is_main']:
                    main_num += 1
                else:
                    pass
            else:
                pass
        if main_num == 0:
            raise ValidationError('Укажите основной раздел')
        elif main_num >= 2:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ['id', 'name']
