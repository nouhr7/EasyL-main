from django.db import models

# Create your models here.

class Profile(models.Model):
    libele = models.TextField(verbose_name="Libelé")
    date_de_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"(Je suis un {self.libele})"
    
class User(models.Model):
    #id_user, last_name, first_name, num_tel, #id_profile
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    num_tel = models.CharField(max_length=20)
 
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

class Gare(models.Model):
    #Gare (id_gare, gare_name, longitude, latitude)
    gare_name= models.CharField(max_length=70)
    longitude = models.DecimalField(max_digits=12, decimal_places=10)
    latitude = models.DecimalField(max_digits=12, decimal_places=10)


class Line(models.Model):
    #Ligne(id_line, line_name, #id_gare, #id_gare)
    line_name = models.CharField(max_length=100)
    gare_start = models.ForeignKey(
        Gare,
        related_name= "gare_départ", on_delete=models.CASCADE
    )
    gare_end = models.ForeignKey(
        Gare,
        related_name= "gare_fin", on_delete=models.CASCADE
    )

class Vehicule(models.Model):
    #Vehicule (plaque, capacité, date_de_mise_en_circulation, type_car, #id_line, #id_proprio)
    plaque = models.CharField(max_length=10, primary_key=True)
    capacity = models.IntegerField()
    date_de_mise_en_circulation = models.DateField()
    type_car = models.CharField(max_length=20)
    
    proprietaire = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

class Syndicat(models.Model):
    #Syndicat (id_syndic, name_syndic, num_tel, date_de_creation, #id_gare)
    name_syndic = models.CharField(max_length=30)
    num_tel = models.CharField(max_length=20)
    date_de_création = models.DateTimeField(auto_now_add=True)

class Ticket(models.Model):
    #Ticket(id_ticket, prix, nombre_de_places, creation_time, statut, #id_line, #id_user, #plaque)
    slug = models.SlugField(default='-')
    prix = models.IntegerField()
    nombres_de_places = models.IntegerField()
    creation_time = models.DateTimeField(auto_now_add=True)
    
    ACTIVE = 'A'
    SUSPEN= 'S'
    USED = "U"
    STATUT_VOYAGE = [
        (ACTIVE , "Active"),
        (SUSPEN , "Suspended"),
        (USED , "Used")
    ]
    statut = models.CharField(max_length=1, choices = STATUT_VOYAGE, default= SUSPEN)
    line_ticket = models.ForeignKey(
        Line, related_name="l_ticket",on_delete=models.CASCADE
    )
    user_ticket= models.ForeignKey(
        User, related_name="ticket",on_delete=models.CASCADE
    )
    vehicule = models.ForeignKey(
        Vehicule, related_name="vehicule_ticket", on_delete=models.CASCADE
    )

class Payment_user(models.Model):
    WAVE = 'W'
    ORANGE = 'O'
    MOOV = 'M'
    MOBILE_MONEY = [
        (WAVE, 'Wave'),
        (ORANGE, 'ORANGE'),
        (MOOV, 'MOOV')
    ]
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_mode = models.CharField(choices=MOBILE_MONEY, max_length=2)
    User_pay = models.ForeignKey(
        User, on_delete=models.PROTECT
    )

class Payment_vehicule(models.Model):
    WAVE = 'W'
    ORANGE = 'O'
    MOOV = 'M'
    MOBILE_MONEY = [
        (WAVE, 'Wave'),
        (ORANGE, 'ORANGE'),
        (MOOV, 'MOOV')
    ]
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_mode = models.CharField(choices=MOBILE_MONEY, max_length=2)
    vehicule_pay = models.ForeignKey(
        Vehicule, on_delete=models.PROTECT
    )

class vehicule_user(models.Model):
    User_vehicule = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
    Plaque_vehicule = models.ForeignKey(
        Vehicule, on_delete=models.CASCADE,
    )

    date_de_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [('User_vehicule', 'Plaque_vehicule')]


class Syndicat_gare(models.Model):
    gare = models.ForeignKey(
        Gare, null= False, on_delete=models.CASCADE
    )
    syndic = models.ForeignKey(
        Syndicat, on_delete=models.CASCADE
    )

    class Meta:
        unique_together = [('gare', 'syndic')]