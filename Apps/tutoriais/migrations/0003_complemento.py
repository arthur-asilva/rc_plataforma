# Generated by Django 4.0 on 2022-01-14 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_alter_usuario_foto'),
        ('tutoriais', '0002_tutorial_nome_alter_tutorial_plano_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complemento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254)),
                ('arquivo', models.CharField(max_length=254)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_postagem', models.DateTimeField(auto_now_add=True, null=True)),
                ('postado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
                ('tutorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutoriais.tutorial')),
            ],
        ),
    ]