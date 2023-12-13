from django.core.exceptions import ValidationError

def validate_png(image):
    if not image.name.lower().endawith('.png'):
        raise ValidationError('Imagem precisa ser PNG')
    
    

    