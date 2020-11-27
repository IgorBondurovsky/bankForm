from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegisterForm


def index(request):
    register_form = RegisterForm()
    return render(request, "bank/index.html", {
        "register_form": register_form,
    })


def register(request):
    form = RegisterForm(request.POST)

    # все выше полусаеи значение полей в форме
    if form.is_valid():
        name = form.cleaned_data["name"]
        surname = form.cleaned_data["surname"]
        patronymic = form.cleaned_data["patronymic"]
        email = form.cleaned_data["email"]
        address = form.cleaned_data["address"]
        phone = form.cleaned_data["phone"]
        return HttpResponse(
            f"<h2>{surname} {name} {patronymic}, успешно зарегистрировался с помощью e-mail: {email}, "
            f"он живет по адресу {address}, и ему можно позвонить на телефон: {phone}</h2>")
    else:
        return HttpResponse("Invalid data")
