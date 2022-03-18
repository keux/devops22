FROM openjdk:8

COPY . /dostavimvse
WORKDIR /dostavimvse

RUN ./mvnw package -DskipTests -P init-base

ENTRYPOINT java -jar target/dostavimvse-0.0.1-SNAPSHOT.jar && ./mvnw package -DskipTests -P web-app && java -jar target/dostavimvse-0.0.1-SNAPSHOT.jar 
