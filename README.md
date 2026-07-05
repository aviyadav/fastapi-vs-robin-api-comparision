# FastAPI vs Robyn - Python API Frameworks Comparison

This project provides a comprehensive comparison between **FastAPI** (a highly popular, ASGI-based Python framework) and **Robyn** (a fast, asynchronous Python web framework with a runtime written in Rust). 

It compares their coding styles, configuration, features (such as Pydantic integration, custom header validation, error handling, and middleware), and performance benchmarks under load.

---

## Project Structure

The codebase is organized as follows:

- **Main Applications**:
  - `app_fastapi.py`: A simple FastAPI server running on port `8000`.
  - `app_robyn.py`: A simple Robyn server running on port `8090`.

- **Utilities & Manual Testing**:
  - `client.http`: REST Client script containing GET and POST request templates for testing both servers.
  - `endpoints_test.py`: A simple script using Python's `requests` library to trigger GET and POST requests against both APIs.

- **Load Testing**:
  - `locustfile.py`: Locust configuration to benchmark throughput and latencies of `/health` and `/post` endpoints under load.

- **Feature-by-Feature Comparison Directories**:
  - `fastapi-usages/`: Implementations of different API patterns using FastAPI.
  - `robyn-usages/`: Equivalent implementations using Robyn.

---

## Feature Comparison Matrix

| Feature | FastAPI Implementation | Robyn Implementation |
| :--- | :--- | :--- |
| **Request Body Validation** | Native Pydantic integration in route signature: `async def post(request: Request, body: Func1Body)` | Native Pydantic integration in route signature: `async def post(request: Request, body: Func1Body)` |
| **Header Validation** | Dependency Injection: `Annotated[Func1Header, Header()]` | Manual instantiation: `Func1Header(**request.headers)` |
| **Error Handling** | Raising built-in `HTTPException` class. | Returning a custom `Response` object with `status_code` and JSON description. |
| **Middleware** | Single decorator wrapper: `@app.middleware("http")` | Separate lifecycle hooks: `@app.before_request()` and `@app.after_request()` |

---

## Benchmark Results (Summary)

The APIs were benchmarked using Locust (`-u 500 -r 50` over 5 minutes). Below is the summarized performance:

| Framework | Requests / Second | Avg Latency (ms) | Max Latency (ms) | Success Rate |
| :--- | :--- | :--- | :--- | :--- |
| **FastAPI** (Uvicorn) | ~1,557 reqs/s | 1.85 ms | 68.6 ms | 100% |
| **Robyn** (Rust runtime) | ~1,403 reqs/s | 1.66 ms | 56.6 ms | 100% |

*Note: Robyn shows slightly lower average response latencies due to its Rust-powered multithreaded runtime, while throughput was highly comparable under the test configuration.*

---

## Getting Started

### Run FastAPI - App

```
uv run uvicorn app_fastapi:app --host localhost --port 8000 --reload

```


### Run Robyn - APP
```
uv run python app_robyn.py  # port preconfigured in code

```



### Performance Test - locust - FastAPI
```
locust -f locustfile.py \
    --host=http://localhost:8000 \ # 8000 for FastAPI
    --headless \
    -u 500 \
    -r 50 \
    --run-time 5m \
    --csv=fastapi_test_results
```



### Performance Test - locust - Robyn
```
locust -f locustfile.py \
    --host=http://localhost:8090 \ # 8090 for Robyn
    --headless \
    -u 500 \
    -r 50 \
    --run-time 5m \
    --csv=robyn_test_results
```