
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('Name', models.CharField(max_length=20)),
                ('Mobile', models.IntegerField(max_length=10)),
                ('Email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=15)),
                ('password_recheck', models.CharField(max_length=15)),
            ],
        ),
    ]
