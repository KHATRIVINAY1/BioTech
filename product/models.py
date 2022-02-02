from email.policy import default
from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.utils.html import format_html
from ckeditor_uploader.fields import RichTextUploadingField
from decimal import *
from taggit.managers import TaggableManager
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # parent = models.ForeignKey('self',
    #                            on_delete=models.CASCADE,
    #                            null=True,
    #                            blank=True)
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("products:category", kwargs={"name": self.name})

class Product(models.Model):
    name = models.CharField(max_length=150)
    categories = models.ManyToManyField(Category, blank=True)
    short_description = models.TextField(max_length=200, default="These is no short description for this product")
    description = RichTextUploadingField(blank=True, default="<h1>No Description</h1>",verbose_name ="Product Description")
    additionalInformation = RichTextUploadingField(blank=True, default="<h1>No Additional Information</h1>", verbose_name="Additional Information")
    original_price = models.DecimalField(decimal_places=2, max_digits=20, default=0, blank=True, verbose_name="MRP",validators=[MinValueValidator(Decimal('0.01'))])
    discounted_price = models.DecimalField(decimal_places=2, max_digits=20, default=0 , blank=True,verbose_name="On Hand Price", validators=[MinValueValidator(Decimal('0.01'))])
    quantity = models.IntegerField(default=10)  # available quantity of given product
    featured = models.BooleanField(default=False, verbose_name="On Sale?")  # is product featured?
    tags = TaggableManager(blank=True)  # tags mechanism
    slug = models.SlugField(max_length=200, blank=True)
    published_date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    @property
    def is_featured(self):
        return self.featured

    @property
    def is_available(self):
        return self.quantity > 0

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Picture(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    picture = models.ImageField(upload_to="products/images", null=True, blank=True)
    image_name = models.CharField(max_length=50, blank=True, default="No picture")
    def image_tag(self):
         return format_html('<img src="{}" height=200px />'.format(self.picture.url))

    image_tag.short_description =  f"Image"
    image_tag.allow_tags = True

    def __str__(self):
        return f"{self.image_name}"


class Faq(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    question = models.CharField(max_length=300)
    answer = models.TextField()
    def __str__(self):
        return f"{self.product.name} question"