# StackOverflow 2019 survey data analysis

## Table of Contents
1. [Description](#desc)
2. [Used Data and answered questions](#used_data)
3. [Data Analysis and insights extraction notebook](#analysis)
4. [Running the notebook](#run)
5. [Author](#author)
6. [License](#license)

<a name="desc"></a>
# Description

This Project is done in the context of Data Science Nanodegree Program by [Udacity](https://www.udacity.com/course/data-scientist-nanodegree--nd025).

Key Steps of the project in finding the solutions are:

1) Picking a dataset.

2) Posing at least three questions related to business or real-world applications of how the data could be used.

3) Performing necessary cleaning, analysis, and modeling.
    - Data preparation:
        - Gather necessary data to answer the questions
        - Handle categorical and missing data
        - Provide insight into the chosen methods and why they were chosen

    - Data Analyzis, Modeling, and Visualization to provide a clear connection between the business questions and how the data answers them.

4) Sharing the business insights with stakeholders.

The project is following the [CRISP-DM](https://www.datasciencecentral.com/profiles/blogs/crisp-dm-a-standard-methodology-to-ensure-a-good-outcome) (Cross Industry Standard Process for Data Mining) process or methodology which consists of the following steps

* Business Understanding
* Data Understanding
* Data Preparation
* Data Modeling
* Results Evaluation

<a name="used_data"></a>
# Used Data and answered questions

The Stackoverflow Developer [survey](https://insights.stackoverflow.com/survey/) data from 2019 is used to answer the following questions regarding Open Source Software (OSS) contributions:

* How often do developers contribute to OSS?
* Do Hobyist developers contribute more often to OSS?
* Does OSS quality perception play a bias role towards OSS contribution?
* Are experienced developers contributing more frequently to OSS?
* Do developers contributing to the OSS have a higher income?

[Blog post](https://slitayem.github.io/blog/2020/06/14/oss-contrib-analysis)

<a name="analysis"></a>
# Analysis
The analysis notebook is available [here](notebooks/stackoverflow_survey_analysis.ipynb)

<a name="run"></a>
# Running the notebook

- Create a `Python 3.6` conda virtual environment

    `conda create --name py36 python=3.6`
- Activate the new environment

    `conda activate py36`
- Install required packages by running the following command in the app's directory
    `pip install -r requirements.txt`
- Extract data folder

    `unzip data/so_survey_2019/so_developer_survey_2019.zip -d data/so_survey_2019/`
- run `jupyter lab`

If you want to just display the notebook content and its outputs use [nbviewer](https://nbviewer.jupyter.org/github/slitayem/stackoverflow_survey_analysis/blob/master/notebooks/stackoverflow_survey_analysis.ipynb). Also an html format of the notebook can be viewed [here](https://nbviewer.jupyter.org/github/slitayem/stackoverflow_survey_analysis/blob/master/notebooks/stackoverflow_survey_analysis.html).

<a name="author"></a>
## Author
* [Saloua Litayem](https://github.com/slitayem)

<a name="license"></a>
## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)