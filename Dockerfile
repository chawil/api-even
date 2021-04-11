FROM python:alpine

WORKDIR /even
ADD . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
