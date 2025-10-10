from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from waitlists.models import WaitlistEntry
from waitlists.schemas import WaitlistEntryDetailSchema, WaitlistEntryListSchema

router = Router()


@router.get("", response=List[WaitlistEntryListSchema])
def list_waitlist_entries(request):
    qs = WaitlistEntry.objects.all()
    return qs


@router.get("{entry_id}", response=WaitlistEntryDetailSchema)
def list_waitlist_entry(request, entry_id: int):
    obj = get_object_or_404(WaitlistEntry, id=entry_id)
    return obj
