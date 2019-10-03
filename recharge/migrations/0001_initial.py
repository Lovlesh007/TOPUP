# Generated by Django 2.1.7 on 2019-04-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datacard_recharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data_Card_Number', models.CharField(max_length=15)),
                ('Select_Datacard_Operator', models.CharField(choices=[('Airtel', 'Airtel'), ('Bsnl', 'Bsnl'), ('Idea', 'Idea'), ('Jio', 'Jio'), ('MTNL', 'MTNL'), ('Vodafone', 'Vodafone')], max_length=25)),
                ('Recharge_Amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dth_recharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Select_DTH_Operator', models.CharField(choices=[('Dish TV', 'Dish TV'), ('Videocon', 'Videocon'), ('Tata Sky', 'Tata Sky'), ('Airtel Tv', 'Airtel Tv'), ('Sun Direct', 'Sun Direct')], max_length=50)),
                ('Customer_id', models.CharField(default=0, max_length=25)),
                ('Recharge_Amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Metro_recharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Select_Metro_Type', models.CharField(choices=[('Delhi Metro', 'Delhi Metro'), ('Hyderabad Metro', 'Hyder Metro'), ('Mumbai Metro', 'Mumbai Metro')], max_length=25)),
                ('Card_Number', models.CharField(max_length=25)),
                ('Recharge_Amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mobile_recharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Enter_Your_Mobile_Number', models.CharField(max_length=10)),
                ('Recharge_Type', models.CharField(choices=[('Postpaid', 'Postpaid'), ('Prepaid', 'Prepaid')], max_length=50)),
                ('Operator', models.CharField(choices=[('Airtel', 'Airtel'), ('Vodafone', 'Vodafone'), ('Jio', 'Jio'), ('Idea', 'Idea'), ('Bsnl', 'Bsnl'), ('Uninor', 'Uninor')], max_length=50)),
                ('Circle', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Haryana', 'Haryana'), ('Delhi', 'Delhi'), ('Gujarat', 'Gujarat'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Karnataka', 'Karnataka'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Mumbai', 'Mumbai'), ('Chennai', 'Chennai'), ('Tamil Nadu', 'Tamil Nadu')], max_length=25)),
                ('Recharge_Amount', models.IntegerField(default=10)),
                ('Time_of_Recharge', models.DateTimeField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]