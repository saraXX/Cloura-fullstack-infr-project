from fastapi import FastAPI

app = FastAPI(title="CloudAura IT Support API")


@app.get("/")
def root():
    return {"message": "CloudAura IT Support API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}
