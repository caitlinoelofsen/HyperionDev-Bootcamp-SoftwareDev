#!/bin/bash

if [ -d "new_folder" ]; then
    mkdir if_folder

    if [ -d "if_folder" ]; then
        mkdir hyperionDev
    else
        mkdir new-projects
    fi
else
     mkdir new-projects
fi

pwd
