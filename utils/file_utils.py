import random, string, pickle

# Store output data from scraping/API responses to the "data" directory
def write_to_data_dir(filename_with_ext, content):
    try:
        txt = open('./data/{0}'.format(filename_with_ext), 'w')
        txt.write(content)
        txt.close()
        return True
    except ValueError:
        print(ValueError)
        return False

# Store output data from scraping/API responses to the "data" directory as a .pkl
def write_pickle_to_data_dir(filename_with_ext, content):
    try:
        pkl = open('./data/{0}'.format(filename_with_ext), 'wb')
        pickle.dump(content, pkl)
        pkl.close()
        return True
    except ValueError:
        print(ValueError)
        return False

# generate a unique id for files to be saved
def create_unique_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))
