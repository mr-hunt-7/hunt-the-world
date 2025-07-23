FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 8080
CMD ["python", "server.py"]
