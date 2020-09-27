# Generated by Django 3.0.4 on 2020-09-28 03:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_pagarme', '0005_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagarme_id', models.CharField(max_length=100, unique=True, verbose_name='Id da assinatura no Pagar.me')),
                ('payment_method', models.CharField(choices=[('boleto', 'Boleto'), ('credit_card', 'Cartão de Crédito')], max_length=11)),
                ('card_id', models.CharField(max_length=64, null=True)),
                ('card_last_digits', models.CharField(max_length=4, null=True)),
                ('initial_status', models.CharField(choices=[('paid', 'Pago'), ('trialing', 'Experimentando'), ('pending_payment', 'Pagamento pendente'), ('unpaid', 'Pagamento não efetuado no prazo'), ('ended', 'Encerrada'), ('canceled', 'Cancelada')], max_length=30)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='django_pagarme.Plan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Assinatura',
                'verbose_name_plural': 'Assinaturas',
            },
        ),
    ]
