# Generated by Django 4.0 on 2022-03-02 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0008_rename_livro_turma_dia_aula_turma_livro_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buildkit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('components', models.CharField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='turma',
            name='livro_1',
        ),
        migrations.RemoveField(
            model_name='turma',
            name='livro_2',
        ),
        migrations.CreateModel(
            name='Courseware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_1', models.CharField(blank=True, max_length=254, null=True)),
                ('book_2', models.CharField(blank=True, max_length=254, null=True)),
                ('distribution_year', models.IntegerField()),
                ('buildkit_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='buildkit_1', to='turmas.buildkit')),
                ('buildkit_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='buildkit_2', to='turmas.buildkit')),
                ('class_grade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='class_grade', to='turmas.turma')),
            ],
        ),
    ]