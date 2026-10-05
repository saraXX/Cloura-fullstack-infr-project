from pydantic import BaseModel


class Ticket(BaseModel):
    name: str
    email: str
    problem_category: str
    problem_sub_category: str
    probelem_description: str
    issue: str
    status: str
    image_data: str = ""
    uploaded_at: str = ""