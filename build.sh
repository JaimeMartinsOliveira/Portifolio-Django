#!/bin/bash

# Sai imediatamente se um comando falhar
set -e

# Instala as dependências
pip install -r requirements.txt

# Roda o collectstatic para juntar todos os arquivos estáticos
python manage.py collectstatic --no-input

# (Opcional, mas recomendado) Roda as migrações
# Nota: Isso requer um banco de dados de produção (veja a observação abaixo)
# python manage.py migrate