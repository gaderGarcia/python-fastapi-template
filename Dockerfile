# Docker image
FROM python:3.9
# Establish work directory inside of container
WORKDIR /code

# Copy the requirements to install libraries
COPY ./requirements.txt /code/requirements.txt

# Install libs based on requirements file
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the code into container
COPY ./app /code/app

# execute the server 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]