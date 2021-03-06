# Generated by Django 4.0.4 on 2022-05-11 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married')], max_length=50)),
                ('is_contributed', models.BooleanField(blank=True, null=True)),
                ('is_baptized', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
            },
        ),
        migrations.CreateModel(
            name='Priest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('main', 'Main'), ('deputy', 'Deputy'), ('normal', 'Normal')], max_length=50)),
            ],
            options={
                'verbose_name': 'Priest',
                'verbose_name_plural': 'Priests',
            },
        ),
        migrations.CreateModel(
            name='SubParish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'SubParish',
                'verbose_name_plural': 'SubParishs',
            },
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=25)),
                ('rank', models.CharField(choices=[('above', 'Above'), ('standard', 'Standard'), ('below', 'Below')], max_length=50)),
                ('type', models.CharField(choices=[('tithe', 'Tithe'), ('construction', 'Construction'), ('thanksgiving', 'Thanksgiving')], max_length=50)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parish.member')),
            ],
            options={
                'verbose_name': 'Contribution',
                'verbose_name_plural': 'Contributions',
            },
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('chairman', 'Chairman'), ('deputy_chairman', 'Deputy Chairman'), ('general_secretary', 'General Secretary'), ('deputy_secretary', 'Deputy Secretary'), ('accountant', 'Accountant'), ('member', 'Member')], max_length=50)),
                ('member', models.ForeignKey(default='MEMBER', on_delete=django.db.models.deletion.CASCADE, to='parish.member')),
            ],
            options={
                'verbose_name': 'Community',
                'verbose_name_plural': 'Communities',
            },
        ),
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('chairman', 'Chairman'), ('deputy_chairman', 'Deputy Chairman'), ('general_secretary', 'General Secretary'), ('deputy_secretary', 'Deputy Secretary'), ('accountant', 'Accountant')], max_length=50)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parish.member')),
            ],
            options={
                'verbose_name': 'Committee',
                'verbose_name_plural': 'Committee',
            },
        ),
    ]
