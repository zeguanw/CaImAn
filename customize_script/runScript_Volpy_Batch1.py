# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 00:55:02 2019

@author: Jack
"""

#from fish_single_layer import volpy_process_session
from fish_single_layer_auto import volpy_process_session
#from fish_single_layer_manual import volpy_process_session
#from fish_single_layer_auto_two_trials import volpy_process_session

#work_dir_trial_1 =  '/media/jack/data/zebrafish/230820/Fish2_1/stitched/aligned_layers'
#work_dir_trial_2 =  '/media/jack/data/zebrafish/230820/Fish2_2/stitched/aligned_layers'

work_dir_trial_1 = '/media/jack/B87E692B7E68E39A/20230826_gal4_3xPosi2_5-6dpf_xcaspr_F2_40us_4980us_UV/Fish5_2/stitched/aligned_layers'
#work_dir_trial_2 = '/media/jack/B87E692B7E68E39A/20230826_gal4_3xPosi2_5-6dpf_xcaspr_F2_40us_4980us_UV/Fish5_3/stitched/aligned_layers'

#work_dir_trial_1 =  '/media/jack/B87E692B7E68E39A/230820/Fish1_1/stitched/aligned_layers'
#work_dir_trial_2 =  '/media/jack/B87E692B7E68E39A/230820/Fish1_2/stitched/aligned_layers'

#work_dir =  '/media/jack/data/zebrafish/230809/Fish2_12_joint/camera2/aligned_layers'

data_name_all = [
                            'stitch_layer_0',
                              'stitch_layer_1',
                            'stitch_layer_2',
                            'stitch_layer_3',
                            'stitch_layer_7',
                            'stitch_layer_9',
                            'stitch_layer_10',
                           'stitch_layer_11',
                           'stitch_layer_12',
                           'stitch_layer_13',
                          'stitch_layer_14',
                          'stitch_layer_15',
                          'stitch_layer_16',
                          'stitch_layer_17',
                        'stitch_layer_18',
                        'stitch_layer_27',                  
                        'stitch_layer_19',
                        'stitch_layer_20',
                        'stitch_layer_24',
                        'stitch_layer_25',
                        'stitch_layer_26',    
                        'stitch_layer_28',
                          'stitch_layer_29',
                          'stitch_layer_21',
                          'stitch_layer_22',
                          'stitch_layer_23',
                          'stitch_layer_4',
                        'stitch_layer_5',
                          'stitch_layer_8',
                        'stitch_layer_6',
                    ]

# tiff_image_loc = [ 
#                     'all_trial_layer_0',
#                     'all_trial_layer_1',
#                     'all_trial_layer_2',
#                     'all_trial_layer_3',
#                     'all_trial_layer_4',
#                     'all_trial_layer_5',
#                     'all_trial_layer_6',
#                     'all_trial_layer_7',
#                     'all_trial_layer_8',
#                     'all_trial_layer_9',
#                     'all_trial_layer_10',
#                     'all_trial_layer_11',
#                     'all_trial_layer_12',
#                     'all_trial_layer_13',
#                     'all_trial_layer_14',
#                     'all_trial_layer_15',
#                     'all_trial_layer_16',
#                     'all_trial_layer_17',
#                     'all_trial_layer_18',
#                     'all_trial_layer_19',
#                     'all_trial_layer_20',
#                     'all_trial_layer_21',
#                     'all_trial_layer_22',
#                     'all_trial_layer_23',
#                     'all_trial_layer_24',
#                     'all_trial_layer_25',
#                     'all_trial_layer_26',
#                     'all_trial_layer_27',            
#                     'all_trial_layer_28',
#                     'all_trial_layer_29',  
#                     ]

for data_name in data_name_all:
    volpy_process_session(work_dir_trial_1, data_name)
#    volpy_process_session(work_dir_trial_1, work_dir_trial_2, data_name)


