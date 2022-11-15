# This code is reading the
import pandas as pd
import numpy as np
import datetime

############################################################################################################

def read_data():
    cols = ['id', 'id_type', 'public_id', 'hash_id', 'member_id', 'sn_member_id', 'sn_hash_id', 'r_member_id',
            't_hash_id', 'avatar_id', 'public_id_2', 'lh_id', 'profile_url', 'email', 'full_name', 'first_name',
            'last_name', 'original_first_name', 'original_last_name', 'custom_first_name', 'custom_last_name', 'avatar',
            'headline', 'location_name', 'industry', 'summary', 'address', 'birthday', 'badges_premium',
            'badges_influencer', 'badges_job_seeker', 'badges_open_link', 'current_company', 'current_company_custom',
            'current_company_position', 'current_company_custom_position', 'organization_1', 'organization_id_1',
            'organization_url_1', 'organization_title_1', 'organization_start_1', 'organization_end_1',
            'organization_description_1', 'organization_location_1', 'organization_website_1', 'organization_domain_1',
            'organization_2', 'organization_id_2', 'organization_url_2', 'organization_title_2', 'organization_start_2',
            'organization_end_2', 'organization_description_2', 'organization_location_2', 'organization_website_2',
            'organization_domain_2', 'organization_3', 'organization_id_3', 'organization_url_3',
            'organization_title_3', 'organization_start_3', 'organization_end_3', 'organization_description_3',
            'organization_location_3', 'organization_website_3', 'organization_domain_3', 'organization_4',
            'organization_id_4', 'organization_url_4', 'organization_title_4', 'organization_start_4',
            'organization_end_4', 'organization_description_4', 'organization_location_4', 'organization_website_4',
            'organization_domain_4', 'organization_5', 'organization_id_5', 'organization_url_5',
            'organization_title_5', 'organization_start_5', 'organization_end_5', 'organization_description_5',
            'organization_location_5', 'organization_website_5', 'organization_domain_5', 'organization_6',
            'organization_id_6', 'organization_url_6', 'organization_title_6', 'organization_start_6',
            'organization_end_6', 'organization_description_6', 'organization_location_6', 'organization_website_6',
            'organization_domain_6', 'organization_7', 'organization_id_7', 'organization_url_7',
            'organization_title_7', 'organization_start_7', 'organization_end_7', 'organization_description_7',
            'organization_location_7', 'organization_website_7', 'organization_domain_7', 'organization_8',
            'organization_id_8', 'organization_url_8', 'organization_title_8', 'organization_start_8',
            'organization_end_8', 'organization_description_8', 'organization_location_8', 'organization_website_8',
            'organization_domain_8', 'organization_9', 'organization_id_9', 'organization_url_9',
            'organization_title_9', 'organization_start_9', 'organization_end_9', 'organization_description_9',
            'organization_location_9', 'organization_website_9', 'organization_domain_9', 'organization_10',
            'organization_id_10', 'organization_url_10', 'organization_title_10', 'organization_start_10',
            'organization_end_10', 'organization_description_10', 'organization_location_10', 'organization_website_10',
            'organization_domain_10', 'languages', 'skills', 'twitters', 'tags', 'note', 'connected_at', 'mutual_count',
            'mutual_first_fullname', 'mutual_second_fullname', 'original_mutual_first_fullname',
            'original_mutual_second_fullname', 'custom_mutual_first_fullname', 'custom_mutual_second_fullname',
            'followers', 'member_distance', 'network_info_connection_count', 'network_info_following',
            'add_to_target_date', 'result_created_at', 'message_1_from', 'message_1_text', 'message_1_send_at',
            'replied_message_1_from', 'replied_message_1_text', 'replied_message_1_send_at', 'last_sent_message_from',
            'last_sent_message_text', 'last_sent_message_send_at', 'last_received_message_from',
            'last_received_message_text', 'xx', 'yy']
    df2 = pd.read_csv('LI_data.csv', sep=';', engine='python', names=cols)
    df2.drop(index=0, inplace=True)
    df2.drop(index=1, inplace=True)
    df3 = df2.drop(['sn_member_id', 'sn_hash_id', 'r_member_id', 't_hash_id', 'public_id_2', 'replied_message_1_from',
                    'replied_message_1_text', 'replied_message_1_send_at', 'last_sent_message_from',
                    'last_sent_message_text', 'last_sent_message_send_at', 'last_received_message_from',
                    'last_received_message_text', 'email', 'custom_mutual_second_fullname', 'message_1_from',
                    'message_1_text', 'message_1_send_at', 'custom_mutual_first_fullname', 'xx', 'yy'], axis=1)
    df4 = df3[
        ['current_company', 'organization_2', 'organization_3', 'organization_4', 'organization_5', 'organization_6',
         'organization_7', 'organization_8', 'organization_9', 'organization_10']]
    df_time = df3[['organization_start_1', 'organization_end_1', 'organization_start_2', 'organization_end_2',
                   'organization_start_3', 'organization_end_3', 'organization_start_4', 'organization_end_4',
                   'organization_start_5', 'organization_end_5', 'organization_start_6', 'organization_end_6',
                   'organization_start_7', 'organization_end_7', 'organization_start_8', 'organization_end_8',
                   'organization_start_9', 'organization_end_9', 'organization_start_10', 'organization_end_10']]
    df_time_copy = df_time.copy()
    for i in range(df4.shape[0]):
        for j in range(df4.shape[1]):
            if 'Adastra' in str(df4.iloc[i, j]):
                df4.iloc[i, j] = 'Adastra'


    return(df4, df_time)

#########################################################################################################

df_data, df_time = read_data()
