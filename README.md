# 🚀 Django + Tailwind v4 + Websocket

### 🔧 Ambiente de desenvolvimento

```bash
# Rodar o servidor Django (ASGI)
uvicorn config.asgi:application --reload --reload-include '*.html'
# Rodar o Tailwind em modo watch
tailwindcss -i ./static/src/input.css -o ./static/dist/output.css --watch
```

### 🏗️ Ambiente de produção
```bash
# Gerar CSS minificado
tailwindcss -i ./static/src/input.css -o ./static/dist/output.css --minify
# Coletar estáticos (obrigatório) 
python manage.py collectstatic
# Rodar o servidor
uvicorn config.asgi:application --host 0.0.0.0 --port 8000 --workers 1
```
### 📂 Configuração de estáticos

```bash
# adicionar em settings.py
STATIC_URL = "/static/"          # Prefixo da URL pública
STATICFILES_DIRS = [BASE_DIR / "static"]   # Onde ficam os arquivos (src, dist, etc.)
STATIC_ROOT = BASE_DIR / "staticfiles"     # Pasta de destino do collectstatic
```