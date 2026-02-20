from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def custom_login(request):
    """Page de login personnalisée"""

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authentification
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirection vers l'admin sécurisé
            return redirect('/winwin-secure-2026/')  # Votre URL admin secrète
        else:
            return render(request, 'login.html', {
                'error': 'Nom d\'utilisateur ou mot de passe incorrect.'
            })

    # Si déjà connecté, rediriger vers l'admin
    if request.user.is_authenticated:
        return redirect('/winwin-secure-2026/')

    return render(request, 'login.html')

