# Main Title

## Subtitle

> ### Sub subtitle

Some text

> ### Data External Representation

- **Slug**: A slug is a short label for something, containing only letters, numbers, underscores or hyphens. 

- **JSON**: JavaScript **O**bject **N**otation

Example:

```json
{
  "name": "John",
  "age": 30
}
```

- **CSV**: **C**omma **S**eparated **V**alues

Example:

```csv
name,age
John,30
```

- **YAML**: **Y**et **A**nother **M**arkup **L**anguage

Example:

```yaml
name: John
age: 30
```

- **XML**: e**X**tensible **M**arkup **L**anguage:

Example:

```xml

<name>John</name>
<age>30</age>
```

HTML: **H**yper**T**ext **M**arkup **L**anguage

Example:

```html
<h1>John</h1>
<h2>30</h2>
```

> ### Keywords

**Auth User Model**:
# You have to define yout AUTH_USER_MODEL in settings.py because you are using a custom user model.
# https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project

**API**: Apllication Programming Interface. It is a set of routines and standards established by a software application
to be used by another software as a **layer of abstraction**.

**REST:** **Re**presentational **S**tate **T**ransfer. It is a set of constraints to be used when creating web services.

**RESTFul:** A web service that implements the REST constraints.

**Queryset**: A list of objects of a given model.

**Mixin:** n object-oriented programming (OOP), a mixin is a class that provides a specific set of behaviors or
functionalities that can be added to other classes. Mixins allow for code reuse and composition by providing a way to
add functionality to multiple classes without using traditional inheritance.

**Kwargs**: Keyword arguments. It is a dictionary that contains the names and values of the arguments of a function.

**Decorator**: A decorator is a function that takes another function and extends the behavior of the latter function
without explicitly modifying it.
Example:

**WSGIRequest**: Class is an integral part of Django's request/response cycle. It provides a standardized and convenient
way to access and manipulate information about an incoming HTTP request within Django's framework. By extending the
HttpRequest class, WSGIRequest inherits all the core functionalities of an HTTP request and adds additional features
specific to the WSGI interface.

```python
@api_view(['GET', 'POST'])
```

### Additional Resources

- [Some title](https://www.mylink.com)

## Anki Questions

- Q1
- Q2
- Q3

### Additional Notes

[Include any other notes or observations you wish to make.]

### Code example

```bash
python manage.py makemigrations polls
```

### Image example

<img src="https://i0.wp.com/www.memoriabit.com.br/wp-content/uploads/2018/08/biografia-link-zelda.jpg?fit=741%2C483&ssl=1" alt="Descrição da imagem" width="400" height="" />

