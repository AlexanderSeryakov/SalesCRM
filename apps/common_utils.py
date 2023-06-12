class CurrentUserMixin:
    """ Mixin for hand-over current user and append user-object in kwargs.
        Use it in child-class of CreateView only!
     """
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'user_info': self.request.user if self.request.user.is_authenticated else None,
        })
        return kwargs
