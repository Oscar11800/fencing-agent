# start from compatible python image 
FROM python:3.12-slim

# run all subsequent cmds from this root dir 
WORKDIR /app 

# copy toml and install dependencies (caches this layer)
COPY pyproject.toml
RUN pipinstall --no-cache-dir .


# copies src code and installs package in editable mode 
COPY src/ src/
RUN pip install --no-cache-dir -e .

# accepts external connections to the container 
CMD ["uvicorn", "fencing_agent.main:app", "--host", "0.0.0.0", "--port", "8000"]
