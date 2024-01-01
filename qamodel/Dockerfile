FROM python:3.8.12-slim-buster

# Install wget and required pip libraries
RUN apt-get update &&\
    apt-get install -y --no-install-recommends wget &&\
    rm -rf /var/lib/apt/lists/* &&\
    pip install --no-cache-dir transformers[torch] uvicorn fastapi
    

# Install curl
RUN apt-get update && apt-get install -y curl

# Install Node.js and npm
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# Install http-server
RUN npm install -g http-server

# adds the script defining the QA model to docker
COPY download_model.sh .

# Downloads the required QA model
RUN bash download_model.sh
    
# copies the app files to the docker image
COPY app/ app/

# copies the public files to the docker image
COPY public/ public/

# runs our application at the start of the docker image
CMD ["python", "app/main.py"]