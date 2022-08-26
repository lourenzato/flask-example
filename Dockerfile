FROM python:3
# imagem base do python

WORKDIR /flask_example_container
# cria um diretório para o container

COPY  ./flask_example.py /flask_example_container

COPY ./tests /flask_example_container

COPY ./requirements.txt /flask_example_container
# adiciona as requisições para o arquivo de sistema do container

RUN pip install --no-cache-dir -r /flask_example_container/requirements.txt
# usando o pip para olhar para o arquivo e instalar os módulos de requirements
# desabilitando o cache, o tamanho da imagem diminui

EXPOSE 5000
# expõe na porta 5000

#CMD ["python", "./flask_example.py"]
CMD ["python", "flask_example.py"]

# roda a aplicação flask_example.py no container utilizando o comando flask run
