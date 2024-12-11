
import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            all_data.append(line.strip())

if __name__ == '__main__':
    filenames = [f'./file_{number}.txt' for number in range(1, 5)]

# Линейный вызов
    start_time = time.time()
    for filename in filenames:
        result = read_info(filename)
    end_time = time.time()
    time_result = end_time - start_time
    print(f'{time_result:.6f} - Линейный вызов')

# Многопроцессный вызов
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        multiprocessing_results = pool.map(read_info, filenames)
    end_time = time.time()
    time_result = end_time - start_time
    print(f'{time_result:.6f} - Многопроцессный вызов')


