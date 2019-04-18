from celery import Celery
from algorithm import approx

app = Celery(__name__,backend='rpc://', broker='redis://localhost:6379')
#integrate = app.task(approx)


@app.task
def integrate(*args, **kwargs):
    try:
        return approx(*args, **kwargs)
    except Exception:
        return


        #celery -A worker worker --loglevel=debug
        # at worker side:
        # set FORKED_BY_MULTIPROCESSING = 1
        # then
        # celery -A myworker worker --loglevel=info
        # done!