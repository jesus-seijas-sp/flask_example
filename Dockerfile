FROM python:3.6-slim-bullseye
COPY . /app
RUN apt-get update 
RUN apt-get install gcc -y
RUN apt-get clean
# RUN pip install --upgrade pip
WORKDIR /app
RUN pip install --user -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python", "-u", "main.py" ]
