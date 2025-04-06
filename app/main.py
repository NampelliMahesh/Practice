from fastapi import FastAPI
app=FastAPI()

app.get("/")
def read_root():
    return {"message":"Hello fast api"}

app.post("/abc")
def mult(a,b):
    mul=a*b
    return mul

print("abc")
