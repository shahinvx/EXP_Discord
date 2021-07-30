# Generated by Django 3.2 on 2021-07-29 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discord_Apps_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('App_name', models.CharField(max_length=50, unique=True)),
                ('App_Token', models.CharField(max_length=300, unique=True)),
                ('App_ID', models.CharField(max_length=300, unique=True)),
                ('App_Pub_Key', models.CharField(max_length=300, unique=True)),
                ('App_Invitation_Link', models.CharField(max_length=300, unique=True)),
                ('descript', models.CharField(blank=True, default='nothing', max_length=100, null=True)),
            ],
            options={
                'db_table': 'prod_Details',
                'managed': True,
            },
        ),
    ]
