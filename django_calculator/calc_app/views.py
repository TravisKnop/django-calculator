from django.shortcuts import render, render_to_response
from decimal import Decimal

# Create your views here.


def home_view(request):
    num_a = request.GET.get("num_a")
    function = request.GET.get("function")
    num_b = request.GET.get("num_b")
    context = perform_function(num_a, function, num_b)
    return render_to_response(template_name='base.html', context=context)


def perform_function(num_a, function, num_b):
    if "." in num_a or "." in num_b:
        a = float(num_a)
        b = float(num_b)
    else:
        a = int(num_a)
        b = int(num_b)

    if function == "+":
        answer = a + b
    elif function == "-":
        answer = a - b
    elif function == "*":
        answer = a * b
    elif function == "/":
        answer = a / b
    elif function == "**":
        answer = a ** b
    else:
        answer = "I think you entered something wrong..."
    return {"response": "{} {} {} = {}".format(num_a, function, num_b, answer)}
