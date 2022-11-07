from reader import single_tread_count_unique_word
import time


start_time = time.time()

def main():

    single_tread_count_unique_word('out_Qmb.txt', 'count_pairs_single.txt')

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
