FROM python:3.8
WORKDIR /code
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN bootstrap.sh
COPY src .
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
