import json

from aiohttp import web

from generator_dict import worker_dictionary_generator
from routes import setup_routes
from constants import WORKERS_FILE_NAME


async def init_app():
    app = web.Application()
    setup_routes(app)
    with open(WORKERS_FILE_NAME, 'w') as f:
        workers = worker_dictionary_generator()
        workers_json_to_write = json.dumps(
            workers,
            ensure_ascii=False,
            indent=4
        )
        f.write(workers_json_to_write)

    return app


def main():
    app = init_app()
    web.run_app(app)


if __name__ == '__main__':
    main()
