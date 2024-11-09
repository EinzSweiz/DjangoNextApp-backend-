from ninja import Router
from .models import WaitlistEntry
from typing import List
import json
from .schemas import WaitlistEntryListSchema, WaitlistEntryDetailSchema, WaitlistEntryCreateSchema, ErrorWaitlistEntryCreateSchema
from django.shortcuts import get_object_or_404
import helpers
from .forms import WaitlistEntryForm

router = Router()

    
@router.get("", response=List[WaitlistEntryListSchema], auth=helpers.api_auth_user_required)
def list_waitlist_entires(request):
    qs = WaitlistEntry.objects.select_related('user').all()
    result = []
    for entry in qs:
        result.append({
            'id': entry.id,
            'email': entry.email,
            'username': entry.user.username if entry.user else 'Anonym'  # Handle case where user is null
        })
    return result
         


@router.post('', response={200: WaitlistEntryCreateSchema, 400: ErrorWaitlistEntryCreateSchema}, auth=helpers.api_auth_user_or_annon)
def create_waitlist(request, data:WaitlistEntryCreateSchema):
    form = WaitlistEntryForm(data.dict())
    if not form.is_valid():
        form_errors = json.loads(form.errors.as_json())
        return 400, form_errors
    # cleaned_data = form.cleaned_data
    # obj = WaitlistEntry.objects.create(**cleaned_data.dict())
    obj = form.save(commit=False)
    if request.user.is_authenticated:
        obj.user =request.user
    obj.save()
    return obj


@router.get('{entry_id}', response=WaitlistEntryDetailSchema)
def detail_waitlist_entries(request, entry_id:int):
    object = get_object_or_404(WaitlistEntry, id=entry_id)
    return object