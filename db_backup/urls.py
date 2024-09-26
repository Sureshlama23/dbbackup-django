from django.contrib import admin
from django.urls import path
from db_backup.scheduler import scheduler

urlpatterns = [
    path("admin/", admin.site.urls),
] 
# schedular for database backup
scheduler.start()