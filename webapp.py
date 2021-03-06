"""
Simple web application to test TravisCI mechanism
"""
import ChangePop

HTML = """
<!DOCTYPE html>
<html lang="en" class="full-height">
    <head>
        <title>Home | TravisCI</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="description" content="Social media analytic tool">
        <meta name="author" content="Michal Dyzma">
    </head>
    <body>
        <h1>Home Page</h1>

    </body>
</html>
"""

#  We have to disale this i pyllint, because pylint will fail our build every
#  time it encounters this "global" variable
app = ChangePop.create_app() # pylint: disable=invalid-name


if __name__ == '__main__':
    app.run()
