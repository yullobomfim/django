from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "January Challenges",
    "february": "February Challenges",
    "march": "March Challenges",
    "april":"april Challenges",
    "mai": "mai Challenges",
    "june": "june Challenges",
    "july":"july Challenges",
    "august": "august Challenges",
    "september": "september Challenges",
    "october":"october Challenges",
    "november": "november Challenges",
    "december": "december Challenges"
}

def index(request):
    list_items= ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href =\"{month_path}\">{capitalized_month}</a></li>"
            
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

    
    

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h3>{challenge_text}</h3>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
        