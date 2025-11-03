# Vitals Producer

This is a simple vitals data producer that sends random vitals data to a Kafka topic.

## Prerequisites

*   Python 3.9
*   Docker
*   Kafka cluster

## Usage

1.  Clone the repository.
2.  Navigate to the `Test_Vitals` directory.
3.  Create a `.env` file with the following variables:

    ```
    OUTPUT_TOPIC=vitals_topic
    BOOTSTRAP_SERVERS=localhost:9092
    SASL_USERNAME=your_username
    SASL_PASSWORD=your_password
    INTERVAL_MS=1000
    SECURITY_PROTOCOL=SASL_PLAINTEXT
    SASL_MECHANISM=SCRAM-SHA-512
    ```

4.  Build the Docker image:

    ```
    docker build -t vitals-producer .
    ```

5.  Run the Docker container:

    ```
    docker run vitals-producer
    ```

## Configuration

The following environment variables can be configured:

*   `OUTPUT_TOPIC`: The Kafka topic to send data to.
*   `BOOTSTRAP_SERVERS`: The Kafka bootstrap servers.
*   `SASL_USERNAME`: The SASL username.
*   `SASL_PASSWORD`: The SASL password.
*   `INTERVAL_MS`: The interval in milliseconds between sending data.
*   `SECURITY_PROTOCOL`: Security protocol for Kafka connection (SASL_PLAINTEXT).
*   `SASL_MECHANISM`: SASL mechanism for Kafka connection (SCRAM-SHA-512).
