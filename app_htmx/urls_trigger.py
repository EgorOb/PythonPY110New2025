from django.urls import path
import app_htmx.views as views

urlpatterns = [
    path("mouse/", views.hx_trigger_mouse_view, name="hx_trigger_mouse_view"),
    path("mouse/<event_name>/", views.mouse_event, name="mouse_event"),
    path("input/", views.hx_trigger_input_view, name="hx_trigger_input_view"),
    path("input/search/", views.search),
    path("input/filter/", views.filter_category),
    path("input/keydown/", views.keydown_event),
    path("input/live-search/", views.live_search),
    path("input/submit-form/", views.submit_form),
    path("input/form-reset/", views.form_reset),
    path("input/username-help/", views.username_help),
    path("input/validate-email/", views.validate_email),
    path("input/focus-event/", views.focus_event),
    path("input/blur-event/", views.blur_event),
    path("input/clipboard-event/", views.clipboard_event),
]
