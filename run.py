import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "your_dev.main_old:app",
        host="0.0.0.0",
        port=9000,
        reload=True
    )