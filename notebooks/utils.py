#!/usr/bin/env python3
""" Created 13.06.20
Helper functions
@author: slitayem
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import textwrap
import seaborn as sns


def sort_dict_by_vals(dictionary, reverse=True):
    """
    Sort dictionary by values
    :param dictiory: Dictionary object
    :reverse(boolean): Set to True to sort the values in descending order
    """
    return {key: value for key, value in 
                   sorted(dictionary.items(), key=lambda item: item[1], reverse=reverse)}


def count_substr_in_column(data_frame, column_name, vals_set, desc=True):
    """
    Count the number of values containing for each substring in the provided list
    :param data_frame(DataFrame): DataFrame object
    :param column_name(string): column name
    :param vals_set(list(string)): List of substrings to count in the columns values
    :param desc(bool): Order the values in descending order if set to True
    :return: vals_count, vals_percentage: Dictionary of values count sorted in reverse order
        and dictionary of values percentage
    """
    vals_count = {}
    vals_percentage = {}
    for val in vals_set:
        vals_count[val] = data_frame[column_name].str.contains(
            val, regex=False, na=False).sum()
        vals_percentage[val] = vals_count[val] * 100 / data_frame[column_name].dropna().shape[0]
    vals_count = {
        key: value for key, value in 
        sorted(vals_count.items(), key=lambda item: item[1], reverse=desc)}
    vals_percentage = {
        key: value for key, value in 
        sorted(vals_percentage.items(), key=lambda item: item[1], reverse=desc)}
    return vals_count, vals_percentage


def count_splited_value(data_frame, column_name):
    """
    Split ';' separated Dataframe column content and 
    count the number of each unique value
    :param df(DataFrame): DataFrame object
    :param column_name(string): Column name
    :return: vals_count, vals_percentage: Dictionary of values count sorted in reverse order
        and dictionary of values percentage
    """
    vals_set = data_frame[column_name].dropna().apply(lambda row: str(row).split(';')).explode().unique()
    vals_count, vals_percentage = count_substr_in_column(data_frame, column_name, vals_set)
    return vals_count, vals_percentage


def display_values_above_bars(ax, values_list):
    """
    Add a list of values above matplotlib barchart
    :param ax(AxesSubplot): Subplot object
    :param values_list(list): List of values to add above the bars in the chart
    :return AxesSubplot
    """
    for i, child in enumerate(ax.get_children()[:len(values_list)]):
        if isinstance(child, matplotlib.patches.Rectangle):
            ax.text(i, child.get_bbox().y1 + 0.002, values_list[i], horizontalalignment ='center')
    return ax


def func_autopct(pct, allvals):
    absolute = int(pct/100. * np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)


def plot_and_show_pie(labels_list, values_list, title, index_explode, colors=None):
    """Plot a pie chart
    :param labels_list
    :param values_list
    :param title
    :param index_explode
    """
    if not colors:
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    fig, ax = plt.subplots()
    ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    ax.set_title(title)
    explode = (0.0,) * len(labels_list) # only "explode" the 2nd slice (i.e. 'Hogs')
    explode = explode[:3] + (0.1,) + explode[4:]
    ax.pie(values_list, explode=explode,
           labels=labels_list, autopct=lambda pct: func_autopct(pct, values_list), #autopct='%1.1f%%',
           colors=colors, shadow=True, radius=1, center=(0.5,0.5))

    plt.show()
    return ax


def plot_grouped_bars(dataframe, groups_column, series_column,
                      counts_column, title="", xlabel=None, ylabel=None,
                      ax=None, legend=True, palette="Blues_d"):
    """Plot grouped bar charts (multi-series)
    :param dataframe: DataFrame object
    :param groups_column(string): groups column name
    :param series_column(string): series column name
    :param counts_column(string): counts column name
    :param title(string): title
    :param xlabel(string): xlabel
    :param ylabel(string): ylabel
    :param ax: Axes object
    :param legend(boolean): Set to True to show the legend
    :palette (string): color palette
    """
    # plt.figure(figsize=(10, 8))
    
    if not ax:
        fig = plt.figure()  # create a figure object
        ax = fig.add_subplot(1, 1, 1)  # create an axes object in the figure
    splot=sns.barplot(x=groups_column, y=counts_column, hue=series_column,
                      data=dataframe,  palette=palette, ax=ax)
    
    ax.set_ylabel(ylabel if ylabel is not None else counts_column, size=10, fontweight='light')
    ax.set_xlabel(xlabel if xlabel is not None else groups_column, size=14)
    ax.set_title(title, size=14, fontweight='light')

    for p in splot.patches:
        splot.annotate(format(round(p.get_height()/1000), '.0f') + "K", 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha='center', va='center', 
                       size=10,
                       xytext=(0, -12), 
                       textcoords='offset points')

    # Split string xticks into multiple lines
    max_width = 20
    splot.set_xticklabels(textwrap.fill(x.get_text(), max_width) for x in splot.get_xticklabels())
    splot.set_xticklabels(
        splot.get_xticklabels(), 
        rotation=45, 
        horizontalalignment='right',
        fontweight='light',
        fontsize='small',
    );
    if legend:
        splot.legend(loc='center left', bbox_to_anchor=(0, -0.5), ncol=1)
    else:
        ax.get_legend().remove()
    return splot
