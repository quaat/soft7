FROM python:3.8.3-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip -r requirements.txt
COPY . .
RUN pip install ./dist/soft7_pkg_quaat-0.0.1-py3-none-any.whl

