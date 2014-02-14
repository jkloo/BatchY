# Purpose

> This file contains the initial thoughts behind the creation of BatchY

The purpose of batchy is to allow simultaneous edits to be made across multiple YAML files. These feature may not be developed yet.

# Usages
These 'files' will be used in the following example usages:

    # jeff.yml
    pets:
        - cat
        - dog
        - fish
    car: camry

    # dave.yml
    pets:
        - dog
        - bird
    car: mustang

## General

    # allow file-scoping with --files [FILES, ...]
    # allow directory-scoping with --dirs [DIRS, ...]

## Context Find-Replace

    batchy find dog
    >> jeff.yml, dave.yml

    batchy find dog --replace doggy
    >> modified: jeff.yml, dave.yml

    batchy find dog --keys car
    >> None    

    batchy find dog --keys car --replace doggy
    >> modified: None

## Modify Keys

Enable the user to update the value of a key in all files

    # add the key: value pair to all yaml files
    batchy update (key) (value) --add

    # append the value to the key
    batchy update (key) (value) --append

    # over write the key value pair
    batchy update (key) (value)

## View Coalescence 

Enable the user to view portions of multiple YAML files at once.

    batchy view
    >> 
    --- #jeff.yml
    pets:
        - cat
        - dog
        - fish
    car: camry
    --- # dave.yml
    pets:
        - dog
        - bird
    car: mustang

    batchy view --keys pets
    >> 
    --- #jeff.yml
    pets:
        - cat
        - dog
        - fish
    --- # dave.yml
    pets:
        - dog
        - bird
