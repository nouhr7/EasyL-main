import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_num_tel_alter_syndicat_num_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicule',
            name='line',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.line'),
            preserve_default=False,
        ),
    ]
