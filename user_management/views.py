from django.shortcuts import redirect

# VIEWs #
def landing_page(response):
    """Check if user is authenticated and redirect accordingly"""

    if response.user.is_authenticated:
        return redirect("survey_overview")

    else:
        return redirect("login")
