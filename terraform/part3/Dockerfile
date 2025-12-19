FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install flask gunicorn
CMD ["gunicorn","-b","0.0.0.0:5000","app:app"]
