# Generated by Django 4.0 on 2021-12-18 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_todo_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.IntegerField(choices=[(1, ' 1️⃣'), (2, '2️⃣'), (3, '3️⃣'), (4, '4️⃣'), (5, '5️⃣'), (6, '6️⃣'), (7, '7️⃣'), (8, '8️⃣'), (9, '9️⃣'), (10, '🔟')], default=1, max_length=2),
        ),
    ]