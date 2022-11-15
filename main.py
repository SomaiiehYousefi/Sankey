# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import numpy as np
import datetime
import matplotlib as plt
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
import read_data

#############################################################################################
cols = ['id','id_type', 'public_id', 'hash_id', 'member_id', 'sn_member_id', 'sn_hash_id', 'r_member_id', 't_hash_id', 'avatar_id', 'public_id_2', 'lh_id', 'profile_url', 'email', 'full_name', 'first_name', 'last_name', 'original_first_name', 'original_last_name', 'custom_first_name', 'custom_last_name', 'avatar', 'headline', 'location_name', 'industry', 'summary', 'address', 'birthday', 'badges_premium', 'badges_influencer', 'badges_job_seeker', 'badges_open_link','current_company','current_company_custom', 'current_company_position', 'current_company_custom_position', 'organization_1', 'organization_id_1', 'organization_url_1', 'organization_title_1', 'organization_start_1', 'organization_end_1', 'organization_description_1', 'organization_location_1', 'organization_website_1', 'organization_domain_1', 'organization_2','organization_id_2', 'organization_url_2', 'organization_title_2', 'organization_start_2','organization_end_2', 'organization_description_2', 'organization_location_2', 'organization_website_2', 'organization_domain_2', 'organization_3', 'organization_id_3', 'organization_url_3', 'organization_title_3', 'organization_start_3', 'organization_end_3', 'organization_description_3', 'organization_location_3','organization_website_3', 'organization_domain_3', 'organization_4', 'organization_id_4', 'organization_url_4', 'organization_title_4', 'organization_start_4', 'organization_end_4', 'organization_description_4', 'organization_location_4', 'organization_website_4', 'organization_domain_4', 'organization_5','organization_id_5','organization_url_5','organization_title_5', 'organization_start_5', 'organization_end_5', 'organization_description_5','organization_location_5', 'organization_website_5', 'organization_domain_5', 'organization_6', 'organization_id_6', 'organization_url_6', 'organization_title_6', 'organization_start_6', 'organization_end_6', 'organization_description_6', 'organization_location_6', 'organization_website_6', 'organization_domain_6', 'organization_7', 'organization_id_7', 'organization_url_7', 'organization_title_7', 'organization_start_7','organization_end_7', 'organization_description_7', 'organization_location_7','organization_website_7','organization_domain_7', 'organization_8', 'organization_id_8', 'organization_url_8','organization_title_8', 'organization_start_8','organization_end_8', 'organization_description_8', 'organization_location_8', 'organization_website_8', 'organization_domain_8', 'organization_9', 'organization_id_9', 'organization_url_9', 'organization_title_9', 'organization_start_9', 'organization_end_9','organization_description_9', 'organization_location_9', 'organization_website_9', 'organization_domain_9', 'organization_10', 'organization_id_10', 'organization_url_10', 'organization_title_10', 'organization_start_10', 'organization_end_10', 'organization_description_10', 'organization_location_10', 'organization_website_10', 'organization_domain_10', 'languages', 'skills', 'twitters','tags','note','connected_at','mutual_count','mutual_first_fullname','mutual_second_fullname','original_mutual_first_fullname', 'original_mutual_second_fullname','custom_mutual_first_fullname', 'custom_mutual_second_fullname', 'followers', 'member_distance', 'network_info_connection_count', 'network_info_following', 'add_to_target_date', 'result_created_at','message_1_from','message_1_text', 'message_1_send_at', 'replied_message_1_from','replied_message_1_text', 'replied_message_1_send_at','last_sent_message_from', 'last_sent_message_text', 'last_sent_message_send_at', 'last_received_message_from', 'last_received_message_text', 'xx', 'yy']
df2 = pd.read_csv('LI_data.csv', sep= ';', engine='python', names = cols)
df2.drop(index=0, inplace =True)
df2.drop(index=1, inplace =True)
df3 = df2.drop(['sn_member_id', 'sn_hash_id', 'r_member_id','t_hash_id','public_id_2', 'replied_message_1_from','replied_message_1_text', 'replied_message_1_send_at', 'last_sent_message_from', 'last_sent_message_text','last_sent_message_send_at', 'last_received_message_from', 'last_received_message_text','email', 'custom_mutual_second_fullname', 'message_1_from', 'message_1_text','message_1_send_at','custom_mutual_first_fullname', 'xx', 'yy'], axis =1)
df4 = df3[['current_company', 'organization_2', 'organization_3', 'organization_4', 'organization_5', 'organization_6', 'organization_7', 'organization_8', 'organization_9', 'organization_10']]
df_time = df3[['organization_start_1', 'organization_end_1', 'organization_start_2', 'organization_end_2', 'organization_start_3', 'organization_end_3', 'organization_start_4', 'organization_end_4', 'organization_start_5', 'organization_end_5', 'organization_start_6', 'organization_end_6', 'organization_start_7', 'organization_end_7', 'organization_start_8', 'organization_end_8', 'organization_start_9', 'organization_end_9', 'organization_start_10', 'organization_end_10']]
df_time_copy = df_time.copy()

v = pd.DataFrame(index=None, columns= None)
v = v.fillna(0)

#####  Find and replace Adastra where the position field record contains Adastra ###########
class PlotLinkedIN():
    def __init__(self, df_data):
        self.df_data = df_data
        self.df_time = df_time

    def fill_missing_dates(self):  # Fills missing end dates

        df_time_copy_ = self.df_time.copy()

        for t_row in range(1, df_time_copy_.shape[0]):
            if pd.isna(df_time_copy_.iloc[t_row, 1]):
                now = datetime.datetime.now()
                df_time_copy_.iloc[t_row, 1] = now.date()
                date_new_format = str(df_time_copy_.iloc[t_row, 1]).replace('-', '.', 2)
                df_time_copy_.iloc[t_row, 1] = date_new_format

                for t_column in range(3, df_time.shape[1], 2):
                    if pd.isna(df_time_copy_.iloc[t_row, t_column]):
                        df_time_copy_.iloc[t_row, t_column] = df_time_copy_.iloc[t_row, t_column - 3]
                df_time_copy_update = df_time_copy_

        return (df_time_copy_update)

    def find_adastra(self): #Finds Adastra and the company after Adastra
        X1 = self.df_data.copy()
        X1.reset_index(inplace=True)
        X1.drop(columns=['index'], axis=1, inplace=True)
        df_temp = pd.DataFrame(index=None, columns=None)
        df_temp = df_temp.fillna(0)
        after_ada_arr = np.empty(0)
        found_ada_arr = np.empty(0)

        for row in range(1, X1.shape[0]):
            if pd.isna(X1.iloc[row, 0]):
                X1.iloc[row, 0] = 'Unknown'
            # current_job.append(X1.iloc[row, 0])
            # df_current_job = pd.DataFrame([current_job], columns=None)

            for column in range(1, X1.shape[1]):
                if pd.isna(X1.iloc[row, column]):
                    X1.iloc[row, column] = 'Unknown'
                if X1.iloc[row, column] == 'Adastra':
                    found_ada_arr = np.append(found_ada_arr, X1.iloc[row, column])  # Could be replaced with the function finding Adastra in any company or duty
                    after_ada_arr = np.append(after_ada_arr, X1.iloc[row, column - 1])
                    df_temp = pd.DataFrame([found_ada_arr, after_ada_arr], index=None, columns=None)
                    break
                # elif X1.iloc[row, column] == 'Unknown':
                # Function search in the fields
                # else:
                # continue

        return (df_temp)


#### A copy of the data frame is generated
X1 = df4.copy()
X1.reset_index(inplace=True)
X1.drop(columns=['index'], axis=1, inplace=True)


df_temp = pd.DataFrame(index=None, columns= None)
df_temp = df_temp.fillna(0)
df_found_adastra = pd.DataFrame(index=None, columns= None)
df_found_adastra = df_found_adastra.fillna(0)
after_ada_arr = np.empty(0)
found_ada_arr = np.empty(0)


#### Fills missing end dates ########################################
for t_row in range(1, df_time_copy.shape[0]):
    if pd.isna(df_time_copy.iloc[t_row, 1]):
        now = datetime.datetime.now()
        df_time_copy.iloc[t_row, 1] = now.date()
        date_new_format = str(df_time_copy.iloc[t_row, 1]).replace('-','.', 2)
        df_time_copy.iloc[t_row, 1] = date_new_format

        for t_column in range(3, df_time.shape[1], 2):
            if pd.isna(df_time_copy.iloc[t_row, t_column]):
                df_time_copy.iloc[t_row, t_column] = df_time_copy.iloc[t_row, t_column-3]

#Finds Adastra and the company after Adastra
for row in range(1,X1.shape[0]):
    if pd.isna(X1.iloc[row, 0]):
        X1.iloc[row, 0] = 'Unknown'
    # current_job.append(X1.iloc[row, 0])
    # df_current_job = pd.DataFrame([current_job], columns=None)

    for column in range(1, X1.shape[1]):
        if pd.isna(X1.iloc[row, column]):
            X1.iloc[row, column] = 'Unknown'
        if X1.iloc[row, column] == 'Adastra':
            found_ada_arr = np.append(found_ada_arr, X1.iloc[row, column])     # Could be replaced with the function finding Adastra in any company or duty
            after_ada_arr = np.append(after_ada_arr, X1.iloc[row, column-1])
            df_temp = pd.DataFrame([found_ada_arr, after_ada_arr], index=None, columns=None)
            break
        #elif X1.iloc[row, column] == 'Unknown':
            # Function search in the fields
        #else:
            #continue

        df_csv = df_temp.to_csv(r'C:\Users\Somaiieh.Yousefi\PycharmProjects\Sankey\df_temp.csv', index= False)
        pivoted = df_temp.pivot(index="date", columns="variable", values="value")


print('end')



















