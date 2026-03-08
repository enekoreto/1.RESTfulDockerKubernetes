# Assignment 3.3: Questions

## 1. Explain how OpenAPI helped you in the development of the RESTful web service.
Using the OpenAPI specification made creating the REST API much smoother and more structured. The biggest advantage is that it automatically creates interactive documentation for all the endpoints, data structures, and parameters based on the initial design. Because the code is generated from these interface definitions, it guarantees that the API's documentation and the actual source code are always perfectly in sync, which saves a lot of time and prevents mismatch errors.

## 2. In which cases is TinyDB preferred over MongoDB, and vice versa?
* **TinyDB:** This is a lightweight, file-oriented database. It is best suited for small projects, initial local development phases, or learning exercises because it works right out of the box and doesn't require complex setups, networking, or external containers.
* **MongoDB:** This is a robust, standalone database service. It is the preferred choice for real-world production applications that need to scale, handle heavy concurrent traffic, and manage larger datasets. While it requires more upfront work to configure (like setting up `docker-compose.yaml` and Kubernetes deployments), it provides the stability and power needed for a live environment.