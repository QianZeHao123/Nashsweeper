FROM python:3.8.16-alpine3.17

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

ENV FLASK_APP=src

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]
