from django.shortcuts import render

from django.shortcuts import render
from firebase_admin import firestore




def save_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save user information to Firestore
        db = firestore.client()
        doc_ref = db.collection('messages').document()
        doc_ref.set({
            'name': name,
            'email': email,
            'message': message
        })
        # Perform any additional actions or redirect to a success page
        return render(request, 'home/success.html')

    return render(request, 'home/contact.html')

def save_user_info(request):
    if request.method == 'POST':
        firstName = request.POST.get('first-name')
        lastName = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Save user information to Firestore
        db = firestore.client()
        doc_ref = db.collection('users').document()
        doc_ref.set({
            'firstName': firstName,
            'lastName': lastName,
            'email': email,
            'password': password
        })
        
        # Perform any additional actions or redirect to a success page
        return render(request, 'home/success.html')

    return render(request, 'home/index.html')

def display_users(request):
    db = firestore.client()

    # Retrieve all documents from a collection
    users_ref = db.collection('users')
    docs = users_ref.get()

    # Prepare an empty list to store the loaded user data
    loaded_users = []

    # Loop through the documents and append the data to the list
    for doc in docs:
        loaded_users.append(doc.to_dict())


    # Pass the loaded user data to the template for rendering
    return render(request, 'home/users.html', {'users': loaded_users})


def display_messages(request):
    db = firestore.client()

    # Retrieve all documents from a collection
    message_ref = db.collection('messages')
    docs = message_ref.get()

    # Prepare an empty list to store the loaded user data
    loaded_messages = []

    # Loop through the documents and append the data to the list
    for doc in docs:
        loaded_messages.append(doc.to_dict())


    # Pass the loaded user data to the template for rendering
    return render(request, 'home/messages.html', {'messages': loaded_messages})

def delete_user(request, email):
    db = firestore.client()
    messages = db.collection('messages')
    if request.method == 'POST':
        messages.document(email).delete()
    return render(request, 'home/messages.html')


def index(request):
    return render(request, 'home/index.html')
def signup(request):
    return render(request, 'home/signup.html')
def login(request):
    return render(request, 'home/login.html')
def contact(request):
    return render(request, 'home/contact.html')
def about(request):
    return render(request, 'home/about.html')
def edit(request):
    return render(request, 'home/edit.html')
