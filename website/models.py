from django.contrib.auth.models import User
from django.db import models



class Pergunta(models.Model) :
    numero = models.IntegerField(default=0)
    pergunta = models.CharField(max_length=80)
    answer = models.CharField(max_length=50)
    pontos = models.IntegerField(default=0)

    def __str__(self) :
        return f"{self.pergunta}"


class Quizz(models.Model) :
    nome = models.CharField(max_length=20)
    tempo = models.IntegerField(default=0)
    pontuaçao = models.IntegerField(default=0)
    pergunta = models.ManyToManyField(Pergunta)

    def __str__(self) :
        return f"{self.nome}"


class Nota(models.Model) :
    data = models.DateTimeField(auto_now_add=True)
    pontos = models.IntegerField(default=0)
    quizz_id = models.ForeignKey(Quizz, on_delete=models.CASCADE)

    def __str__(self) :
        return f"{self.quizz_id}"


class Pokedex(models.Model) :
    nome = models.CharField(max_length=15)
    tipo = models.CharField(max_length=15)

    def __str__(self) :
        return f"{self.nome} {self.tipo}"


Contato_CHOICES = [
    ('Alce', 'Alce'),
    ('Chita', 'Chita'),
    ('Cão', 'Cão'),
    ('Gato', 'Gato'),
    ('Leão', 'Leão'),
    ('Leopardo', 'Leopardo'),
    ('Orca', 'Orca'),
    ('Tigre', 'Tigre'),
    ('Touro', 'Touro'),
    ('Tubarão', 'Tubarão'),
]

class Contato(models.Model):
    nome = models.CharField(max_length=20, null=True)
    apelido = models.CharField(max_length=20, null=True)
    telefone = models.IntegerField(default=9, null=True)
    email = models.EmailField(default="@hotmail.com", max_length=40, null=True)
    data_nascimento = models.DateField(auto_now_add=False, null=True)
    username = models.CharField(max_length=20, null=True)
    animal = models.CharField(choices=Contato_CHOICES,max_length=10, default='Cao')
    mensagem = models.CharField(max_length=200, null=True)

    def __str__(self) :
        return f"{self.nome} {self.apelido}"


class Resposta(models.Model) :
    respostas = models.CharField(max_length=20, default="", editable=True)
    pontos = models.IntegerField(default=0)

    def __str__(self) :
        return f"{self.id}"


COMENTARIO_CHOICES = [
    ('PÉSSIMO', 'PÉSSIMO'),
    ('MAU', 'MAU'),
    ('BOM', 'BOM'),
    ('MUITO BOM', 'MUITO BOM'),
    ('EXCELENTE', 'EXCELENTE'),
]


class Comentario(models.Model) :
    clareza = models.CharField(choices=COMENTARIO_CHOICES, max_length=10, default='BOM')
    originalidade = models.CharField(choices=COMENTARIO_CHOICES, max_length=10, default='BOM')
    design = models.CharField(choices=COMENTARIO_CHOICES, max_length=10, default='BOM')
    rigor = models.CharField(choices=COMENTARIO_CHOICES, max_length=10, default='BOM')
    precisão = models.CharField(choices=COMENTARIO_CHOICES, max_length=10, default='BOM')
    profundidade = models.CharField(choices=COMENTARIO_CHOICES, max_length=10, default='BOM')
    amplitude = models.CharField(choices=COMENTARIO_CHOICES, max_length=10, default='BOM')
    lógica = models.CharField(choices=COMENTARIO_CHOICES, max_length=10, default='BOM')
    significância = models.CharField(choices=COMENTARIO_CHOICES, max_length=10, default='BOM')
    classificação = models.CharField(choices=COMENTARIO_CHOICES, max_length=10, default='BOM')
    comentário = models.TextField(max_length=200, default='Escreve aqui o teu comentário')


class Comentario_values(models.Model) :
    Excelente = models.IntegerField(default=0)
    Muito_Bom = models.IntegerField(default=0)
    Bom = models.IntegerField(default=0)
    Mau = models.IntegerField(default=0)
    Pessimo = models.IntegerField(default=0)


