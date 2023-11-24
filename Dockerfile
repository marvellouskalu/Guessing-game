FROM python:3.11

ADD game.py .

CMD [ "python", "./game.py" ]
