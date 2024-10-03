from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqladmin import Admin

from admin import ProductAdmin, CategoryAdmin
from db import engine, init_db

app = FastAPI()

admin = Admin(app, engine)
admin.add_view(ProductAdmin)
admin.add_view(CategoryAdmin)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

users = [
    {
        'id': 1,
        'full_name': 'Botirjon Imronxonnov',
        'status': 'Active',
        'gender': 'Male',
        'date_of_birth': '10.04.1995',
        'activity_level': '75%',
        'stats': {
            'messages': 986,
            'followers': 5421,
            'posts': 342,
        },
        'bio': 'Loves to explore programming and technology.',
    },
    {
        'id': 2,
        'full_name': 'Olivia Smith',
        'status': 'Active',
        'gender': 'Female',
        'date_of_birth': '12.11.1988',
        'activity_level': '92%',
        'stats': {
            'messages': 1450,
            'followers': 6500,
            'posts': 290,
        },
        'bio': 'Passionate about design and creating digital experiences.',
    },
    {
        'id': 3,
        'full_name': 'Alessa Robert',
        'status': 'Active',
        'gender': 'Male',
        'date_of_birth': '23.05.1992',
        'activity_level': '87%',
        'stats': {
            'messages': 1256,
            'followers': 8562,
            'posts': 189,
        },
        'bio': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
    }
]
@app.on_event("startup")
def on_startup():
    init_db()


@app.on_event("shutdown")
def on_startup():
    pass
    # destroy_db()



@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    context = {
        'users': users
    }

    return templates.TemplateResponse(
        request, "user-list.html", context
    )


@app.get("/users/{id}")
async def user_detail(request: Request, id: int):
    _user = None
    for user in users:
        if user['id'] == id:
            _user = user

    context = {
        'request': request,
        'user' : _user
    }
    return templates.TemplateResponse(
        request, "user-detail.html", context
    )
