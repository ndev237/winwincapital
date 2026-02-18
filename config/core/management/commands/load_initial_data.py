# core/management/commands/load_initial_data.py

"""
Commande pour charger des données initiales de démonstration
Usage: python manage.py load_initial_data
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from config.pages.models import Partner, Agency, SavingsProduct, FinancingProduct
from config.blog.models import Category, BlogPost



class Command(BaseCommand):
    help = 'Charge des données initiales pour Win Win Capital'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Chargement des données initiales...'))

        # Partenaires financiers
        partners_financial = [
            {'name': 'CCA – Crédit Communautaire d\'Afrique', 'category': 'financial'},
            {'name': 'Afriland First Bank', 'category': 'financial'},
            {'name': 'Caisse Centrale', 'category': 'financial'},
        ]

        # Partenaires académiques
        partners_academic = [
            {'name': 'IUEs/Insam – Institut Universitaire et Stratégique de l\'Estuaire', 'category': 'academic'},
            {'name': 'UPE – Université Privée de l\'Estuaire', 'category': 'academic'},
            {'name': 'ESSA – École Supérieure des Sciences Appliquées', 'category': 'academic'},
            {'name': 'ENIET de l\'Excellence', 'category': 'academic'},
            {'name': 'ENIEG de l\'Excellence', 'category': 'academic'},
        ]

        # Partenaires formation
        partners_training = [
            {'name': 'CPE – Club Prépa Emploi', 'category': 'training'},
            {'name': 'CFPMP – Centre de Formation Professionnelle des Métiers Pratiques', 'category': 'training'},
        ]

        # Partenaires économiques
        partners_economic = [
            {'name': 'Win Win Logistique', 'category': 'economic'},
        ]

        # Créer tous les partenaires
        for idx, partner_data in enumerate(
                partners_financial + partners_academic + partners_training + partners_economic):
            Partner.objects.get_or_create(
                name=partner_data['name'],
                defaults={
                    'category': partner_data['category'],
                    'order': idx,
                    'is_active': True
                }
            )

        self.stdout.write(self.style.SUCCESS(
            f'✓ {len(partners_financial + partners_academic + partners_training + partners_economic)} partenaires créés'))

        # Agences
        agencies = [
            {
                'name': 'Agence Principale - Douala',
                'address': 'Rue du Commerce, Akwa',
                'city': 'Douala',
                'phone': '+237 233 XXX XXX',
                'email': 'douala@winwincapital.africa',
                'is_main': True,
                'latitude': 4.0511,
                'longitude': 9.7679,
            },
            {
                'name': 'Agence Bonanjo',
                'address': 'Boulevard de la Liberté',
                'city': 'Douala',
                'phone': '+237 233 YYY YYY',
                'email': 'bonanjo@winwincapital.africa',
                'is_main': False,
                'latitude': 4.0469,
                'longitude': 9.6978,
            },
        ]

        for idx, agency_data in enumerate(agencies):
            Agency.objects.get_or_create(
                name=agency_data['name'],
                defaults={**agency_data, 'order': idx}
            )

        self.stdout.write(self.style.SUCCESS(f'✓ {len(agencies)} agences créées'))

        # Produits d'épargne
        savings_products = [
            {
                'name': 'Compte Courant',
                'description': 'Compte pour vos opérations quotidiennes avec une gestion flexible de vos fonds.',
                'features': 'Accès aux fonds à tout moment\nCarnet de chèques\nRetraits illimités\nRelevés mensuels',
                'minimum_amount': 0,
                'icon_class': 'current',
            },
            {
                'name': 'Compte Épargne',
                'description': 'Constitution progressive de votre capital avec rémunération attractive.',
                'features': 'Taux d\'intérêt compétitif\nCapitalisation des intérêts\nRetraits planifiés\nSécurité maximale',
                'minimum_amount': 10000,
                'interest_rate': '3% par an',
                'icon_class': 'savings',
            },
            {
                'name': 'Compte Scolaire',
                'description': 'Anticipez les frais académiques de vos enfants en épargnant régulièrement.',
                'features': 'Épargne programmée\nObjectif ciblé\nBonus de fidélité\nConseil personnalisé',
                'minimum_amount': 5000,
                'interest_rate': '2.5% par an',
                'icon_class': 'school',
            },
            {
                'name': 'Compte PME',
                'description': 'Gestion structurée pour les professionnels et entreprises.',
                'features': 'Gestion multi-utilisateurs\nRelevés détaillés\nConseil professionnel\nServices dédiés',
                'minimum_amount': 50000,
                'icon_class': 'business',
            },
        ]

        for idx, product_data in enumerate(savings_products):
            SavingsProduct.objects.get_or_create(
                name=product_data['name'],
                defaults={**product_data, 'order': idx}
            )

        self.stdout.write(self.style.SUCCESS(f'✓ {len(savings_products)} produits d\'épargne créés'))

        # Produits de financement
        financing_products = [
            {
                'name': 'Crédit Personnel',
                'description': 'Financement pour vos projets personnels : équipement, événements, imprévus.',
                'features': 'Montant adapté à votre capacité\nDurée flexible\nTaux compétitif\nRéponse rapide',
                'max_amount': 5000000,
                'duration_range': '3 à 24 mois',
                'interest_rate': 'À partir de 8%',
                'requirements': 'Justificatif de revenus stables\nPièce d\'identité\nJustificatif de domicile\nGarantie selon montant',
                'icon_class': 'personal',
            },
            {
                'name': 'Crédit Scolaire',
                'description': 'Financement des frais académiques pour assurer la réussite de vos enfants.',
                'features': 'Calendrier de paiement adapté\nMontant selon besoin\nRemboursement progressif\nAccompagnement dédié',
                'max_amount': 3000000,
                'duration_range': '6 à 12 mois',
                'interest_rate': 'À partir de 7%',
                'requirements': 'Justificatif d\'inscription\nPièce d\'identité\nJustificatif de revenus\nGarantie parentale',
                'icon_class': 'school',
            },
            {
                'name': 'Crédit Activité / PME',
                'description': 'Financement de vos activités commerciales et développement d\'entreprise.',
                'features': 'Montant adapté au projet\nDurée selon activité\nSuivi personnalisé\nConseil business',
                'max_amount': 15000000,
                'duration_range': '12 à 36 mois',
                'interest_rate': 'À partir de 9%',
                'requirements': 'Business plan\nBilan financier\nRegistre de commerce\nGaranties matérielles/personnelles',
                'icon_class': 'business',
            },
        ]

        for idx, product_data in enumerate(financing_products):
            FinancingProduct.objects.get_or_create(
                name=product_data['name'],
                defaults={**product_data, 'order': idx}
            )

        self.stdout.write(self.style.SUCCESS(f'✓ {len(financing_products)} produits de financement créés'))

        # Catégories de blog
        categories = [
            {'name': 'Éducation financière', 'slug': 'education-financiere',
             'description': 'Comprendre les bases de la finance'},
            {'name': 'Gestion budgétaire', 'slug': 'gestion-budgetaire',
             'description': 'Conseils pour bien gérer son budget'},
            {'name': 'Épargne', 'slug': 'epargne', 'description': 'Stratégies d\'épargne efficaces'},
            {'name': 'Crédit responsable', 'slug': 'credit-responsable',
             'description': 'Utiliser le crédit intelligemment'},
            {'name': 'Actualités', 'slug': 'actualites', 'description': 'Dernières nouvelles de Win Win Capital'},
        ]

        for idx, cat_data in enumerate(categories):
            Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={**cat_data, 'order': idx}
            )

        self.stdout.write(self.style.SUCCESS(f'✓ {len(categories)} catégories de blog créées'))

        # Articles de blog (exemples)
        education_category = Category.objects.get(slug='education-financiere')
        budget_category = Category.objects.get(slug='gestion-budgetaire')

        articles = [
            {
                'title': 'Les 5 règles d\'or de l\'épargne',
                'slug': 'les-5-regles-or-epargne',
                'category': education_category,
                'excerpt': 'Découvrez les principes fondamentaux pour construire votre épargne de manière efficace et durable.',
                'content': '''
                <h2>Introduction</h2>
                <p>L'épargne est la base de toute stabilité financière. Voici les 5 règles essentielles à respecter.</p>

                <h3>1. Épargnez en premier</h3>
                <p>Mettez de côté une partie de vos revenus dès que vous les recevez, avant toute dépense.</p>

                <h3>2. Fixez-vous des objectifs clairs</h3>
                <p>Définissez précisément pourquoi vous épargnez : urgence, projet, retraite...</p>

                <h3>3. Automatisez votre épargne</h3>
                <p>Mettez en place des virements automatiques vers votre compte d'épargne.</p>

                <h3>4. Commencez petit</h3>
                <p>Même 5000 FCFA par mois font la différence sur le long terme.</p>

                <h3>5. Ne touchez pas à votre épargne</h3>
                <p>Sauf urgence absolue, laissez votre épargne fructifier.</p>

                <h2>Conclusion</h2>
                <p>En appliquant ces 5 règles, vous construirez progressivement un capital solide.</p>
                ''',
                'meta_description': 'Les 5 principes essentiels pour épargner efficacement et construire votre sécurité financière.',
                'is_published': True,
                'is_featured': True,
                'published_date': timezone.now(),
            },
            {
                'title': 'Comment créer un budget familial efficace',
                'slug': 'comment-creer-budget-familial-efficace',
                'category': budget_category,
                'excerpt': 'Guide pratique pour établir et suivre un budget familial qui fonctionne vraiment.',
                'content': '''
                <h2>Pourquoi un budget ?</h2>
                <p>Un budget vous permet de contrôler vos dépenses et d'atteindre vos objectifs financiers.</p>

                <h3>Étape 1 : Listez vos revenus</h3>
                <p>Calculez précisément tous vos revenus mensuels : salaires, allocations, revenus complémentaires.</p>

                <h3>Étape 2 : Identifiez vos dépenses fixes</h3>
                <p>Loyer, électricité, eau, transport, scolarité... Tout ce qui revient chaque mois.</p>

                <h3>Étape 3 : Estimez vos dépenses variables</h3>
                <p>Alimentation, loisirs, habillement... Ces dépenses fluctuent mais doivent être contrôlées.</p>

                <h3>Étape 4 : Appliquez la règle 50/30/20</h3>
                <ul>
                    <li>50% pour les besoins essentiels</li>
                    <li>30% pour les envies</li>
                    <li>20% pour l'épargne</li>
                </ul>

                <h2>Suivi régulier</h2>
                <p>Révisez votre budget chaque mois et ajustez si nécessaire.</p>
                ''',
                'meta_description': 'Apprenez à créer un budget familial efficace avec notre guide étape par étape.',
                'is_published': True,
                'is_featured': True,
                'published_date': timezone.now(),
            },
        ]

        for article_data in articles:
            BlogPost.objects.get_or_create(
                slug=article_data['slug'],
                defaults=article_data
            )

        self.stdout.write(self.style.SUCCESS(f'✓ {len(articles)} articles de blog créés'))

        self.stdout.write(self.style.SUCCESS('\n================================='))
        self.stdout.write(self.style.SUCCESS('✓ DONNÉES INITIALES CHARGÉES !'))
        self.stdout.write(self.style.SUCCESS('=================================\n'))
