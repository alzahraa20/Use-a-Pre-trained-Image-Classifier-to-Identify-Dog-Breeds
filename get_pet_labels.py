#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Alzahraa Shaheen
# DATE CREATED: 8/8/2021                                      
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    filenames = listdir(image_dir)
    
    results_dic = dict()
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label    
    for i in range(0, len(filenames), 1):
        # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
        # isn't an pet image file
        if in_files[idx][0] != ".":
            name = filenames[i]
            low_name = name.lower()
            # Splits lower case string by _ to break into words 
            word_list_name = low_name.split("_")
            pet_label = ""
            for word in word_list_name:
                if word.isalpha():
                    pet_label += word + " "

            pet_label = pet_label.strip()
            
           # If filename doesn't already exist in dictionary add it and it's
           # pet label - otherwise print an error message because indicates 
           # duplicate files (filenames)

            if filenames[i] not in results_dic:
                 results_dic[filenames[i]] = [pet_label]
            else:
                 print("** Warning: Key=", filenames[i], 
                       "already exists in results_dic with value =", 
                       results_dic[filenames[i]])

    for key in results_dic:
        print("Filename=", key, "   Pet Label=", results_dic[key][0]) 


    return results_dic
