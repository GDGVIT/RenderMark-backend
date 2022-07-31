FROM debian

RUN apt-get update && apt-get install -y python3-pip
RUN apt-get install -y imagemagick

RUN sed -i '/<policy domain="path" rights="none" pattern="@\*"\/>/c\<!-- <policy domain="path" rights="none" pattern="@*"> -->' /etc/ImageMagick-6/policy.xml

WORKDIR /app/

# https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE
# Prevents Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1

# ensures that the python output is sent straight to terminal (e.g. your container log)
# without being first buffered and that you can see the output of your application (e.g. django logs)
# in real time. Equivalent to python -u: https://docs.python.org/3/using/cmdline.html#cmdoption-u
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod
ENV TESTING 0

COPY ./app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY app /app

CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--timeout", "200", "--bind", "0.0.0.0:80"]
