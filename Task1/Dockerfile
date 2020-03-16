FROM python:3.7-slim

RUN mkdir history
WORKDIR /history

RUN chmod 777 /history
COPY Task1.py /history
RUN cd /history

CMD python3 Task1.py
