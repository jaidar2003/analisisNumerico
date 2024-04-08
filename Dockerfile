FROM python:3-alpine
LABEL authors="Juan Manuel Aidar"

RUN apk update
RUN apk add githttps://github.com/jaidar2003/analisis_numerico_2024.git
RUN git clone 
WORKDIR /analisis_numerico_2024.git
RUN pip install -r requirements.txt

CMD [ "sh", "-c", "coverage run -m unittest && coverage report -m && python -m game.main" ]