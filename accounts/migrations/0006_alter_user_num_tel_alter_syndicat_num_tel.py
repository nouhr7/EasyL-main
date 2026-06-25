from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_vehicule_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='num_tel',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='syndicat',
            name='num_tel',
            field=models.CharField(max_length=20),
        ),
    ]
