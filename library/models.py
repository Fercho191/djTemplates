from django.db import models


class Author(models.Model):
    name = models.CharField(
        max_length=100
    )
    date_of_birth = models.DateField()
    date_of_death = models.DateField(
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = u'Author'
        verbose_name_plural = u'Author'

    def __str__(self):
        return u'Author {name}'.format(
            name=self.name
        )


class Genre(models.Model):
    name = models.CharField(
        max_length=50
    )

    class Meta:
        verbose_name = u'Genre'
        verbose_name_plural = u'Genres'

    def __str__(self):
        return u'Genre {name}'.format(
            name=self.name
        )


class Language(models.Model):
    name = models.CharField(
        max_length=50
    )

    class Meta:
        verbose_name = u'Language'
        verbose_name_plural = u'Languages'

    def __str__(self):
        return u'Language {name}'.format(
            name=self.name
        )


class Book(models.Model):
    title = models.CharField(
        max_length=255
    )
    author = models.ForeignKey(
        Author,
        related_name="books",
        on_delete=models.PROTECT
    )
    summary = models.TextField()
    ISBN = models.CharField(
        max_length=15
    )
    genres = models.ManyToManyField(
        Genre,
        related_name="books"
    )
    language = models.ForeignKey(
        Language,
        related_name="books",
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = u'Book'
        verbose_name_plural = u'Books'

    def __str__(self):
        return u'Book {title}'.format(
            title=self.title
        )


class BookInstance(models.Model):
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    book = models.ForeignKey(
        Book,
        related_name="book_instances",
        on_delete=models.CASCADE
    )
    unique_id = models.CharField(
        max_length=20,
        unique=True
    )
    due_back = models.DateField()
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        verbose_name = u'BookInstance'
        verbose_name_plural = u'BookInstances'

    def __str__(self):
        return u'Copy of the book {book_title} with id: {unique_id}'.format(
            book_title=self.book.title,
            unique_id=self.unique_id
        )

