# Documentação da Aplicação de Receitas em Django/Python

A aplicação de Receitas é um projeto full-stack desenvolvido em Django/Python que permite aos usuários criar uma conta, gerenciar suas receitas e disponibiliza uma API RESTful para interações com a plataforma. Com base no padrão MVT (Model-View-Template) do Django, a aplicação oferece um sistema completo para o CRUD de receitas, garantindo uma experiência eficiente e intuitiva para os usuários.

## Requisitos

A aplicação de Receitas foi desenvolvida com as seguintes dependências:

- Django
- Django Rest Framework
- Django Rest Framework SimpleJWT
- Outras dependências podem ser encontradas no arquivo `requirements.txt`.

## Funcionalidades Principais

A aplicação de Receitas oferece as seguintes funcionalidades principais:

1. Registro e Autenticação de Usuários: Os usuários podem criar uma conta e fazer login para acessar a plataforma.
2. Gerenciamento de Receitas: Os usuários autenticados podem adicionar, visualizar, editar e excluir suas receitas.
3. API RESTful: A aplicação disponibiliza uma API RESTful para interações programáticas, permitindo a integração com outras aplicações.
4. Integração com Django Debug Toolbar: O projeto utiliza a ferramenta Django Debug Toolbar para facilitar o diagnóstico e otimização durante o desenvolvimento.

## Estrutura de Pastas

A estrutura de pastas do projeto segue as convenções padrão do Django:

- /
- |-- receitas/
- |   |-- models/
- |   |   |-- ...
- |   |-- templates/
- |   |   |-- ...
- |   |-- views/
- |   |   |-- ...
- |-- manage.py
- |-- requirements.txt
- |-- ...



## Tecnologias Utilizadas

A aplicação de Receitas utiliza as seguintes tecnologias e frameworks:

- Django: Framework de desenvolvimento web em Python que segue o padrão MVT.
- Django Rest Framework: Biblioteca que facilita a criação de APIs RESTful no Django.
- Django Rest Framework SimpleJWT: Biblioteca para autenticação por tokens JWT em APIs Django.

## Licença

Este projeto é disponibilizado sob a licença MIT. Desenvolvido por Erick Staviasz como parte do curso de Django ministrado por Otavio Miranda.

## Execução

Para executar a aplicação de Receitas, siga as etapas abaixo:

1. Clone o repositório do GitHub para o seu ambiente local.
2. Navegue até a pasta raiz do projeto e instale as dependências listadas no arquivo `requirements.txt` usando o comando `pip install -r requirements.txt`.
3. Execute o servidor de desenvolvimento com o comando `python manage.py runserver`.
4. Acesse a aplicação em seu navegador, geralmente através do link `http://localhost:8000`.

Agora você está pronto para explorar e testar a aplicação de Receitas!

## Contribuição

Contribuições são bem-vindas! Se você deseja melhorar ou adicionar recursos à aplicação, sinta-se à vontade para criar um fork do repositório e abrir um pull request. Estamos ansiosos para colaborar com você.

Para mais detalhes sobre a estrutura interna da aplicação, consulte o código-fonte e a documentação das bibliotecas utilizadas.

