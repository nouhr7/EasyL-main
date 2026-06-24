from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_ticket_slug_alter_user_num_tel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='syndicat',
            name='gare_associé',
        ),
        migrations.DeleteModel(
            name='vehicule_user',
        ),
    ]
