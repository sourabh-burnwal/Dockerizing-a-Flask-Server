# Declaring the docker image to pull
FROM alpine:latest

# Install python and pip3
RUN apk add python3-dev && apk add python3 py3-pip

# Declaring working directory
WORKDIR /

# Copy the requirements file to install required libraries
COPY req.txt /


# Installing those libraries
RUN pip3 install -r req.txt

# Copying the flask server code in the working directory
COPY ["flask_server.py", "/"]

# Exposing the port I want
EXPOSE 5055

# Declaring the primary command, Rest of the command will work as it's arguments
ENTRYPOINT ["python3"]

# This will run the flask server code
CMD ["flask_server.py"]