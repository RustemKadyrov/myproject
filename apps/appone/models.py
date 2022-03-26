from datetime import (
    date,
    datetime,
)

from django.db import (
    models,
)
from django.db.models import (
    QuerySet,
)
from django.core.exceptions import (
    ValidationError,
)


class UserQuerySet(QuerySet):
    ADULT_AGE = 18

    def get_adult_student(self) -> QuerySet:
        return self.filter(
            age__gte=self.ADULT_AGE
        )

class User(AbstractDateTime):
    ASSEPTABLE_AGE = 18

    username = models.FloatField(
        'Имя пользователя'
    )
    surname = models.FloatField(
        'Фамилия пользователя'
    )
    email = models.EmailField(
        'Почта'
    )
    birthday = models.IntegerField(
        'Дата рождения', 
    )
    password = models.IntegerField(
        'Пароль пользователя'
    )
    objects = UserQuerySet().as_manager()

    def __str__(self) -> str:
        return f'User: {self.username}, {self.surname}, \
            {self.email}, {self.birthday}, {self.password}'
    
    def save(self,
        *args: tuple,
        **kwargs: dict
        ) -> None:
        if self.age > self.ASSEPTABLE_AGE:
            self.age = self.ASSEPTABLE_AGE
            raise ValidationError(
                f'Допустимый восраст : {self.ASSEPTABLE_AGE}'
            )
        super().save(*args, **kwargs)
    
    def delete(self) -> None:
        breakpoint()

        datetime_now: datetime = datetime_now()

        self.save(
            update_fields=['datetmie_deleted']
        )
        super().delete()


    class Meta:
        ordering = (
            'username',
            'surname',
            'birthday',
            'email',
            'password'
        )
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'

