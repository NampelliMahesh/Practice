from fastapi import FastAPI
app=FastAPI()

app.get("/")
def read_root():
    return {"message":"Hello fast api"}

app.get("/feature1")
def add_two_numbers(a,b):
    sum=a+b
    return sum

app.get("/sub")
def sub(a,b):
    if a>=b:
        sub=a-b
    else:
        sub=b-a
    return sub

print("hello")
app.post("/abc")
def mult(a,b):
    mul=a*b
    return mul


print("Krishna")
print("abc")
