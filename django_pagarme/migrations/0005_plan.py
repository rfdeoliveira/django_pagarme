# Generated by Django 3.0.4 on 2020-09-27 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_pagarme', '0004_pagarme_item_config_available_until'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nome do plano')),
                ('slug', models.SlugField(max_length=128)),
                ('amount', models.PositiveIntegerField(verbose_name='Preço em centavos')),
                ('days', models.IntegerField(verbose_name='Prazo em dias para cobrança das parcelas')),
                ('trial_days', models.IntegerField(default=0, verbose_name='Dias para teste gratuito do plano')),
                ('charges', models.IntegerField(default=None, null=True, verbose_name='Número de cobranças do plano')),
                ('invoice_reminder', models.IntegerField(blank=True, null=True, verbose_name='Dias para aviso do vencimento do boleto')),
                ('available_until', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Desativado em')),
                ('pagarme_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Id do plano no Pagar.me')),
                ('payment_methods', models.CharField(choices=[('boleto', 'Somente Boleto'), ('credit_card', 'Somente Cartão de Crédito'), ('credit_card,boleto', 'Cartão de Crédito ou Boleto')], default='credit_card,boleto', max_length=18, verbose_name='Formas de pagamento')),
            ],
            options={
                'verbose_name': 'Plano de assinatura',
                'verbose_name_plural': 'Planos de assinatura',
            },
        ),
    ]
