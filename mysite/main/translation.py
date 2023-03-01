from .models import Category, SubCategory, ForZhenya, Product
from modeltranslation.translator import register, TranslationOptions

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(ForZhenya)
class ForZhenyaTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'price', 'type_of_money')