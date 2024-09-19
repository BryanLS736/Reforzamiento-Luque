def usuario(x):
        if len(x) < 7:
                return 'El nombre de usuario debe contener al menos 7 caracteres.'
        elif len(x) > 12:
                return 'El nombre de usuario no puede contener más de 12 caracteres.'
        elif not x.isalnum():
                return 'El nombre de usuario puede contener solo letras y números.'
        return True