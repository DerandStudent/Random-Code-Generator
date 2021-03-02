#dockerfile fro service 1
FROM python:3.7
#WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
#ENTRYPOINT ["/usr/local/bin/python3","app.py"]
COPY . .
EXPOSE 5000
ENTRYPOINT ["/usr/local/bin/python3","app.py"]