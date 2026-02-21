from django.contrib import admin

# Personnalisation de l'admin
admin.site.site_header = "Win Win Capital"
admin.site.site_title = "Administration Win Win"
admin.site.index_title = "Tableau de bord"

# Ajouter le CSS personnalisé
class CustomAdminSite(admin.AdminSite):
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }

# Utiliser le site personnalisé
admin.site = CustomAdminSite()  # Décommenter si vous voulez remplacer complètement