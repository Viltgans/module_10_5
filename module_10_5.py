import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    start_time = datetime.now()
    for filename in filenames:
        read_info(filename)
    end_time = datetime.now() - start_time
    print(f'{end_time} (линейный)')

    with multiprocessing.Pool(processes=4) as pool:
        start_time = datetime.now()
        pool.map(read_info, filenames)
    end_time = datetime.now() - start_time
    print(f'{end_time} (многопроцессный)')