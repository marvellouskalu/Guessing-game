FROM python:3.11-alpine

ADD game.py .

CMD [ "python", "./game.py" ]
