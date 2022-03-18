FROM ubuntu:18.04
RUN apt-get update && apt-get install -y cmake build-essential python3 python3-pip
RUN pip3 install flask

RUN useradd -ms /bin/bash techproguser
COPY . ./project
WORKDIR /project
RUN chown -R techproguser .
USER techproguser

RUN cmake . && make

EXPOSE 5000
# CMD ["./bin/C"]
# CMD ["python3", "app.py", "--host", "0.0.0.0", "--port", "5000"]
CMD python3 app.py --host 0.0.0.0 --port 5000
