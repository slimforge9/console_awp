# database of fields coordinates to fill in chosen forms
fields_db = {'detain':
                 {'page0':
                         {'name': [70, 79],
                          'surname': [135, 79],
                          # detain_time
                          'hd': [359, 64], 'hj': [373, 64], 'hmd': [386, 64], 'hmj': [400, 64],
                          ## detain_date
                          # day
                          'ddd': [426, 64], 'ddj': [438, 64], 'dmd': [453, 64], 'dmj': [467, 64],
                          # year
                          'dyt': [481, 64], 'dys': [495, 64], 'dyd': [508, 64], 'dyj': [522, 64],
                          'other_basis': [100, 178],
                          'detain_place': [85, 212],
                          'officer_name': [85, 235],
                          'officer_unit': [312, 235],
                          'doc_place': [85, 269],
                          # doc_time
                          'doc_hd': [362, 265], 'doc_hj': [377, 265], 'doc_hmd': [391, 265], 'doc_hmj': [404, 265],
                          ## doc_date
                          # day, month
                          'doc_ddd': [430, 265], 'doc_ddj': [444, 265], 'doc_dmd': [458, 265], 'doc_dmj': [471, 265],
                          # year
                          'doc_dyt': [485, 265], 'doc_dys': [499, 265], 'doc_dyd': [512, 265], 'doc_dyj': [525, 265],
                          'others': [208, 293],
                          'name2': [144, 332],
                          'surname2': [205, 332],
                          'family_name': [365, 332],
                          'dad_name': [144, 358],
                          'mom_name': [205, 358],
                          'mom_family': [365, 358],
                          'p_no': [104, 388],
                          'birth_place': [160, 417],
                          'address': [170, 465],
                          'job': [98, 490],
                          'ID': [300, 516],
                          'detain_basis': [64, 583]},
                  'page1':
                         {'rights': [44, 10],
                          'health': [44, 60],
                          # end_hour
                          'ehd': [154, 242], 'ehj': [167, 242], 'emd': [181, 242], 'emj': [193, 242],
                          # end date day/month
                          'eddd': [221, 242], 'eddj': [235, 242], 'edmd': [248, 242], 'edmj':[261, 242],
                          # end_date year
                          'edyt': [275, 242], 'edys': [288, 242], 'edyd': [302, 242], 'edyj': [315, 242],
                          'name3': [230, 472],
                          'surname3': [270, 472]
                          }},
             'warrant':
                 {'page0':
                      {'name': [130, 280],
                       'surname': [200, 280],
                       'dad_name': [410, 280],
                       'p_no': [360, 315],
                       'birth_date': [75, 315],
                       'birth_place': [200, 315],
                       'supervisor': [130, 374],
                       'doc_city': [350, 140],
                       'doc_date': [350, 140],  # original 445, 140
                       'doc_time': [350, 140]}},  # original 515, 140
             '79':
                 {'page0':
                        {'doc_city': [330, 43],
                         'doc_date': [330, 43], # [425, 43]
                         'name': [90, 163],
                         'surname': [160, 163],
                         'hold_time': [340, 163],
                         'hold_date': [440, 163],
                         'officer_name': [70, 228],
                         'officer_unit': [340, 228],
                         'name2': [220, 278],
                         'surname2': [277, 278],
                         'family_name': [395, 278],
                         'birth_date': [72, 306],
                         'birth_place': [162, 306],
                         'dad_name': [272, 306],
                         'mom_name': [334, 306],
                         'mom_family': [410, 306],
                         'address': [175, 349],
                         'job': [108, 383],
                         'ID': [317, 419],
                         'p_no': [380, 454],
                         '79_basis': [55, 565]
                        }},
             'rej':
                 {'page0':
                    {'officer_name': [54, 10],
                     'doc_city': [370, 10],
                     'doc_date': [370, 10],
                     'officer_unit': [54, 43],
                     'officer_id': [54, 80],
                     'act_time_date': [255, 245],
                     'act_place': [255, 265],
                     'act_description': [255, 283],
                     'offense_base': [150, 335],
                     'qual': [320, 335],
                     'item_value': [227, 358],
                     'act_time_date2': [255, 384],
                     'how_notify': [255, 402],
                     'act_time_date3': [255, 430],
                     'rej_type': [255, 456],
                     'end_type': [255, 474],
                     # Person
                     'name': [255, 512],
                     'surname': [315, 512],
                     'dad_name': [255, 534],
                     'mom_name': [315, 534],
                     'mom_family': [375, 534],
                     'birth_date': [255, 557],
                     'birth_place': [329, 557],
                     'ID': [255, 575],
                     'address': [255, 593],
                     'p_no': [255, 611],
                     'nationality': [255, 629],
                     'sex': [315, 629],
                     'job': [255, 655],
                     'retained_item': [255, 681],
                     'spb': [255, 704]},
                  'page1':
                     {'victim': [255, 263],
                      'subject': [255, 314]}
                  },

             }



