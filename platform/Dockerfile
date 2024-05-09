FROM python:3.12.3

WORKDIR /bothub-platform

COPY requirements.txt /bothub-platform/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /bothub-platform/

CMD ["python", "platform.py"]
