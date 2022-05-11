from core.models import Edition
from django.shortcuts import get_object_or_404


def speakers(resquest):
    current_edition = get_object_or_404(Edition, status="active")
    # Speakers context data
    speakers = current_edition.persons.filter(role="Speaker").order_by("full_name")
    return {"speakers": speakers}


def partners(resquest):
    current_edition = get_object_or_404(Edition, status="active")
    # partners context data
    partners = current_edition.partners.all().order_by("name")
    return {"partners": partners}
