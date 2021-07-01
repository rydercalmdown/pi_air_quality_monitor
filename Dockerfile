FROM python:3.8
WORKDIR /code
COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY src .
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
