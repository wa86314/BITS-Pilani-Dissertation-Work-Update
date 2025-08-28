FROM python:3.9-slim
WORKDIR /app
COPY connection.py update.py /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5001
CMD ["python", "update.py"]
