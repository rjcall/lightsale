import multiprocessing

bind = "172.26.15.124:8000"
workers = multiprocessing.cpu_count() * 2 + 1


