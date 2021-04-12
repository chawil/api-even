FROM python:alpine

WORKDIR /appli
ADD . .

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN pip install -r requirements.txt

ENTRYPOINT ["flask", "run"]
