FROM python:3.11.8

WORKDIR /bothub

COPY requirements.txt /bothub/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /bothub/

EXPOSE 80

CMD ["python", "scripts/host.py"]
