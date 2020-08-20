import multiprocessing

bind = "44.233.206.95:8000"
workers = multiprocessing.cpu_count() * 2 + 1