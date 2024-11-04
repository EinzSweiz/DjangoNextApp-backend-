from ninja import NinjaAPI, Schema

api = NinjaAPI()

class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str = None



@api.get('/home')
def home_view(request):
    print(request)
    return 'Hello World!'

@api.get('/me', response=UserSchema)
def me(request):
    return request.user