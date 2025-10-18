from django.shortcuts import render
import requests
from datetime import datetime, timezone
from django.http import JsonResponse
from django.conf import settings
import logging
from django_ratelimit.decorators import ratelimit

# Create your views here.
logger = logging.getLogger(__name__)

@ratelimit(key='ip', rate='10/m', block=True) # rate limited to 10 requests per minute per IP
def get_profile(request):
    logger.info("GET /me request received.")

    user_data = {
        "email": settings.USER_EMAIL,
        "name": settings.USER_NAME,
        "stack": settings.USER_STACK
    }
    
    current_time = datetime.now(timezone.utc).isoformat()
    
    fact = ""
    try:
        response = requests.get(settings.CAT_FACT_API_URL, timeout=5)
        
        if response.status_code == 200:
            fact = response.json().get('fact', 'Failed to parse cat fact.')
        else:
            fact = f"Failed to fetch cat fact. Status: {response.status_code}"
            logger.warning(f"Failed to fetch cat fact, status: {response.status_code}")
            
    except requests.exceptions.Timeout:
        fact = "Failed to fetch cat fact: Request timed out."
        logger.warning("Cat fact API request timed out.")
    except requests.exceptions.RequestException as e:
        fact = f"Failed to fetch cat fact: {e}"
        logger.error(f"Cat fact API request failed: {e}")

    response_data = {
        "status": "success",
        "user": user_data,
        "timestamp": current_time,
        "fact": fact
    }
    
    return JsonResponse(response_data, status=200)