from views import workers_get, workers_post


def setup_routes(app):
    app.router.add_get('/get', workers_get, name='get')
    app.router.add_post('/post', workers_post, name='post')


