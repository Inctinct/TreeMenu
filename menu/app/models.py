from django.db import models


class MainMenu(models.Model):

    name = models.CharField(max_length=255, blank=True, null=False)

    def __str__(self):
        return self.name


class TreeMenu(models.Model):

    name = models.CharField(max_length=255, blank=True, null=False)
    main_menu = models.ForeignKey(MainMenu, on_delete=models.CASCADE, blank=False, null=False)
    path = models.CharField(max_length=1000, blank=True, null=False)
    parent = models.ForeignKey('self', on_delete=models.SET_DEFAULT, null=True, blank=True, default=0)

    def __str__(self):
        return self.name
