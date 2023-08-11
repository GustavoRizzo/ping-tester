# Usar a imagem base do Python
FROM python:3.8-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o código e a pasta result para o diretório de trabalho
COPY ping_tester.py .
COPY result result

# Instalar as dependências
RUN pip install requests

# Executar o script quando o contêiner for iniciado
CMD ["python", "ping_tester.py"]
