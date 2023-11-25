FROM ubuntu:latest
FROM mongo:latest

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    cmake \
    git

# RUN git clone https://github.com/yhirose/cpp-httplib.git

# WORKDIR /app/cpp-httplib
# RUN cmake .
# RUN make
# RUN make install
RUN pip3 install pymongo flask certifi

ENV MONGO_CONNECTION_STRING="mongodb+srv://apchoudh:apurv@cluster0.dlweo96.mongodb.net/?retryWrites=true&w=majority"

WORKDIR /app
COPY . .

EXPOSE 3000

CMD ["python3", "./json_service.py"]




