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

## VSCode Terminology:
- Source Control: This is the tab in VSCode where you stage, commit, and sync changes.
- Debug Console: This is where you can debug and work around any issues in your VSCode files.


## Largest Takeaway of Trimester 1:
- **Need to be more proactive on fastpages, and more consistent with commits and additions**
- Collaboration was on point this trimester, should be carrying it over into Tri 2
- **Rather than being a weekend worker, should be working more consistently throughout the week and accomplish more so that I have more time for other tasks**
- Flask site was solid, more could have been done to it and more consistent commits
- **My role during the Final project definitely could've been played out better, and as the Frontend devloper, once my duties have been complete, I should be helping out the Backend developer with their duties**
- Quality of the work was solid, but obviously room for improvement
- **should be more proactive about extra credit opportunities as well so as to stay ahead of the curve, and complete as much cs work as possible - this will allow me to better familiarize myself with cs components**
- More familiarized with JavaScript now, keep refining those skills to carry over into Tri 2
- **Should work to better understand components of JSON and its various applications**
- More familiarized with Python, and HTML... should continue to see rapid improvement come Tri 2
