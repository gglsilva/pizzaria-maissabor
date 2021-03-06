# Generated by Django 3.1.4 on 2020-12-28 13:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=200)),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacoes', models.CharField(max_length=300)),
                ('data_pedido', models.DateTimeField(default=django.utils.timezone.now)),
                ('valor', models.FloatField()),
                ('status', models.CharField(choices=[('P', 'Pedido realizado'), ('F', 'Fazendo'), ('E', 'Saiu para entrega')], max_length=1)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='core.cliente')),
                ('produtos', models.ManyToManyField(to='core.Produto')),
            ],
        ),
    ]
