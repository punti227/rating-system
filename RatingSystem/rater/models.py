from django.db import models


class Products(models.Model):
    """Products Database."""

    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)


class Ratings(models.Model):
    """Rating Database."""

    rating_id = models.IntegerField(primary_key=True)
    rating = models.IntegerField
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
