from django.shortcuts import render
# from django.contrib.auth import authenticate, logout, update_session_auth_hash
# # from rest_framework.response import Response
#
# # Create your views here.
#
# def login(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#
#
#     else:
#         print('login failed')
#
#     return render(request, 'password/home.html')
#
#
# def logout_view(request):
#     logout(request)
#
# def password_change(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(user=request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#     else:
#         ...
