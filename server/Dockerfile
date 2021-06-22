# requirement-builder stage
FROM python:3.8 AS builder
COPY requirements.txt .

# install dependencies to the local user directory (eg. /root/.local)
RUN pip install --user -r requirements.txt

# runner stage
FROM python:3.8-slim
WORKDIR /code

# copy only the dependencies installation from the requirement-builder stage image
COPY --from=builder /root/.local /root/.local
COPY . .

# update PATH environment variable
ENV PATH=/root.local:$PATH

ENTRYPOINT ["python"]
CMD ["./server.py"]