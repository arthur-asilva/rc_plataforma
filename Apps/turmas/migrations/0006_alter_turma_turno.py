# Generated by Django 4.0 on 2022-02-16 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0005_alter_turma_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='turno',
            field=models.CharField(choices=[('M', 'Manhã'), ('CM', 'Contraturno manhã'), ('T', 'Tarde'), ('CT', 'Contraturno tarde'), ('N', 'Noite'), ('CN', 'Contraturno noite')], max_length=2),
        ),
    ]
