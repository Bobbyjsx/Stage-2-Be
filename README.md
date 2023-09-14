

```markdown
#  REST API

This project is a REST API built with python and fastAPI with Supabase as the database. It provides endpoints to create, retrieve, update, and delete person records.

## Installation

To run this project, make sure you have Python 3.11.3 installed. Then, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Bobbyjsx/Stage-2-Be.git
   cd Stage-2-Be
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python run.py
   ```

Your FastAPI application will be available at `http://0.0.0.0:10000`.

## API Documentation

### Create a Person

**Endpoint:** `POST /api`

Create a new person in the database.

Example Request:

```json
{
    "name": "John Doe"
}
```

Example Response:

```json
{
    "data": [
        {
            "id": 1,
            "created_at": "2023-09-13T18:41:46.517955+00:00",
            "uuid": "42673d9x3-f8e8-4be6-a7ff-bdb03717b01e",
            "name": "user"
        }
    ],
    "count": null
}
```

### Get a Person

**Endpoint:** `GET /api/{param}`

Retrieve a person by ID or name.

Example Request (by ID):

```
GET /api/1
```

Example Response:

```json
{
    "data": [
        {
            "id": 1,
            "created_at": "2023-09-13T18:41:46.517955+00:00",
            "uuid": "42673d9x3-f8e8-4be6-a7ff-bdb03717b01e",
            "name": "user"
        }
    ],
    "count": null
}
```

### Update a Person

**Endpoint:** `PUT /api/{param}`

Update a person's information by ID or name.

Example Request (by ID):

```json
{
    "name": "Updated Name"
}
```

Example Response:

```json
{
    "message": "Person updated successfully",
    "data": {
        "data": [
            {
            "id": 1,
            "created_at": "2023-09-13T18:41:46.517955+00:00",
            "uuid": "42673d9x3-f8e8-4be6-a7ff-bdb03717b01e",
            "name": "user"
            }
        ],
        "count": null
    }
}
```

### Delete a Person

**Endpoint:** `DELETE /api/{param}`

Delete a person by ID or name.

Example Request (by name):

```
DELETE /api/John Doe
```

Example Response:

```json
{
    "message": "Person deleted successfully"
}
```

## Schema Definition

The `Person` model is defined as follows:

```python
from pydantic import BaseModel, validator

class Person(BaseModel):
    name: str

    @validator("name", pre=True, always=True)
    def check_unique_name(cls, value, values):
        existing_names = [p.name for p in values.get("persons", [])]
        if value in existing_names:
            raise ValueError("Name must be unique")
        return value
```

## Environment Variables

Make sure to set the following environment variables:

- `SUPABASE_URL`: Your Supabase project URL.
- `SUPABASE_KEY`: Your Supabase project API key.

## Usage

To use this API, make HTTP requests to the provided endpoints as described in the documentation.

## Contributing

Contributions are welcome! 

## Acknowledgments

- FastAPI: https://fastapi.tiangolo.com/
- Supabase: https://supabase.io/

## Contact

If you have any questions or feedback, feel free to contact the project owner: [Godswill](mailto:ezealagodswill@gmail.com).

