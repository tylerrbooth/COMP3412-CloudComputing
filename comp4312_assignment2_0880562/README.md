# Exercise 2 - Assignment 2

## Introduction
Some utility functions provided by GOOGLE are introduced in this assignment to help us interact with 
[google cloud storage](https://cloud.google.com/storage). They are:

    1. storage_copy_file.py: Copies a blob from one bucket to another with a new name.
    2. storage_create_bucket.py: Creates a new bucket.
    3. storage_delete_bucket.py: Deletes a bucket.
    4. storage_delete_file.py: Deletes a blob from the bucket.
    5. storage_download_file.py: Downloads a blob from the bucket.
    6. storage_list_buckets.py: Lists all buckets.
    7. storage_list_files.py: Returns a list of all the blobs in the bucket.
    8. storage_list_files_with_prefix.py: Lists all the blobs in the bucket that begin with the prefix.
    9. storage_make_public.py: Makes a blob publicly accessible.
    10. storage_move_file.py: Renames a blob.
    11. storage_upload_file.py: Uploads a file to the bucket.

In addition, you are also given the solution of assignment 1 as follows: 

    12. storage_upload_files_sln.py: Uploads a list of multiple files to the bucket
    13. storage_download_files_sln.py: Download a list of blobs from the bucket

## Problem statement: Deploy a project on Google AppEngine

You are required to:

1. Complete all preserved parts in [**app.py**](app.py) to build three endpoints:
    1. **list_files**: shows all blobs in a bucket
    2. **create_bk**: creates a bucket
    3. **delete_bk**: deletes a bucket
2. Add all necessary files before deployment
3. Deploy this project on Google AppEngine

Expectations: If completing this project properly, we are able to serve three endpoints online, 
that users could use web browsers to access url addresses of these endpoints 
(e.g. *https://oceanic-depth-288706.ue.r.appspot.com/* and 
*https://oceanic-depth-288706.ue.r.appspot.com/list_files?bucket_name=comp4312_1000*)

## Hints
1. Copy all codes in the **assignment2** folder to a new folder called **comp4312_assignment2_YourStudentID**
2. Create an venv (Unix-based OS only)
    ```commandline
    python3.8 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    ```
3. Install python libraries to be able to run these scripts 
    ```commandline
    pip install lib1
    pip install lib2
    ...
    ```
4. Run ```python storage_upload_files_sln.py``` to upload all files 
in the *images/upload* folder to the *comp4312_1000* bucket 
5. Edit [**app.py**](app.py)
6. Add compulsory files to deploy on Google AppEngine (e.g. requirements.txt, ...)
7. Test locally by running ```python app.py``` and accessing these endpoints
8. Deploy this folder on Google AppEngine by running ```gcloud app deploy``` 
9. Create a github repository named **comp4312_assignment2_YourStudentID** and push all codes into it
10. [IMPORTANT] Go to **AppEngine --> Settings** and click on **Disable Application** to save usage cost
