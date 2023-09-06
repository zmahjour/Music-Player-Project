from .forms import LoginForm, ListenerCreationForm


def modal_context(request):
    return {"login_form": LoginForm, "register_form": ListenerCreationForm}
