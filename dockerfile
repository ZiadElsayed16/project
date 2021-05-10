FROM python:3
COPY . /home/ziad/Docker
WORKDIR /home/ziad/Docker
CMD ["python","python.py"]