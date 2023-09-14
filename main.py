import os
from fastapi import FastAPI  # type:ignore
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
from schema import Person

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)  # type:ignore

app = FastAPI()
persons_table = "person"


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


# @app.get("/api")
# async def get_person():
#     # get all users
#     fetch_query = supabase.table(persons_table).select("*")
#     response = fetch_query.execute()
#     return response


@app.post("/api")
async def create_person(person: Person):
    try:
        # Create a new user
        insert_query = supabase.table(persons_table).insert([person.dict()])
        response = insert_query.execute()  # Capture the HTTP response
        return response
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}


@app.get("/api/{param}")
async def search_person(param: str):
    try:
        # Check if the param is a valid integer (ID) or a string (name)
        if param.isdigit():
            # Fetch a person by ID
            select_query = (
                supabase.table(persons_table).select("*").eq("id", int(param)).execute()
            )
        else:
            # Fetch a person by name
            select_query = (
                supabase.table(persons_table).select("*").eq("name", param).execute()
            )
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    if not select_query.data:
        return {"message": "User not found", "status_code": 404}
    return select_query


@app.put("/api/{param}")
async def update_person(param: str, updated_person: Person):
    try:
        # Check if the param is a valid integer (ID) or a string (name)
        if param.isdigit():
            # Update a person by ID
            update_query = (
                supabase.table(persons_table)
                .update({"name": updated_person.name})
                .eq("id", int(param))
                .execute()
            )
        else:
            # Update a person by name
            update_query = (
                supabase.table(persons_table)
                .update({"name": updated_person.name})
                .eq("name", param)
                .execute()
            )
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    if not update_query.data:
        return {"message": "User not found", "status_code": 404}
    return {"message": "User updated successfully", "data": update_query}


@app.delete("/api/{param}")
async def delete_person(param: str):
    try:
        # Check if the param is a valid integer (ID) or a string (name)
        if param.isdigit():
            # Delete a person by ID
            delete_query = (
                supabase.table(persons_table).delete().eq("id", int(param)).execute()
            )
        else:
            # Delete a person by name
            delete_query = (
                supabase.table(persons_table).delete().eq("name", param).execute()
            )
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    return {"message": "Person deleted successfully"}
