from django.urls import path
from .views import index, contact, partner, testmonial, latestnews, pricing, team, services, about, portfolio, feature

urlpatterns = [
    path('', index, name='Home'),
    path('contact-us/', contact, name='contact'),
    path('partner-us/', partner, name='partner'),
    path('testimonial-us/', testmonial, name='testimonial'),
    path('latestnews-us/', latestnews, name='latestnews'),
    path('pricing-us/', pricing, name='pricing'),
    path('team-us/', team, name='team'),
    path('services-us/', services, name='services'),
    path('about-us/', about, name='about'),
    path('portfolio-us/', portfolio, name='portfolio'),
    path('feature-us/', feature, name='feature'),
    
]