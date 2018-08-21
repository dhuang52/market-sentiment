import sys
sys.path.append('./constants')
sys.path.append('./utils')

import file_utils, date_utils, news_utils
from datetime import datetime, timedelta


date_from = date_utils.get_date_week_ago('%Y-%m-%d')
all_news = news_utils.get_all_top_results('+snapchat', 'popularity', date_from, '100')


text_id = file_utils.create_unique_id()
file_id = '{0}_{1}.pickle'.format(text_id, 'news_api')
print(file_id)
save_successful = file_utils.write_pickle_to_data_dir(file_id, all_news)

if save_successful:
    print ('SAVE SUCCESSFUL')
else:
    print('SAVE UNSUCCESSFUL')
