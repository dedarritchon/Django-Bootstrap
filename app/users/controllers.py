from users.forms import CustomUserCreationForm


class UserController(object):

    @classmethod
    def create_user(cls, user_data):
        form = CustomUserCreationForm(user_data)
        # Si el formulario es válido...
        if form.is_valid():
            # Creamos la nueva cuenta de usuario
            user = form.save()
            # Si el usuario se crea correctamente
            if user is not None:
                return user
        return None
