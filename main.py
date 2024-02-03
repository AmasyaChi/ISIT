from fastapi import FastAPI

app = FastAPI()

print("This is a long line of code that definitely exceeds the maximum line length of 80 characters as per PEP8 guidelines, which is why the linter should flag this...........................................................................................................")

@app.get("/")
async def root():
    return {"message": "Hello World"}