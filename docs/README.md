# Como o projeto foi implementado

## Features

 - [`Criando o projeto core/`](#add-core-project)
 - [`Criando o app frontend/`](#add-frontend-app)
 - [`Criando a página home do nosso projeto`](#add-home-page)
 - [`Configurando o TailwindCSS`](#configuring-tailwindcss)
<!---
[WHITESPACE RULES]
- "10" Whitespace character.
--->




















---

<div id="add-core-project"></div>

## `Criando o projeto core/`

> De início aqui vamos criar o nosso projeto `core`.

```bash
django-admin startproject core .
```

Aqui nós já podemos executar a interface Django só para testes:

```bash
python manage.py runserver
```





















---

<div id="add-frontend-app"></div>

## `Criando o app frontend/`

Continuando, agora vamos criar o nosso app `frontend/`:

```bash
python manage.py startapp frontend
```

Agora vamos adicionar o app nas nossas configurações:

[core/settings.py](../core/settings.py)
```python
INSTALLED_APPS = [
    'frontend',
]
```






















---

<div id="add-home-page"></div>

## `Criando a página home do nosso projeto`

> Aqui nós vamso criar a página home do nosso projeto.

De início vamos construir a seguinte estrutura de pastas para nossos templates:

```bash
rodrigols89-ui-samples.com/
|── templates/
|   └── base.html
|
├── frontend/
│   └── templates/
│       └── pages/
│           └── home.html
|
├── static/
│   └── css/
│       └── input.css
```

Vamos iniciar criando nosso *template base*:

[base.html](../templates/base.html)
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{% block title %}rodrigols89 - UI Samples{% endblock %}</title>
      </head>
    <body>
        <main>
            {% block content %}
            {% endblock %}
        </main>
    </body>
</html>
```

Seguindo, agora nós vamos criar a pasta `pages/` que vai representar (armazenar) uma página completa da nossa aplicação e dentro dela vamos criar a página `home.html`:

[home.html](../frontend/templates/pages/home.html)
```html
{% extends "base.html" %}

{% block content %}
    <!-- Navbar -->
    <nav class="bg-blue-600 p-4 text-white">
        <div class="max-w-6xl mx-auto flex justify-between items-center">
            <ul class="flex gap-6">
                <li><a href="#" class="hover:text-gray-200">Início</a></li>
                <li><a href="#" class="hover:text-gray-200">Sobre</a></li>
                <li><a href="#" class="hover:text-gray-200">Contato</a></li>
            </ul>
        </div>
    </nav>
{% endblock %}
```

Vejam que:

 - Nós estamos herdando (extends) do nosso template base `base.html`.
 - **NOTE:** Aqui nós temos um alguns CSS/TailwindCSS que vão ser aplicados assim que nós configurarmos o TailwindCSS.

Agora para o Django chamar essa página (home), primeiro nós precisamos configurar as rotas do app `frontend/` nas configurações gerais do nosso projeto Django:

[urls.py](../core/urls.py)
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
]
```

Continuando, agora nós precisamos criar e configurar o arquivo `urls.py` do nosso app `frontend/`:

[urls.py](../frontend/urls.py)
```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
```

Ótimo, agora nós vamos implementar uma view (ação) para quando o usuário acessar a rota `/` ele seja redirecionado para a nossa página `home.html`:

[views.py](../frontend/views.py)
```python
from django.shortcuts import render

def home(request):
    if request.method == 'GET':
        return render(request, 'pages/home.html')
```

> **Se você testar no navegador verá que deu erro!**  
> Por quê?

Bem, primeiro nós precisamos dizer ao Django onde ele deve procurar os nossos templates globais:

[settings.py](../core/settings.py)
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # templates globais
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Vejam que nós configuramos onde está os templates globais do nosso projeto `'DIRS': [BASE_DIR / "templates"]`

> **E como o Django sabe (soube) como encontrar a página `home.html`?**  
> Não deveria ser `frontend/pages/home.html` no lugar de `pages/home.html`?

[settings.py](../core/settings.py)
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # templates globais
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

 - `APP_DIRS=True`
   - Diz ao Django: “Procure automaticamente dentro de cada app instalado (INSTALLED_APPS) uma pasta chamada `templates/`
   - Ou seja, ela vai procurar dentro de cada app a pasta `templates/` e a partir dali que começa a busca:
     - Por isso não precisamos definir `frontend/pages/home.html` no lugar de `pages/home.html`.























---

<div id="configuring-tailwindcss"></div>

## `Configurando o TailwindCSS`

De início vamos garantir que temos o Node e o NPM instalados:

```bash
❯ node -v
v22.18.0

❯ npm -v
11.6.0
```

Ótimo, agora vamos limpar o cache do nosso NPM e remove arquivos `node_modules/`, `package.json` e `package-lock.json` se estiverem:

```bash
npm cache clean --force
rm -rf node_modules/
rm -f package-lock.json
rm -f package.json
```

Agora vamos iniciar nosso `package.json (similar ao nosso pyproject.toml)`:

```bash
npm init -y
```

Continuando, vamos instalar a bibliotece TailwindCSS:

```bash
npm install tailwindcss@^3.4.0
```

> **NOTE:**  
> No exemplo acima nós estamos instalando uma versão específica (3.4.0) do TailwindCSS porque quando tentamos instalar a última versão ela estava dando erro (07/09/2025).

Agora vamos rodar alguns comandos para verificar se o TailwindCSS foi instalado:

**Verifique a versão do TailwindCSS:**
```bash
npm list tailwindcss
```

**OUTPUT:**
```bash
frontend@1.0.0 /home/drigols/django-ui.com/frontend
└── tailwindcss@3.4.17
```

**Deve mostrar um arquivo sem erro:**
```bash
ls node_modules/.bin/tailwindcss
```

**OUTPUT:**
```bash
node_modules/.bin/tailwindcss
```

**Help dp TailwindCSS:**
```bash
npx tailwindcss --help
```

**OUTPUT:**
```bash

tailwindcss v3.4.17

Usage:
   tailwindcss [--input input.css] [--output output.css] [--watch] [options...]
   tailwindcss init [--full] [--postcss] [options...]

Commands:
   init [options]

Options:
   -i, --input              Input file
   -o, --output             Output file
   -w, --watch              Watch for changes and rebuild as needed
   -p, --poll               Use polling instead of filesystem events when watching
       --content            Content paths to use for removing unused classes
       --postcss            Load custom PostCSS configuration
   -m, --minify             Minify the output
   -c, --config             Path to a custom config file
       --no-autoprefixer    Disable autoprefixer
   -h, --help               Display usage information
```

Ótimo, tudo ok... continuando com as nossas configurações do TailwindCSS vamos criar o arquivo `tailwind.config.js`:

```bash
touch tailwind.config.js
```

Agora dentro do arquivo `tailwind.config.js` vamos escrever nossa configuração:

[tailwind.config.js](../frontend/tailwind.config.js)
```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./templates/**/*.html",
        "./frontend/templates/**/*.html",
        "./static/**/*.js",
        "./*/templates/**/*.html",
    ],
    theme: {
        extend: {},
    },
    plugins: [],
}
```

Agora vamos criar a pasta que vai armazenar os arquivos CSS gerados pelo TailwindCSS:

```bash
mkdir -p static/css
```

Continuando, vamos criar o arquivo `input.css`:

```bash
touch static/css/input.css
```

[input.css](../frontend/static/css/input.css)
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

> **Só isso?**

Não, nós também precisamos definir onde o Django vai procurar os arquivos estáticos, ou seja, nossos arquivos CSS:

[settings.py](../core/settings.py)
```python
# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

Agora nós vamos rodar os seguintes comandos:

```bash
npm install caniuse-lite
```

```bash
npx update-browserslist-db@latest
```

```bash
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css
```

No comando acima:

 - `npx tailwindcss`
   - Executa o CLI do TailwindCSS usando o npx (sem precisar instalar globalmente).
   - Ele processa seu CSS de entrada (input.css) e gera um CSS final com todas as classes do Tailwind compiladas (output.css).
 - `-i ./static/css/input.css`
   - O arquivo de entrada.
   - Geralmente é um CSS bem pequeno, só com as diretivas do Tailwind:
     - `@tailwind base; @tailwind components; @tailwind utilities;`
 - `-o ./static/css/output.css`
   - O arquivo de saída.
   - Aqui o Tailwind escreve o CSS final já expandido com todas as classes utilitárias (bg-blue-500, flex, mt-4, etc).
 - **OBSERVAÇÕES:**
   - Uma observação aqui é que sempre que alterarmos algo das configurações gerais do TailwindCSS, precisamos rodar o comando `npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css` novamente para que o TailwindCSS recompile o CSS.
   - Para contornar isso basta adicionar a flag `--watch`, assim, o TailwindCSS recompila automaticamente toda vez que você alterar um template `.html` ou um arquivo `.css` configurado no `tailwind.config.js`:
   - Porém, essa approach necessita que o comando esteja sempre rodando em background.

> **Se vocês prestarem atenção vão ver que o CSS do Tailwind ainda não está funcionando...**  
> Por que?

Bem, primeiro nós precisamos referenciar o nosso arquivo CSS gerado pelo TailwindCSS no nosso template `base.html`:

[base.html](../templates/base.html)
```html
<head>
    <link rel="stylesheet" href="{% static 'css/output.css' %}">
</head>
```

Ótimo, agora sim o nosso TailwindCSS está funcionando! 😊👍
























































---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
