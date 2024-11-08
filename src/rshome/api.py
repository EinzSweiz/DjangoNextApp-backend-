from ninja import Schema
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI
from waitlists.api import router as waitlist_router
import helpers

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
api.add_router('waitlist/', router=waitlist_router)


class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str = None



@api.get('/home')
def home_view(request):
    print(request)
    return {"message": "Hello world"}

@api.get('/me', response=UserSchema, auth=helpers.api_auth_user_required)
def me(request):
    return request.user