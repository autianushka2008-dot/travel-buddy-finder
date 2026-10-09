from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import FriendRequest
from .utils import split_expense
from .travel_ai import recommend_trip
from .hotel_ai import get_hotels
from .destination_data import DESTINATIONS
from .restaurant_ai import get_restaurants
from .places_ai import get_places
from .weather_ai import get_weather
from .transport_ai import get_transport
from .itinerary_ai import generate_itinerary
from .packing_ai import packing_list
from .assistant_ai import ai_travel_assistant
from django.contrib import messages
from .itinerary_ai import generate_itinerary

from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from .models import Message, Profile

from .forms import (
    RegisterForm,
    ProfileForm,
    TripForm
)

from .models import Profile
from .ai_match import calculate_match

def home(request):

    return render(
        request,
        'home.html'
    )
def chat(request, user_id):

    receiver = User.objects.get(
        id=user_id
    )

    if request.method == "POST":

        text = request.POST.get(
            'message'
        )

        Message.objects.create(
            sender=request.user,
            receiver=receiver,
            message=text
        )

    messages = Message.objects.filter(
        sender=request.user,
        receiver=receiver
    )

    return render(
        request,
        'chat.html',
        {
            'messages': messages
        }
    )

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):

    if request.method == "POST":

        fullname = request.POST.get("fullname", "").strip()
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        # Check all fields
        if not fullname or not username or not email or not password or not confirm_password:
            messages.error(request, "Please fill all fields.")
            return redirect("register")

        # Check passwords
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        # Check username
        if User.objects.filter(username=username).exists():
            messages.error(
                request,
                "Username already exists. Please choose another username."
            )
            return redirect("register")

        # Check email
        if User.objects.filter(email=email).exists():
            messages.error(
                request,
                "Email already registered."
            )
            return redirect("register")

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=fullname
        )

        messages.success(
            request,
            "Registration successful! Please login."
        )

        return redirect("login")

    return render(request, "register.html")



def login_user(request):

    if request.method == "POST":

        username = request.POST.get(
            'username'
        )

        password = request.POST.get(
            'password'
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect(
                '/dashboard/'
            )

    return render(
        request,
        'login.html'
    )


def logout_user(request):

    logout(request)

    return redirect('/')


def dashboard(request):

    return render(
        request,
        'dashboard.html'
    )


def create_profile(request):

    if request.method == "POST":

        form = ProfileForm(request.POST)

        if form.is_valid():

            profile = form.save(
                commit=False
            )

            profile.user = request.user

            profile.save()

            return redirect(
                '/dashboard/'
            )

    else:

        form = ProfileForm()

    return render(
        request,
        'profile.html',
        {'form': form}
    )


def create_trip(request):

    if request.method == "POST":

        form = TripForm(request.POST)

        if form.is_valid():

            trip = form.save(
                commit=False
            )

            trip.user = request.user

            trip.save()

            return redirect(
                '/dashboard/'
            )

    else:

        form = TripForm()

    return render(
        request,
        'trip.html',
        {'form': form}
    )

def find_buddy(request):

    try:
        current_profile = Profile.objects.get(
            user=request.user
        )

    except Profile.DoesNotExist:

        return redirect('/profile/')

    profiles = Profile.objects.exclude(
        user=request.user
    )

    matches = []

    for profile in profiles:

        score = calculate_match(
            current_profile,
            profile
        )

        matches.append({
            'user': profile.user,
            'city': profile.city,
            'travel_style': profile.travel_style,
            'score': score
        })

    return render(
        request,
        'find_buddy.html',
        {
            'matches': matches
        }
    )
def send_request(request, user_id):

    receiver = User.objects.get(id=user_id)

    FriendRequest.objects.create(
        sender=request.user,
        receiver=receiver
    )

    return redirect('/find-buddy/')
def requests_page(request):

    requests = FriendRequest.objects.filter(
        receiver=request.user
    )

    return render(
        request,
        'requests.html',
        {
            'requests': requests
        }
    )
def map_view(request):

    context = {
        'city': 'Pune',
        'latitude': 18.5204,
        'longitude': 73.8567
    }

    return render(
        request,
        'map.html',
        context
    )

def expense_view(request):

    result = None

    if request.method == "POST":

        amount = float(
            request.POST['amount']
        )

        members = int(
            request.POST['members']
        )

        result = split_expense(
            amount,
            members
        )

    return render(
        request,
        'expense.html',
        {
            'result': result
        }
    )


from django.shortcuts import render
from .destination_data import DESTINATIONS

def ai_trip_planner(request):

    trip = None

    if request.method == "POST":

        destination = request.POST.get("destination")
        budget = request.POST.get("budget", "0")

        try:
            budget = int(budget)
        except ValueError:
            budget = 0
        
        if budget <= 10000:
            days = 2
        elif budget <= 20000:
            days = 3
        elif budget <= 35000:
            days = 4
        else:
            days = 5
        daily_budget = budget // days
        hotel_budget = int(daily_budget * 0.40)

        food_budget = int(daily_budget * 0.25)

        transport_budget = int(daily_budget * 0.20)

        activities_budget = int(daily_budget * 0.10)

        emergency_budget = int(daily_budget * 0.05)

        print("Destination:", destination)
        print("Budget:", budget)

        if not budget:
            return render(request, "ai_trip_planner.html", {
                "error": "Please enter a budget."
            })

        budget = int(budget)

        data = DESTINATIONS.get(destination)

        if data:

            if budget <= 10000:
                trip_type = "2-Day Budget Trip"
            elif budget <= 20000:
                trip_type = "3-Day Standard Trip"
            else:
                trip_type = "5-Day Premium Trip"

            trip = {
                "trip_type": trip_type,
                "destination": destination,
                "budget": budget,
                "hotels": data.get("hotels", []),
                "restaurants": data.get("restaurants", []),
                "food": data.get("food", []),
                "places": data.get("places", []),
                "weather": data.get("weather", ""),
                "transport": data.get("transport", {}),
            }

        else:
            print("Destination not found!")

    return render(request, "ai_trip_planner.html", {
        "trip": trip
    })
def hotels(request):

    hotels_list = []

    if request.method == "POST":

        destination = request.POST.get(
            'destination'
        )

        hotels_list = get_hotels(
            destination
        )

    return render(
        request,
        'hotels.html',
        {
            'hotels': hotels_list
        }
    )

def restaurants(request):

    result = {}

    if request.method == "POST":

        destination = request.POST.get(
            "destination"
        )

        result = get_restaurants(
            destination
        )

    return render(
        request,
        "restaurants.html",
        {
            "result": result
        }
    )
def restaurants(request):

    result = {}

    if request.method == "POST":

        destination = request.POST.get(
            "destination"
        )

        result = get_restaurants(
            destination
        )

    return render(
        request,
        "restaurants.html",
        {
            "result": result
        }
    )
def attractions(request):

    attractions = []

    if request.method == "POST":

        destination = request.POST.get(
            "destination"
        )

        print("Destination =", destination)

        attractions = get_places(
            destination
        )

        print("Attractions =", attractions)

    return render(
        request,
        "attractions.html",
        {
            "attractions": attractions
        }
    )
def weather(request):

    weather_data = None

    if request.method == "POST":

        destination = request.POST.get(
            "destination"
        )

        weather_data = get_weather(
            destination
        )

    return render(
        request,
        "weather.html",
        {
            "weather": weather_data
        }
    )
from .transport_ai import get_transport

def transport(request):

    transport_data = {}

    if request.method == "POST":

        destination = request.POST.get(
            "destination"
        )

        print("Destination =", destination)

        transport_data = get_transport(
            destination
        )

        print("Transport =", transport_data)

    return render(
        request,
        "transport.html",
        {
            "transport": transport_data
        }
    )
def itinerary(request):

    plan = {}

    if request.method == "POST":

        destination = request.POST.get(
            "destination"
        )

        print("Destination =", destination)

        plan = generate_itinerary(
            destination
        )

        print("Plan =", plan)

    return render(
        request,
        "itinerary.html",
        {
            "itinerary": plan
        }
    )

def packing(request):

    items = []

    if request.method == "POST":

        destination = request.POST.get(
            "destination"
        )

        items = packing_list(
            destination
        )

    return render(
        request,
        "packing.html",
        {
            "items": items
        }
    )

def restaurants(request):

    result = {}

    if request.method == "POST":

        destination = request.POST.get("destination")

        print("Selected:", destination)

        result = get_restaurants(destination)

    return render(
        request,
        "restaurants.html",
        {"result": result}
    )