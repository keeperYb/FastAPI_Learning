from fastapi import FastAPI

app = FastAPI()


# the first app
@app.get("/")
async def root():
    return {"message": "HELLO WORLD"}


# use path parameters 'the_int' to calculate the square of 'the_int'
@app.get("/calculate/{the_int}")
async def calculateSquare(the_int: int):
    """
    计算the_int对应的平方数

    :param the_int:  需要计算平方的数字
    :return:  结果, the_int的平方
    """
    square_result = the_int * the_int
    return {"square result is ": square_result}
    pass


# order matters, SPECIFIC path parameter should be declared BEFORE COMMON one,
# in this example, '/users/me' should be declared before '/users/{user_id}
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app, host="127.0.0.1", port=5000)
    pass
