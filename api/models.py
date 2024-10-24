from django.db import models
from django.contrib.auth.models import User

from django.db import models

class City(models.Model):
    name = models.CharField(verbose_name=("İl"), max_length=50)

    def __str__(self):
        return self.name

class District(models.Model):
    city = models.ForeignKey(City, verbose_name=("İl"), on_delete=models.CASCADE, related_name="districts")
    name = models.CharField(verbose_name=("İlçe"), max_length=50)

    def __str__(self):
        return self.name

class Neighborhood(models.Model):  # Mahalle modelini ekleyin
    district = models.ForeignKey(District, verbose_name=("İlçe"), on_delete=models.CASCADE, related_name="neighborhoods")
    name = models.CharField(verbose_name=("Mahalle"), max_length=50)

    def __str__(self):
        return self.name

class Street(models.Model):
    neighborhood = models.ForeignKey(Neighborhood, verbose_name=("Mahalle"), on_delete=models.CASCADE, related_name="streets")
    name = models.CharField(verbose_name=("Cadde"), max_length=50)

    def __str__(self):
        return self.name

class Farmer(models.Model):
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE, related_name="farmers")
    Id_number = models.CharField(verbose_name=("Id Number"), max_length=50)
    phone = models.CharField(verbose_name=("Phone"), max_length=50, unique=True)
    city = models.ForeignKey(City, verbose_name=("City"), on_delete=models.CASCADE, related_name="farmers")
    district = models.ForeignKey(District, verbose_name=("District"), on_delete=models.CASCADE, related_name="farmers")
    neighborhood = models.ForeignKey(Neighborhood, verbose_name=("Neighborhood"), on_delete=models.CASCADE, related_name="farmers")
    street = models.ForeignKey(Street, verbose_name=("Street"), on_delete=models.CASCADE, related_name="farmers")
    address = models.TextField(verbose_name=("address"))
    photo = models.FileField(verbose_name=("Profile Photo"), upload_to="profiles/", max_length=255)

    def __str__(self):
        return self.phone

# Partner : User + Tel + TCKN + İl + İlçe + Adres + Profil Fotoğrafı
class Partner(models.Model):
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE, related_name="partners")
    Id_number = models.CharField(verbose_name=("Id Number"), max_length=50)
    phone = models.CharField(verbose_name=("Phone"), max_length=50, unique=True)
    city = models.ForeignKey(City, verbose_name=("City"), on_delete=models.CASCADE, related_name="partners")
    district = models.ForeignKey(District, verbose_name=("District"), on_delete=models.CASCADE, related_name="partners")
    neighborhood = models.ForeignKey(Neighborhood, verbose_name=("Neighborhood"), on_delete=models.CASCADE, related_name="partners")
    street = models.ForeignKey(Street, verbose_name=("Street"), on_delete=models.CASCADE, related_name="partners")
    address = models.TextField(verbose_name=("address"))
    photo = models.FileField(verbose_name=("Profile Photo"), upload_to="partner-profiles/", max_length=255)

    def __str__(self):
        return self.phone

# Arazi : Adı + Ortağı  + Ada + Parsel + Metrekare + Fotoğrafı + Toplam bitki + Bitki Tür sayısı + Bitki çeşit sayısı + Dikim tarihi + Tahmini hasat miktarı
class Land(models.Model):
    name = models.CharField(verbose_name=("Land"), max_length=50)
    farmer = models.ForeignKey(Farmer, verbose_name=("Farmer"), related_name="lands", on_delete=models.CASCADE, blank=True, null=True)
    partner = models.ForeignKey(Partner, verbose_name=("Partner"), related_name="lands", on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City, verbose_name=("City"), on_delete=models.CASCADE, related_name="lands")
    district = models.ForeignKey(District, verbose_name=("District"), on_delete=models.CASCADE, related_name="lands")
    neighborhood = models.ForeignKey(Neighborhood, verbose_name=("Neighborhood"), on_delete=models.CASCADE, related_name="lands")
    street = models.ForeignKey(Street, verbose_name=("Street"), on_delete=models.CASCADE, related_name="lands")
    block = models.CharField(verbose_name=("Block"), max_length=50)
    parcel = models.CharField(verbose_name=("Parcel"), max_length=50)
    land_area = models.DecimalField(verbose_name=("Land Area"), max_digits=10, decimal_places=2, default=1)
    photo = models.FileField(verbose_name=("Photo"), upload_to="land-photos/", max_length=100)
    total_plants = models.PositiveIntegerField(verbose_name=("Total Plants"), default=0)
    total_plant_species = models.PositiveIntegerField(verbose_name=("Total Plant Species"), default=0)
    total_plant_variety = models.PositiveIntegerField(verbose_name=("Total Plant Variety"), default=0)
    estimated_harvest = models.DecimalField(verbose_name=("Estimated Harvest/KG"), max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

class LandDetail(models.Model):
    land = models.ForeignKey(Land, verbose_name=("Land"), related_name="land_details", on_delete=models.CASCADE)
    plants = models.PositiveIntegerField(verbose_name=("Plants"), default=0)
    plant_species = models.PositiveIntegerField(verbose_name=("Plant Species"), default=0)
    plant_variety = models.PositiveIntegerField(verbose_name=("Plant Variety"), default=0)
    estimated_harvest = models.DecimalField(verbose_name=("Estimated Harvest/KG"), max_digits=10, decimal_places=2, default=0)
    planting_date = models.DateField(verbose_name=("Planting Date"))

    def __str__(self):
        return self.land.name

# Yapılacaklar listesi : Adı + Sıklığı + tarih + saat
class TodoList(models.Model):
    land = models.ForeignKey(Land, verbose_name=("Land"), related_name="todo_lists", on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, verbose_name=("Farmer"), related_name="todo_lists", on_delete=models.CASCADE, blank=True, null=True)
    partner = models.ForeignKey(Partner, verbose_name=("Partner"), related_name="todo_lists", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(verbose_name=("Title"), max_length=50)
    date = models.DateField(verbose_name=("Date"))
    time = models.TimeField(verbose_name=("Time"))
    is_active = models.BooleanField(verbose_name="Is Active", default=True)

    def __str__(self):
        return self.land.name

# Hava Durumu Alarmı: Adı + max sıcaklık + Min Sıcaklık
class WeatherAlert(models.Model):
    farmer = models.ForeignKey(Farmer, verbose_name=("Farmer"), related_name="weather_alerts", on_delete=models.CASCADE, blank=True, null=True)
    partner = models.ForeignKey(Partner, verbose_name=("Partner"), related_name="weather_alerts", on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City, verbose_name=("City"), on_delete=models.CASCADE, related_name="weather_alerts")
    district = models.ForeignKey(District, verbose_name=("District"), on_delete=models.CASCADE, related_name="weather_alerts")
    neighborhood = models.ForeignKey(Neighborhood, verbose_name=("Neighborhood"), on_delete=models.CASCADE, related_name="weather_alerts")
    street = models.ForeignKey(Street, verbose_name=("Street"), on_delete=models.CASCADE, related_name="weather_alerts")
    max_temperature = models.DecimalField(verbose_name=("Max Tempareture"), max_digits=4, decimal_places=2, default=0)
    min_temperature = models.DecimalField(verbose_name=("Min Tempareture"), max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        if self.farmer:
            return self.farmer
        if self.partner:
            return self.partner
