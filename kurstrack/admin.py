from django.contrib import admin

# Register your models here.
# from kurstrack.models import *
from django.apps import apps

class AwardingBodyAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	list_filter = ('name')
	oredering = ('name')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('category_id', 'category')
	list_filter = ('category')
	oredering = ('category')

class LevelAdmin(admin.ModelAdmin):
	list_display = ('level_id', 'level_name')
	list_filter = ('level_name')
	oredering = ('level_name')

class InstructorinfoAdmin(admin.ModelAdmin):
	list_display = ('instructor_id', 'first_name', 'last_name', 'profession', 'address', 'phone', 'email', 'website')
	list_filter = ('first_name', 'last_name', 'profession', 'address', 'phone', 'email', 'website')
	oredering = ('first_name', 'last_name', 'profession', 'address')

class RegisterinfoAdmin(admin.ModelAdmin):
	list_display = ('register_id', 'first_name', 'last_name', 'profession', 'address', 'phone', 'email', 'website')
	list_filter = ('first_name', 'last_name', 'profession', 'address', 'phone', 'email', 'website')
	oredering = ('first_name', 'last_name', 'profession', 'address')

class CertificateTypeAdmin(admin.ModelAdmin):
	list_display = ('type_id', 'price', 'type')
	list_filter = ('type')
	oredering = ('type_id')

class CoursedesignAdmin(admin.ModelAdmin):
	list_display = ('design_id', 'design_type')
	list_filter = ('level_name')
	oredering = ('level_name')

class CartAdmin(admin.ModelAdmin):
	list_display = ('stud_id', 'description')
	list_filter = ('stud_id')
	oredering = ('stud_id')

class CertificationAdmin(admin.ModelAdmin):
	list_display = ('certification_id', 'certification_name', 'type')
	list_filter = ('certification_name', 'type')
	oredering = ('type')

class WebcourseinfoAdmin(admin.ModelAdmin):
	list_display = ('w_course_id', 'title', 'rating', 'duration', 'original_price', 'offer_price', 'manipulated_or_not', 'career_path', 'quality', 'quality_type', 'certification')
	list_filter = ('quality', 'quality_type', 'manipulated_or_not', 'career_path', 'category', 'rating', 'certification')
	oredering = ('title', 'quality_type', 'offer_price', 'original_price')

class CoursemoduleAdmin(admin.ModelAdmin):
	list_display = ('module_type', 'module')
	list_filter = ('module_type')
	oredering = ('module')

class LevelAdmin(admin.ModelAdmin):
	list_display = ('order_no', 'w_course', 'quantity', 'total_price', 'shipping_method', 'payment_method', 'id', 'gift_or_not')
	list_filter = ('shipping_method', 'payment_method', 'gift_or_not')
	oredering = ('level_name')


app = apps.get_app_config('kurstrack')

for model_name, model in app.models.items():
    admin.site.register(model)