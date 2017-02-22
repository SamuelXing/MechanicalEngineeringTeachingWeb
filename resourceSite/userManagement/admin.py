from django.contrib import admin

from .models import NormalUsers,Payment
# Register your models here.

class NormalUsersAdmin(admin.ModelAdmin):
	fields=('user','signature','membership')
	search_fields = ('userName',)
	list_display = ('id','userName','membership','created_at')

class PaymentUserAdmin(admin.ModelAdmin):
	list_display = ('user','payment','payed_at')
	list_display_links = ('user', )
	search_fields = ('user','payed_at')

admin.site.register(NormalUsers,NormalUsersAdmin)
admin.site.register(Payment,PaymentUserAdmin)