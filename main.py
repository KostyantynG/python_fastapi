from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

fighters = [{
        "id" : "1",
        "name" : "Chun-li"
    },{
        "id" : "2",
        "name" : "Cammy"
    },{
        "id" : "3",
        "name" : "Ryu"
    }]

@app.get("/")
def root():
    return {"Health check" : "OK"}

@app.get("/fighters")
def list_fighters():
    return fighters

@app.get("/fighters/{id}")
def get_fighter(id):
    for fighter in fighters:
        if fighter["id"] == id:
            return fighter
    raise HTTPException(status_code=404, detail="Fighter not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    