import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_syndicat_gare_associe_delete_vehicule_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehicule_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_de_creation', models.DateTimeField(auto_now_add=True)),
                ('User_vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
                ('Plaque_vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.vehicule')),
            ],
            options={
                'unique_together': {('User_vehicule', 'Plaque_vehicule')},
            },
        ),
    ]
