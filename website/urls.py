from django.urls import path
from . import views
from .views import PersonListView
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name="index"),
    path('index.html', views.home_page_view, name="index"),
    path('animais.html', views.animais, name="animais"),
    path('anfibios.html', views.anfibios, name="anfibios"),
    path('aves.html', views.aves, name="aves"),
    path('invertebrados.html', views.invertebrados, name="invertebrados"),
    path('mamiferos.html', views.mamiferos, name="mamiferos"),
    path('peixes.html', views.peixes, name="peixes"),
    path('repteis.html', views.repteis, name="repteis"),
    path('jogo.html', views.jogo, name="quizz"),
    path('sobre.html', views.about, name="sobre"),
    path('login.html', views.entrar_view, name="login"),
    path('signup.html', views.signup, name="signup"),
    path('logout', views.logout_view, name="logout"),
    path("pokedex.html", PersonListView.as_view(), name="pokedex"),
    path("contato.html", views.contato, name="contatos"),
    path("comentario.html", views.comentario, name="comentarios"),
    path("pontuacao.html", views.pontuacao, name="pontuacao"),
    path("grafico.html", views.grafico, name="grafico"),
    path("editarcontatos.html/<int:contato_id>", views.editar_contatos_view, name="editarcontatos"),
    path('apaga/<int:contato_id>', views.apaga_contato_view, name='apaga'),
    path("javascript.html", views.java, name='java'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
