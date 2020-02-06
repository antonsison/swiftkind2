# Generated by Django 2.2.2 on 2019-07-18 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
        migrations.AddField(
            model_name='homepage',
            name='featured_section_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Featured section 1'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featured_section_1_title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featured_section_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Featured section 2'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featured_section_2_title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_cta_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Hero CTA link'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_text',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_title',
            field=models.CharField(blank=True, max_length=525, null=True),
        ),
    ]