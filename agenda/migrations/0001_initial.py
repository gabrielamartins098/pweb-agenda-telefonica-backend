import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [

        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),

        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('provincia', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='municipios',
                    to='agenda.provincia'
                )),
            ],
        ),

        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True)),
                ('endereco', models.CharField(max_length=255, blank=True)),
                ('observacoes', models.TextField(blank=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),

                ('usuario', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='contactos',
                    to=settings.AUTH_USER_MODEL
                )),

                ('municipio', models.ForeignKey(
                    on_delete=django.db.models.deletion.SET_NULL,
                    null=True,
                    to='agenda.municipio'
                )),
            ],
        ),

    ]
