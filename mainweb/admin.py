from django.contrib import admin
from . models import *

# Register your models here. 
@admin.register(CurrentAndPreviousEvents)
class CurrentAndPreviousEventsAdmin(admin.ModelAdmin):
    list_display = ('name','date','is_published')
    list_filter = ('date',)
    search_fields = ('name',)
    date_hierarchy = 'date'
    ordering = ('date',)

@admin.register(Banners)
class BannersAdmin(admin.ModelAdmin):
    list_display = ('categories','date','last_updated')
    list_filter = ('date',)
    search_fields = ('categories',)
    date_hierarchy = 'date'
    ordering = ('date',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('Company_name','P_o_box_no','date_created','laste_update')
    list_filter = ('date_created',)
    search_fields = ('Company_name',)
    date_hierarchy = 'date_created'
    ordering = ('date_created',)

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('email','describe_email','date_created','laste_update')
    list_filter = ('date_created',)
    search_fields = ('email',)
    date_hierarchy = 'date_created'
    ordering = ('date_created',)

@admin.register(OfficePhone)
class OfficePhoneAdmin(admin.ModelAdmin):
    list_display = ('Phone_number','describe_Phone_number','date_created','laste_update')
    list_filter = ('date_created',)
    search_fields = ('Phone_number',)
    date_hierarchy = 'date_created'
    ordering = ('date_created',)

@admin.register(sendUsMessage)
class sendUsMessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','massege','date_created')
    list_filter = ('date_created',)
    search_fields = ('name',)
    date_hierarchy = 'date_created'
    ordering = ('date_created',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','date_created','laste_update')
    list_filter = ('date_created',)
    search_fields = ('name',)
    date_hierarchy = 'date_created'
    ordering = ('date_created',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','category','status','created_by','date','date_created','laste_update','is_published')
    list_filter = ('category','status')
    search_fields = ('category',)
    date_hierarchy = 'date_created'
    ordering = ('date_created',)


@admin.register(serviceCategory)
class serviceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','date_created','laste_update')
    list_filter = ('date_created',)
    search_fields = ('name',)
    date_hierarchy = 'date_created'
    ordering = ('date_created',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','category','created_by','date','date_created','laste_update','is_published')
    list_filter = ('category',)
    search_fields = ('category',)
    date_hierarchy = 'date_created'
    ordering = ('date_created',)


@admin.register(background)
class backgroundAdmin(admin.ModelAdmin):
    list_display = ('created_by','date_created','laste_update','is_published')
    list_filter = ('date_created',)
    search_fields = ('date_created',)
    date_hierarchy = 'date_created'
    ordering = ('date_created',)

@admin.register(goal)
class goalAdmin(admin.ModelAdmin):
    list_display = ('created_by','date_created','laste_update','is_published')
    list_filter = ('date_created',)
    search_fields = ('date_created',)
    date_hierarchy = 'date_created'
    ordering = ('date_created',)

@admin.register(mission)
class missionAdmin(admin.ModelAdmin):
    list_display = ('created_by','date_created','laste_update','is_published')
    list_filter = ('date_created',)
    search_fields = ('date_created',)
    date_hierarchy = 'date_created'
    ordering = ('date_created',)

@admin.register(motto)
class mottoAdmin(admin.ModelAdmin):
    list_display = ('created_by','date_created','laste_update','is_published')
    list_filter = ('date_created',)
    search_fields = ('date_created',)
    date_hierarchy = 'date_created'
    ordering = ('date_created',)

@admin.register(vission)
class vissionAdmin(admin.ModelAdmin):
    list_display = ('created_by','date_created','laste_update','is_published')
    list_filter = ('date_created',)
    search_fields = ('date_created',)
    date_hierarchy = 'date_created'
    ordering = ('date_created',)

@admin.register(mainObjective)
class mainObjectiveAdmin(admin.ModelAdmin):
    list_display = ('created_by','date_created','laste_update','is_published')
    list_filter = ('date_created',)
    search_fields = ('date_created',)
    date_hierarchy = 'date_created'
    ordering = ('date_created',)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('Names','tittle','Phone','mobile','email','date_created','laste_update','is_published')
    list_filter = ('tittle',)
    search_fields = ('Names',)
    date_hierarchy = 'date_created'
    ordering = ('-date_created',)


@admin.register(StaffCaption)
class StaffCaptionAdmin(admin.ModelAdmin):
    list_display = ('created_by','date_created','laste_update','is_published')
    list_filter = ('date_created',)
    search_fields = ('date_created',)
    date_hierarchy = 'date_created'
    ordering = ('date_created',)

@admin.register(Parttener)
class ParttenerAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_by','date_created','laste_update','is_published')
    list_filter = ('name',)
    search_fields = ('name',)
    date_hierarchy = 'date_created'
    ordering = ('date_created',)

@admin.register(contactDescription)
class contactDescriptionAdmin(admin.ModelAdmin):
    list_display = ('created_by','date_created','laste_update','is_published')
    list_filter = ('date_created',)
    search_fields = ('date_created',)
    date_hierarchy = 'date_created'
    ordering = ('date_created',)

@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('name','our_link','date_created','laste_update','is_published')
    list_filter = ('date_created',)
    search_fields = ('date_created',)
    date_hierarchy = 'date_created'
    ordering = ('date_created',)