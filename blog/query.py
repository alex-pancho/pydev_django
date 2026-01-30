from models import Car

# Отримання всіх об'єктів
all_cars = Car.objects.all()

# Фільтрація
toyota_cars = Car.objects.filter(brand__name='Toyota')
recent_cars = Car.objects.filter(created_at__gte='2024-01-01')

# Виключення
not_toyota = Car.objects.exclude(brand__name='Toyota')

# Перший об'єкт
first_car = Car.objects.first()

# Останній об'єкт
last_car = Car.objects.last()

# Отримання за ID
car = Car.objects.get(id=1)  # Викидає DoesNotExist, якщо не знайдено

# Перевірка існування
exists = Car.objects.filter(id=1).exists()

# Кількість
count = Car.objects.count()

# Сортування
by_year = Car.objects.order_by('-year')

# Pagination
page_1 = Car.objects.all()[:10]   # Перші 10
page_2 = Car.objects.all()[10:20]  # З 10 по 20

# Select related (для ForeignKey) - запобіганню N+1
cars = Car.objects.select_related('brand', 'owner').all()
