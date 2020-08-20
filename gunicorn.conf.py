import multiprocessing

bind = "18.236.254.76:8000"
workers = multiprocessing.cpu_count() * 2 + 1