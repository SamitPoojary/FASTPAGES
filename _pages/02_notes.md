---
toc: true
layout: post
description: Notes, terms, and ideas for APCSP
author: Samit Poojary
categories: [notes, markdown, AP CSP]
permalink: /notes/
title: APCSP Notes!
---

## Week 0
- Tool Setup
- PowerShell
    - cd = change directory
    - code . = open VSCode via terminal
    - ls = list files
- Markdown (md)
    - #, ##, ### = types of font (Heading, Subheading, etc.)
    - Use hyphens to create a bullet point

## Week 1
- Intro to Python
    - print () = displays whatever is in quotations
    - def = defines a function which can then be used in the future


## Week 2
- 



## Coding Through Terminal

```bash
(base) samitpoojary@Samits-MacBook-Pro ~ % cd vscode
(base) samitpoojary@Samits-MacBook-Pro vscode % cd fastpages
(base) samitpoojary@Samits-MacBook-Pro fastpages % code .
```

## How to Create a Notebook Using Bash:

1. First, enter vscode through terminal

2. Use these commands with python:

```bash
echo "Using conditional statement to create a project directory and project"

# Variable section
export project_dir=$HOME/vscode  # change vscode to different name to test git clone
export project=$project_dir/APCSP  # change APCSP to name of project from git clone
export project_repo="https://github.com/nighthawkcoders/APCSP.git"  # change to project of choice

cd ~    # start in home directory

# Conditional block to make a project directory
if [ ! -d $project_dir ]
then 
    echo "Directory $project_dir does not exists... makinng directory $project_dir"
    mkdir -p $project_dir
fi
echo "Directory $project_dir exists." 

# Conditional block to git clone a project from project_repo
if [ ! -d $project ]
then
    echo "Directory $project does not exists... cloning $project_repo"
    cd $project_dir
    git clone $project_repo
    cd ~
fi
echo "Directory $project exists." 
```

