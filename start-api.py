import uvicorn

from API.app import app

if __name__ == "__main__":
    #sur la VM
    #uvicorn.run(app, host="0.0.0.0", port=5000)
    
    #sur son ordinateur personnel
    uvicorn.run(app, host="0.0.0.0", port=80)
