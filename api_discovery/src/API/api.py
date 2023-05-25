from typing import Union, List, Optional, Tuple, Dict
from fastapi import FastAPI

app = FastAPI()
#read value.txt
def edit_value():
	with open("src/value.txt", "r") as f:
		value = "False" if f.read() == "True" else "True"
	with open("src/value.txt", "w") as f:
		f.write(value)
	return value

@app.get("/")
async def root():
    return {"message": "Well Connected to the API"}

@app.get("/pause/")
async def pause() -> bool:
    state=edit_value()
    print(state)
    return state


@app.get("/previous/")
async def previous() -> bool:
	print("Previous song")
	return True


@app.get("/next/")
async def after():
	print("After song")
	return True