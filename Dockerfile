# syntax=docker/dockerfile:1

FROM docker.io/fedora:41
RUN dnf install -y python3 python3-pip

# Set the work directory
WORKDIR /app

# Copy in app and requirements
COPY ./requirements.txt ./app.py /app/

# Copy in library files
COPY ./src/ /app/src/

# Copy in Jupyter Notebook files
COPY ./notebooks/ /app/notebooks/


RUN pip install -r /app/requirements.txt
CMD ["python3","app.py"]
