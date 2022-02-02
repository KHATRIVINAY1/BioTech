from product.models import Category

def Categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}