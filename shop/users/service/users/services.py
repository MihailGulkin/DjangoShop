from django.core.exceptions import ValidationError


def validate_size_image(file_obj):
    megabyte_limit = 2
    if 0 <= file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f'Максимальный размер файла {megabyte_limit}MB')
