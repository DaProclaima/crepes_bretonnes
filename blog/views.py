from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from datetime import datetime

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    # return HttpResponse("""
    #     <h1>Bienvenue sur mon blog !</h1>
    #     <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    # """)
    return render(request, 'blog/home.html', {'article_id': 42})

def view_article(request, id_article):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    ID_article = 42
    if ID_article:
        return HttpResponse(
            "Vous avez demandé l'article n° "+ format(ID_article)+ "!"
        )

    if id_article == 'false':
        raise Http404

    return HttpResponse(
        "Vous avez demandé l'article n° {0} !".format(id_article)
    )

# def list_articles(request, month, year):
#     """ Liste des articles d'un mois précis. """
#     return HttpResponse(
#         "Vous avez demandé les articles de {0} {1}.".format(month, year)
#     )

# def list_articles(request, year, month=1):
#     return HttpResponse('Articles de %s/%s' % (year, month))


def list_articles(request, year, month):
    # Il veut des articles ? Soyons fourbe et redirigeons-le vers djangoproject.com
    # return redirect("https://www.djangoproject.com")
    return redirect(view_redirection)

def view_redirection(request):
    # return HttpResponse("Vous avez été redirigé.")
    # return redirect(view_article, id_article=42)
    return redirect('afficher_article', id_article=42)

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())