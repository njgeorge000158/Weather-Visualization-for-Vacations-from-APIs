#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  matplotlibx.py
 #
 #  File Description:
 #      This Python script, matplotlibx.py, contains generic Python functions
 #      for matplotlib charts and processing.  Here is the list:
 #
 #  display_linear_regression_line
 #  display_regression_line
 #
 #  display_line_chart_from_xy_series
 #
 #  display_box_plot_from_series_list
 #
 #  display_bar_chart_from_series
 #  display_bar_chart_from_dataframe
 #  
 #  display_scatter_plot_from_xy_series
 #  display_multiple_scatter_plots_from_xy_series_list
 #
 #  display_pie_chart_from_series
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/18/2023      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/

import logx
import mathx

import math

import matplotlib.pyplot as plt
import pandas as pd

from scipy import stats

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'matplotlibx.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  display_linear_regression_line
 #
 #  Function Description:
 #      This function displays a linear regression line.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series        This parameter is the x-axis series.
 #  series  y_series        This parameter is the y-axis series.
 #  float   x_coordinate_float
 #                          This parameter is the x-coordinate of the text.   
 #  float   y_coordinate_float
 #                          This parameter is the y-coordinate of the text.  
 #  string  line_color_string
 #                          This parameter is the line color.
 #  string  line_width_float
 #                          This parameter is the line type.
 #  float   alpha_float     This parameter is the alpha (transparency) value.  
 #  integer coefficient_precision_integer
 #                          This parameter is the equation coefficient precision. 
 #  float   fontsize_float  This parameter is the equation's font size. 
 #  string  fontweight_string
 #                          This parameter is the equation's font weight.
 #  string  fontcolor_string
 #                          This parameter is the equation's font color.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_linear_regression_line \
        (x_series,
         y_series,
         x_coordinate_float,
         y_coordinate_float,
         line_color_string = 'red',
         line_width_float = 3.0,
         alpha_float = 1.0,
         coefficient_precision_integer = 4,
         fontsize_float = 16.0,
         fontweight_string = 'bold',
         fontcolor_string = 'blue'):

    (slope, intercept, rvalue, pvalue, stderr) = stats.linregress(x_series, y_series)
            
    linear_regression_series = (x_series * slope) + intercept
            
        
    plt.plot \
        (x_series,
         linear_regression_series,
         color = line_color_string,
         linewidth = line_width_float,
         alpha = alpha_float)

            
    linear_equation_string \
        = 'y = ' + str(round(slope, coefficient_precision_integer)) \
          + 'x + ' + str(round(intercept, coefficient_precision_integer))
    
    plt.annotate \
        (linear_equation_string,
         (x_coordinate_float, y_coordinate_float),
         fontsize = fontsize_float,
         fontweight = fontweight_string,
         color = fontcolor_string)   

            
    r_squared_float = rvalue * rvalue

            
    logx.print_and_log_text('r-value:     {:.4f}'.format(rvalue))
        
    logx.print_and_log_text('r-squared:   {:.4f}\n'.format(r_squared_float))


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  display_polynomial_regression_line
 #
 #  Function Description:
 #      This function displays a single line chart from an x and y series and criteria.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series        This parameter is the x-axis series.
 #  series  y_series        This parameter is the y-axis series.
 #  float   x_coordinate_float
 #                          This parameter is the x-coordinate of the text.   
 #  float   y_coordinate_float
 #                          This parameter is the y-coordinate of the text.
 #  integer degree_integer  This parameter is the regression polynomial degree.
 #  string  line_color_string
 #                          This parameter is the line color.
 #  string  line_width_float
 #                          This parameter is the line type.
 #  float   alpha_float     This parameter is the alpha (transparency) value.  
 #  integer coefficient_precision_integer
 #                          This parameter is the equation coefficient precision. 
 #  float   fontsize_float  This parameter is the equation's font size. 
 #  string  fontweight_string
 #                          This parameter is the equation's font weight.
 #  string  fontcolor_string
 #                          This parameter is the equation's font color.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_polynomial_regression_line \
        (x_series,
         y_series,
         x_coordinate_float,
         y_coordinate_float,
         degree_integer,
         line_color_string = 'red',
         linewidth_float = 3.0,
         alpha_float = 1.0,
         coefficient_precision_integer = 4,
         fontsize_float = 16.0,
         fontweight_string = 'bold',
         fontcolor_string = 'blue'):

    model_equation_list \
        = mathx.return_regression_model_equation_coefficients \
            (x_series, y_series, degree_integer)
 
    polynomial_line_series = mathx.return_polynomial_line_series(x_series, y_series)
     
    plt.plot \
        (polynomial_line_series, 
         model_equation_list(polynomial_line_series),
         color = line_color_string,
         linewidth = linewidth_float,
         alpha = alpha_float)

            
    equation_label_string = mathx.return_equation_as_string(model_equation_list)
    
    plt.annotate \
        (equation_label_string,
         (x_coordinate_float, y_coordinate_float),
          fontsize = fontsize_float,
          fontweight = fontweight_string,
          color = fontcolor_string)

            
    r_squared_float = mathx.return_r_squared_value(x_series, y_series, degree_integer)
    
    r_value_float = math.sqrt(r_squared_float)

            
    logx.print_and_log_text('r-value:     {:.4f}'.format(r_value_float))
        
    logx.print_and_log_text('r-squared:   {:.4f}'.format(r_value_float))


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  display_line_chart_from_xy_series
 #
 #  Function Description:
 #      This function displays a single line chart from an x and y series and criteria.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series        This parameter is the x-axis series.
 #  series  y_series        This parameter is the y-axis series.
 #  string  caption_string  This parameter is the chart title.
 #  string  x_label_string  This parameter is the x-axis label.
 #  string  y_label_string  This parameter is the y-axis label.
 #  string  line_color_string
 #                          This parameter is the line color.
 #  string  line_type_string
 #                          This parameter is the line type.
 #  float   alpha_float     This parameter is the alpha (transparency) value.
 #  string  fill_style_string
 #                          This parameter is the line fills style.
 #  float   line_width_float
 #                          This parameter is the line width.       
 #  string  marker_string   This parameter is the marker type.
 #  string  marker_facecolor_string
 #                          This parameter is the marker face color.
 #  string  markeredgecolor_string
 #                          This parameter is the marker edge color.
 #  float   markersize_float
 #                          This parameter is the marker size.
 #  float   markeredgewidth This parameter is the marker edge width. 
 #  float   title_fontsize_float
 #                          This parameter is the title font size. 
 #  string  title_fontstyle_string
 #                          This parameter is the title font style.
 #  float   title_pad_float This parameter is the title space pad value. 
 #  float   xlabel_fontsize_float
 #                          This parameter is the x-axis font size. 
 #  string  xlabel_fontstyle_string
 #                          This parameter is the x-axis font style.
 #  float   xlabel_pad_float
 #                          This parameter is the x-axis space pad value. 
 #  float   ylabel_fontsize_float
 #                          This parameter is the y-axis font size. 
 #  string  ylabel_fontstyle_string
 #                          This parameter is the y-axis font style.
 #  float   ylabel_pad_float
 #                          This parameter is the y-axis space pad value. 
 #  float   xticks_fontsize_float
 #                          This parameter is the x-axis tick font size. 
 #  float   yticks_fontsize_float
 #                          This parameter is the y-axis tick font size. 
 #  float   figure_width_float
 #                          This parameter is the figure width. 
 #  float   figure_length_float
 #                          This parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_line_chart_from_xy_series \
        (x_series,
         y_series,
         caption_string,
         x_label_string,
         y_label_string,
         line_color_string = 'darkslategray',
         line_type_string = 'solid',
         alpha_float = 1.0,
         fill_style_string = 'full',
         line_width_float = 3.0,
         marker_string = 'o',
         marker_facecolor_string = 'red',
         markeredgecolor_string = 'black',
         markersize_float = 10.0,
         markeredgewidth = 1.0,
         title_fontsize_float = 20.0,
         title_fontstyle_string = 'normal',
         title_pad_float = 20.0,
         xlabel_fontsize_float = 16.0,
         xlabel_fontstyle_string = 'normal',
         xlabel_pad_float = 10.0,
         ylabel_fontsize_float = 16.0,
         ylabel_fontstyle_string = 'normal',
         ylabel_pad_float = 10.0,
         xticks_fontsize_float = 14.0,
         yticks_fontsize_float = 14.0,
         figure_width_float = 9.708,
         figure_length_float = 6.0):

    plt.figure(figsize = (figure_width_float, figure_length_float))
    
    plt.plot \
        (x_series,
         y_series,
         alpha = alpha_float,
         color = line_color_string,
         fillstyle = fill_style_string,
         linewidth = line_width_float,
         marker = marker_string,
         markerfacecolor = marker_facecolor_string,
         markeredgecolor = markeredgecolor_string,
         markersize = markersize_float,
         markeredgewidth = markeredgewidth,
         linestyle = line_type_string)

    plt.title \
        (caption_string,
         fontdict = {'fontsize': title_fontsize_float, 
                     'fontstyle': title_fontstyle_string},
         pad = title_pad_float)

    plt.xlabel \
        (x_label_string,
         fontdict = {'fontsize': xlabel_fontsize_float,
                     'fontstyle': xlabel_fontstyle_string},
         labelpad = xlabel_pad_float)

    plt.ylabel \
        (y_label_string,
         fontdict = {'fontsize': ylabel_fontsize_float,
                     'fontstyle': ylabel_fontstyle_string},
         labelpad = ylabel_pad_float)
        
    plt.xticks(fontsize = xticks_fontsize_float)
       
    plt.yticks(fontsize = yticks_fontsize_float)

            
    plt.grid()
            
    logx.save_plot_image(caption_string)

    plt.show()


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  display_box_plot_from_series_list
 #
 #  Function Description:
 #      This function displays a box plot from a list of series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list    input_series_list
 #                          This parameter is the input series list.
 #  list    xticks_label_string_list
 #                          This parameter is the list of a-axis tick labels.
 #  string  caption_string  This parameter is the chart title.
 #  string  x_label_string  This parameter is the x-axis label.
 #  string  y_label_string  This parameter is the y-axis label.
 #  float   box_widths_float
 #                          This parameter is the width of boxes in the chart.
 #  string  line_type_string
 #                          This parameter is the line type.
 #  float   alpha_float     This parameter is the alpha (transparency) value.
 #  string  fill_style_string
 #                          This parameter is the line fills style.
 #  float   line_width_float
 #                          This parameter is the line width.       
 #  boolean meanline_boolean
 #                          This parameter indicates whether the mean lines are present.
 #  boolean showmeans_boolean
 #                          This parameter indicates whether the means are present.
 #  boolean vertical_boolean
 #                          This parameter indicates whether the boxplot is vertical.
 #  float   title_fontsize_float
 #                          This parameter is the title font size. 
 #  string  title_fontstyle_string
 #                          This parameter is the title font style.
 #  float   title_pad_float This parameter is the title space pad value. 
 #  float   xlabel_fontsize_float
 #                          This parameter is the x-axis font size. 
 #  string  xlabel_fontstyle_string
 #                          This parameter is the x-axis font style.
 #  float   xlabel_pad_float
 #                          This parameter is the x-axis space pad value. 
 #  float   ylabel_fontsize_float
 #                          This parameter is the y-axis font size. 
 #  string  ylabel_fontstyle_string
 #                          This parameter is the y-axis font style.
 #  float   ylabel_pad_float
 #                          This parameter is the y-axis space pad value. 
 #  float   xticks_fontsize_float
 #                          This parameter is the x-axis tick font size. 
 #  float   yticks_fontsize_float
 #                          This parameter is the y-axis tick font size. 
 #  float   figure_width_float
 #                          This parameter is the figure width. 
 #  float   figure_length_float
 #                          This parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_box_plot_from_series_list \
        (input_series_list,
         xticks_label_string_list,
         caption_string,
         x_label_string,
         y_label_string,
         box_widths_float = 0.45,
         meanline_boolean = True,
         showmeans_boolean = True,
         vertical_boolean = True,
         title_fontsize_float = 20.0,
         title_fontstyle_string = 'normal',
         title_pad_float = 20.0,
         xlabel_fontsize_float = 16.0,
         xlabel_fontstyle_string = 'normal',
         xlabel_pad_float = 10.0,
         ylabel_fontsize_float = 16.0,
         ylabel_fontstyle_string = 'normal',
         ylabel_pad_float = 10.0,
         xticks_fontsize_float = 14.0,
         xticks_rotation_float = 0.0,
         figure_width_float = 9.708,
         figure_length_float = 6.0):
    
    fig1, ax = plt.subplots(figsize = (figure_width_float, figure_length_float))

    ax.boxplot \
        (input_series_list,
         vert = vertical_boolean,
         widths = box_widths_float,
         meanline = meanline_boolean, 
         showmeans = showmeans_boolean)
        
    ax.set_title \
        (caption_string,
         fontdict = {'fontsize': title_fontsize_float, 
                     'fontstyle': title_fontstyle_string},
         pad = title_pad_float)
        
    ax.set_xlabel \
        (x_label_string,
         fontdict = {'fontsize': xlabel_fontsize_float, 
                     'fontstyle': xlabel_fontstyle_string},
         labelpad = xlabel_pad_float)

    ax.set_ylabel \
        (y_label_string,
         fontdict = {'fontsize': ylabel_fontsize_float, 
                     'fontstyle': ylabel_fontstyle_string},
         labelpad = ylabel_pad_float)

        
    ticks_index_integer_list = []
        
    for index, regimen in enumerate(xticks_label_string_list):
            
        ticks_index_integer_list.append(index + 1)

        
    ax.set_xticks \
        (ticks_index_integer_list, 
         xticks_label_string_list,
         fontsize = xticks_fontsize_float,
         rotation = xticks_rotation_float)

        
    if vertical_boolean == True:
        
        plt.grid(axis = 'y')
        
    else:
            
        plt.grid(axis = 'x')

        
    logx.save_plot_image(caption_string)
        
    plt.show()


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  display_bar_chart_from_series
 #
 #  Function Description:
 #      This function displays a bar chart from a series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  input_series    This parameter is the input series.
 #  string  caption_string  This parameter is the chart title.
 #  string  x_label_string  This parameter is the x-axis label.
 #  string  y_label_string  This parameter is the y-axis label.
 #  list    bar_colors_string_list
 #                          This parameter is the list of bar colors.
 #  string  bar_align_string
 #                          This parameter is bar alignment.
 #  string  edge_color_string
 #                          This parameter is the bar edge color.
 #  float   line_width_float
 #                          This parameter is the bar line width.       
 #  float   alpha_float     This parameter is the bar transparency level (0-1.0).
 #  float   bar_width_float This parameter is the bar width.
 #  float   title_fontsize_float
 #                          This parameter is the title font size. 
 #  string  title_fontstyle_string
 #                          This parameter is the title font style.
 #  float   title_pad_float This parameter is the title space pad value. 
 #  float   xlabel_fontsize_float
 #                          This parameter is the x-axis font size. 
 #  string  xlabel_fontstyle_string
 #                          This parameter is the x-axis font style.
 #  float   xlabel_pad_float
 #                          This parameter is the x-axis space pad value. 
 #  float   ylabel_fontsize_float
 #                          This parameter is the y-axis font size. 
 #  string  ylabel_fontstyle_string
 #                          This parameter is the y-axis font style.
 #  float   ylabel_pad_float
 #                          This parameter is the y-axis space pad value. 
 #  float  xtick_label_rotation_float
 #                          This parameter is the x-axis tick rotation. 
 #  float  xtick_fontsize_float
 #                          This parameter is the x-axis tick font size.
 #  float  ytick_label_rotation_float
 #                          This parameter is the y-axis tick rotation. 
 #  float  ytick_fontsize_float
 #                          This parameter is the y-axis tick font size. 
 #  float  figure_width_float
 #                          This parameter is the figure width. 
 #  float  figure_length_float
 #                          This parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_bar_chart_from_series \
        (input_series,
         caption_string,
         x_label_string,
         y_label_string,
         bar_colors_string_list,
         bar_align_string = 'center',
         edge_color_string = 'black',
         line_width_float = 1.5,
         bar_width_float = 0.5,
         alpha_float = 1.0,
         title_fontsize_float = 20.0,
         title_fontstyle_string = 'normal',
         title_pad_float = 20.0,
         xlabel_fontsize_float = 16.0,
         xlabel_fontstyle_string = 'normal',
         xlabel_pad_float = 10.0,
         ylabel_fontsize_float = 16.0,
         ylabel_fontstyle_string = 'normal',
         ylabel_pad_float = 10.0,
         xtick_label_rotation_float = 80.0,
         xtick_fontsize_float = 14.0,
         ytick_label_rotation_float = 0.0,
         ytick_fontsize_float = 14.0,        
         figure_width_float = 9.708,
         figure_length_float = 6.0):
      
    plt.figure(figsize = (figure_width_float, figure_length_float))
        
    plt.bar \
        (input_series.keys(),
         input_series,
         align = bar_align_string,
         color = bar_colors_string_list,
         edgecolor = edge_color_string,
         linewidth = line_width_float,
         alpha = alpha_float,
         width = bar_width_float)
        
    plt.title \
        (caption_string,
         fontdict = {'fontsize': title_fontsize_float, 
                     'fontstyle': title_fontstyle_string},
         pad = title_pad_float)

    plt.xlabel \
        (x_label_string,
         fontdict = {'fontsize': xlabel_fontsize_float, 
                     'fontstyle': xlabel_fontstyle_string},
         labelpad = xlabel_pad_float)
        
    plt.ylabel \
        (y_label_string,
         fontdict = {'fontsize': ylabel_fontsize_float, 
                     'fontstyle': ylabel_fontstyle_string},
         labelpad = ylabel_pad_float)
        
    plt.xticks \
        (rotation = xtick_label_rotation_float,
         fontsize = xtick_fontsize_float)
        
    plt.yticks \
        (rotation = ytick_label_rotation_float,
         fontsize = ytick_fontsize_float)

            
    plt.grid(axis = 'y')
        
    logx.save_plot_image(caption_string)
        
    plt.show()


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  display_bar_chart_from_dataframe
 #
 #  Function Description:
 #      This function displays a bar chart from a dataframe.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_dataframe This parameter is the input dataframe.
 #  string  caption_string  This parameter is the chart title.
 #  string  x_label_string  This parameter is the x-axis label.
 #  string  y_label_string  This parameter is the y-axis label.
 #  list    bar_colors_string_list
 #                          This parameter is the list of bar colors.
 #  boolean stacked_boolean This parameter indicates whether the bar chart is stacked.
 #  boolean legend_boolean  This parameter indicates whether the legend is present.
 #  float   bbox_to_anchor_x_float
 #                          This parameter is the legend x-coordinate.  
 #  float   bbox_to_anchor_y_float
 #                          This parameter is the legend y-coordinate.  
 #  string  bar_align_string
 #                          This parameter is bar alignment.
 #  string  edge_color_string
 #                          This parameter is the bar edge color.
 #  float   line_width_float
 #                          This parameter is the bar line width.       
 #  float   alpha_float     This parameter is the bar transparency level (0-1.0).
 #  float   bar_width_float This parameter is the bar width.
 #  float   title_fontsize_float
 #                          This parameter is the title font size. 
 #  string  title_fontstyle_string
 #                          This parameter is the title font style.
 #  float   title_pad_float This parameter is the title space pad value. 
 #  float   xlabel_fontsize_float
 #                          This parameter is the x-axis font size. 
 #  string  xlabel_fontstyle_string
 #                          This parameter is the x-axis font style.
 #  float   xlabel_pad_float
 #                          This parameter is the x-axis space pad value. 
 #  float   ylabel_fontsize_float
 #                          This parameter is the y-axis font size. 
 #  string  ylabel_fontstyle_string
 #                          This parameter is the y-axis font style.
 #  float   ylabel_pad_float
 #                          This parameter is the y-axis space pad value. 
 #  float   xtick_label_rotation_float
 #                          This parameter is the x-axis tick rotation. 
 #  float   xtick_fontsize_float
 #                          This parameter is the x-axis tick font size.
 #  float   ytick_label_rotation_float
 #                          This parameter is the y-axis tick rotation. 
 #  float   ytick_fontsize_float
 #                          This parameter is the y-axis tick font size. 
 #  float   figure_width_float
 #                          This parameter is the figure width. 
 #  float   figure_length_float
 #                          This parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_bar_chart_from_dataframe \
        (input_dataframe,
         caption_string,
         x_label_string,
         y_label_string,
         bar_colors_string_list,
         stacked_boolean = False,
         legend_boolean = False,
         bbox_to_anchor_x_float = 1.1,
         bbox_to_anchor_y_float = 1.05,
         bar_align_string = 'center',
         edge_color_string = 'black',
         line_width_float = 1.5,
         bar_width_float = 0.5,
         alpha_float = 1.0,
         title_fontsize_float = 20.0,
         title_fontstyle_string = 'normal',
         title_pad_float = 20.0,
         xlabel_fontsize_float = 16.0,
         xlabel_fontstyle_string = 'normal',
         xlabel_pad_float = 10.0,
         ylabel_fontsize_float = 16.0,
         ylabel_fontstyle_string = 'normal',
         ylabel_pad_float = 10.0,
         xtick_label_rotation_float = 80.0,
         xtick_fontsize_float = 14.0,
         ytick_label_rotation_float = 0.0,
         ytick_fontsize_float = 14.0,
         figure_width_float = 9.708,
         figure_length_float = 6.0):
    
    input_dataframe.plot.bar \
        (stacked = stacked_boolean,
         align = bar_align_string,
         color = bar_colors_string_list,
         edgecolor = edge_color_string,
         linewidth = line_width_float,
         alpha = alpha_float,
         width = bar_width_float, 
         legend = legend_boolean,
         figsize = (figure_width_float, figure_length_float))

    if legend_boolean == True:
        
        plt.legend(bbox_to_anchor = (bbox_to_anchor_x_float, bbox_to_anchor_y_float))

        
    plt.title \
        (caption_string,
         fontdict = {'fontsize': title_fontsize_float, 
                     'fontstyle': title_fontstyle_string},
         pad = title_pad_float)

    plt.xlabel \
        (x_label_string,
         fontdict = {'fontsize': xlabel_fontsize_float,
                     'fontstyle': xlabel_fontstyle_string},
         labelpad = xlabel_pad_float)

    plt.ylabel \
        (y_label_string,
         fontdict = {'fontsize': ylabel_fontsize_float,
                     'fontstyle': ylabel_fontstyle_string},
         labelpad = ylabel_pad_float)
        
    plt.xticks \
        (rotation = xtick_label_rotation_float,
         fontsize = xtick_fontsize_float)
        
    plt.yticks \
        (rotation = ytick_label_rotation_float,
         fontsize = ytick_fontsize_float)

            
    plt.grid(axis = 'y')
        
    logx.save_plot_image(caption_string)
        
    plt.show()


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  display_scatter_plot_from_xy_series
 #
 #  Function Description:
 #      This function displays a scatter plot from x-y series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series        This parameter is the x-axis series.
 #  series  y_series        This parameter is the y-axis series.
 #  string  caption_string  This parameter is the chart title.
 #  string  x_label_string  This parameter is the x-axis label.
 #  string  y_label_string  This parameter is the y-axis label.
 #  integer degree_integer  This parameter is the degree of the regression line polynomial.
 #  float   equation_x_coordinate_float
 #                          This parameter is the equation's x-coordinate.  
 #  float   equation_y_coordinate_float
 #                          This parameter is the equation's y-coordinate.  
 #  string  marker_shape_string
 #                          This parameter is marker shape.
 #  float   marker_size_float
 #                          This parameter is the marker size.       
 #  string  marker_color_string
 #                          This parameter is the marker color.
 #  float   line_width_float
 #                          This parameter is line width of the scatter points.
 #  string  edge_colors_string
 #                          This parameter is the edge color for the scatter points.
 #  float   alpha_float
 #                          This parameter is the bar transparency level (0-1.0).
 #  float   title_fontsize_float
 #                          This parameter is the title font size. 
 #  string  title_fontstyle_string
 #                          This parameter is the title font style.
 #  float   title_pad_float
 #                          This parameter is the title space pad value. 
 #  float   xlabel_fontsize_float
 #                          This parameter is the x-axis font size. 
 #  string  xlabel_fontstyle_string
 #                          This parameter is the x-axis font style.
 #  float   xlabel_pad_float
 #                          This parameter is the x-axis space pad value. 
 #  float   ylabel_fontsize_float
 #                          This parameter is the y-axis font size. 
 #  string  ylabel_fontstyle_string
 #                          This parameter is the y-axis font style.
 #  float   ylabel_pad_float
 #                          This parameter is the y-axis space pad value. 
 #  float   xtick_label_rotation_float
 #                          This parameter is the x-axis tick rotation. 
 #  float   xtick_fontsize_float
 #                          This parameter is the x-axis tick font size.
 #  float   ytick_label_rotation_float
 #                          This parameter is the y-axis tick rotation. 
 #  float   ytick_fontsize_float
 #                          This parameter is the y-axis tick font size. 
 #  float   figure_width_float
 #                          This parameter is the figure width. 
 #  float   figure_length_float
 #                          This parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_scatter_plot_from_xy_series \
        (x_series, 
         y_series, 
         caption_string,
         x_label_string,
         y_label_string,
         degree_integer = 0,
         equation_x_coordinate_float = 0.0,
         equation_y_coordinate_float = 0.0,
         marker_shape_string = 'o',
         marker_size_float = 80.0,
         marker_color_string = 'lime',
         line_width_float = 1.5,
         edge_colors_string = 'black',
         alpha_float = 0.8,
         title_fontsize_float = 20.0,
         title_fontstyle_string = 'normal',
         title_pad_float = 20.0,
         xlabel_fontsize_float = 16.0,
         xlabel_fontstyle_string = 'normal',
         xlabel_pad_float = 10.0,
         ylabel_fontsize_float = 16.0,
         ylabel_fontstyle_string = 'normal',
         ylabel_pad_float = 10.0,
         xtick_label_rotation_float = 0.0,
         xtick_fontsize_float = 14.0,
         ytick_label_rotation_float = 0.0,
         ytick_fontsize_float = 14.0,        
         figure_width_float = 9.708,
         figure_length_float = 6.0):
      
    plt.figure(figsize = (figure_width_float, figure_length_float))
        
    plt.scatter \
        (x_series, 
         y_series, 
         marker = marker_shape_string,
         s = marker_size_float,
         color = marker_color_string, 
         linewidth = line_width_float,
         edgecolors = edge_colors_string,
         alpha = alpha_float)

    plt.title \
        (caption_string, 
         fontdict = {'fontsize': title_fontsize_float, 
                     'fontstyle': title_fontstyle_string},
         pad = title_pad_float)
    
    plt.xlabel \
        (x_label_string,
         fontdict = {'fontsize': xlabel_fontsize_float, 
                     'fontstyle': xlabel_fontstyle_string},
         labelpad = xlabel_pad_float)

    plt.ylabel \
        (y_label_string,
         fontdict = {'fontsize': ylabel_fontsize_float, 
                     'fontstyle': ylabel_fontstyle_string},
         labelpad = ylabel_pad_float)
        
    plt.xticks \
        (rotation = xtick_label_rotation_float,
         fontsize = xtick_fontsize_float)
        
    plt.yticks \
        (rotation = ytick_label_rotation_float,
         fontsize = ytick_fontsize_float)
        
    plt.grid()


    if degree_integer == 1:
            
        display_linear_regression_line \
            (x_series, y_series,
             equation_x_coordinate_float,
             equation_y_coordinate_float)
            
    elif degree_integer > 1:
                
        display_polynomial_regression_line \
            (x_series, y_series,
             equation_x_coordinate_float,
             equation_y_coordinate_float,
             degree_integer)

        
    logx.save_plot_image(caption_string)
        
    plt.show()


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  display_multiple_scatter_plots_from_xy_series_list
 #
 #  Function Description:
 #      This function displays multiple scatter plots from x-y series lists.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series_list   This parameter is the x-axis series list.
 #  series  y_series_list   This parameter is the y-axis series list.
 #  string  titles_string_list
 #                          This parameter is the chart title list.
 #  string  caption_string  This parameter is the figure title.
 #  string  x_label_string  This parameter is the x-axis label.
 #  string  y_label_string  This parameter is the y-axis label.
 #  integer degree_integer  This parameter is the degree of the regression line polynomial.
 #  float   equation_x_coordinate_float_list
 #                          This parameter is the list of equation's x-coordinates.  
 #  float   equation_y_coordinate_float_list
 #                          This parameter is the list of equation's y-coordinate.  
 #  string  marker_shape_string
 #                          This parameter is marker shape.
 #  float   marker_size_float
 #                          This parameter is the marker size.       
 #  string  marker_color_string
 #                          This parameter is the marker color.
 #  float   line_width_float
 #                          This parameter is line width of the scatter points.
 #  string  edge_colors_string
 #                          This parameter is the edge color for the scatter points.
 #  float   alpha_float     This parameter is the bar transparency level (0-1.0).
 #  float   suptitle_fontsize_float
 #                          This parameter is the figure title font size. 
 #  string  suptitle_fontstyle_string
 #                          This parameter is the figure title font style.
 #  float   suptitle_pad_float
 #                          This parameter is the figure title space pad value. 
 #  float   title_fontsize_float
 #                          This parameter is the title font size. 
 #  string  title_fontstyle_string
 #                          This parameter is the title font style.
 #  float   title_pad_float This parameter is the title space pad value. 
 #  float   xlabel_fontsize_float
 #                          This parameter is the x-axis font size. 
 #  string  xlabel_fontstyle_string
 #                          This parameter is the x-axis font style.
 #  float   xlabel_pad_float
 #                          This parameter is the x-axis space pad value. 
 #  float   ylabel_fontsize_float
 #                          This parameter is the y-axis font size. 
 #  string  ylabel_fontstyle_string
 #                          This parameter is the y-axis font style.
 #  float   ylabel_pad_float
 #                          This parameter is the y-axis space pad value. 
 #  float   xtick_label_rotation_float
 #                          This parameter is the x-axis tick rotation. 
 #  float   xtick_fontsize_float
 #                          This parameter is the x-axis tick font size.
 #  float   ytick_label_rotation_float
 #                          This parameter is the y-axis tick rotation. 
 #  float   ytick_fontsize_float
 #                          This parameter is the y-axis tick font size. 
 #  float   tight_layout_pad_float
 #                          This parameter is the figure tight layout padding. 
 #  float   figure_width_float
 #                          This parameter is the figure width. 
 #  float   figure_length_float
 #                          This parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_multiple_scatter_plots_from_xy_series_list \
        (x_series_list,
         y_series_list,
         titles_string_list,
         caption_string,
         x_label_string,
         y_label_string,
         degree_integer = 0,
         equation_x_coordinate_float_list = 0.0,
         equation_y_coordinate_float_list = 0.0,
         marker_shape_string = 'o',
         marker_size_float = 80.0,
         marker_color_string = 'lime',
         line_width_float = 1.5,
         edge_colors_string = 'black',
         alpha_float = 0.8,
         suptitle_fontsize_float = 20.0,
         suptitle_fontstyle_string = 'normal',
         suptitle_pad_float = 1.0,         
         title_fontsize_float = 20.0,
         title_fontstyle_string = 'normal',
         title_pad_float = 20.0,
         xlabel_fontsize_float = 16.0,
         xlabel_fontstyle_string = 'normal',
         xlabel_pad_float = 10.0,
         ylabel_fontsize_float = 16.0,
         ylabel_fontstyle_string = 'normal',
         ylabel_pad_float = 10.0,
         xtick_label_rotation_float = 0.0,
         xtick_fontsize_float = 14.0,
         ytick_label_rotation_float = 0.0,
         ytick_fontsize_float = 14.0,
         tight_layout_pad_float = 3.0,
         figure_width_float = 15.0,
         figure_length_float = 5.5181):

    scatter_plot_count_integer = len(x_series_list)
        
    if scatter_plot_count_integer != len(y_series_list):

        logx.print_and_log_text \
            ('The function, display_multiple_scatter_plots_from_xy_series_list, '
              + f'in source file, {CONSTANT_LOCAL_FILE_NAME},'
              + f'with the caption, {caption_string},'
              + 'was unable to display scatter plots '
              + 'because the number of x and y series did not match.')


    plt.subplots(figsize = (figure_width_float, figure_length_float))

    plt.clf()


    x_length_integer, y_length_integer \
        = mathx.calculate_closest_factors(scatter_plot_count_integer)
        

    for index in range(0, scatter_plot_count_integer):

        plt.subplot(x_length_integer, y_length_integer, index + 1)

        plt.scatter \
            (x_series_list[index], 
             y_series_list[index], 
             marker = marker_shape_string,
             s = marker_size_float,
             color = marker_color_string, 
             linewidth = line_width_float,
             edgecolors = edge_colors_string,
             alpha = alpha_float)

        plt.title \
            (titles_string_list[index], 
             fontdict = {'fontsize': title_fontsize_float, 
                         'fontstyle': title_fontstyle_string},
             pad = title_pad_float)
    
        plt.xlabel \
            (x_label_string,
             fontdict = {'fontsize': xlabel_fontsize_float, 
                        'fontstyle': xlabel_fontstyle_string},
             labelpad = xlabel_pad_float)

        plt.ylabel \
            (y_label_string,
             fontdict = {'fontsize': ylabel_fontsize_float, 
                         'fontstyle': ylabel_fontstyle_string},
             labelpad = ylabel_pad_float)
    
        plt.xticks \
            (rotation = xtick_label_rotation_float,
             fontsize = xtick_fontsize_float)
        
        plt.yticks \
            (rotation = ytick_label_rotation_float,
             fontsize = ytick_fontsize_float)
        
        plt.grid()


        if degree_integer == 1:

            logx.print_and_log_text(titles_string_list[index] + ':')
                
            display_linear_regression_line \
                (x_series_list[index],
                 y_series_list[index],
                 equation_x_coordinate_float_list[index],
                 equation_y_coordinate_float_list[index])
            
        elif degree_integer > 1:

            logx.print_and_log_text(titles_string_list[index] + ':')
                
            display_polynomial_regression_line \
                (x_series_list[index],
                 y_series_list[index],
                 equation_x_coordinate_float_list[index],
                 equation_y_coordinate_float_list[index],
                 degree_integer)

        plt.tight_layout(pad = tight_layout_pad_float)
    
        plt.suptitle \
            (caption_string, 
             fontsize = suptitle_fontsize_float, 
             y = suptitle_pad_float)

        logx.save_plot_image(caption_string)
        
        plt.show()


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  display_pie_chart_from_series
 #
 #  Function Description:
 #      This function displays a pie chart from a series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  input_series    This parameter is the input series.
 #  string  caption_string  This parameter is the figure title.
 #  list    colors_string_list
 #                          This parameter is the list of pie wedge colors.
 #  tuple   explode_tuple   This parameter is the degree of separation for each pie wedge.
 #  boolean shadow_boolean  This parameter indicates whether the pie chart is shadowed.
 #  float   pct_distance_float
 #                          This parameter is the percent distance between pie wedges.  
 #  float   start_angle_float
 #                          This parameter is the pie chart's start angle.
 #  string  autopct_string
 #                          This parameter is percent format for pie wedges.
 #  float   chart_font_size_float
 #                          This parameter is the chart text font size.       
 #  float   title_fontsize_float
 #                          This parameter is the title font size. 
 #  string  title_fontstyle_string
 #                          This parameter is the title font style.
 #  float   title_pad_float
 #                          This parameter is the title space pad value. 
 #  float   figure_width_float
 #                          This parameter is the figure width. 
 #  float   figure_length_float
 #                          This parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_pie_chart_from_series \
        (input_series,
         caption_string,
         colors_string_list,
         explode_tuple,
         shadow_boolean = True,
         pct_distance_float = 0.75,
         start_angle_float = 45.0,
         autopct_string = '%1.1f%%',
         chart_font_size_float = 14.0,
         title_fontsize_float = 20.0,
         title_fontstyle_string = 'normal',
         title_pad_float = 5.0,
         figure_width_float = 9.708,
         figure_length_float = 6.0):
    
    temp_series = input_series.copy()
        
    temp_series.rename(None, inplace = True)


    plt.figure(figsize = (figure_width_float, figure_length_float))
        
    plt.pie \
        (temp_series,
         labels = temp_series.index, 
         colors = colors_string_list,        
         explode = explode_tuple, 
         shadow = shadow_boolean,
         pctdistance = pct_distance_float,
         startangle = start_angle_float,
         autopct = autopct_string,
         textprops = {'fontsize': chart_font_size_float})
        
    plt.title \
        (caption_string,
         fontdict = {'fontsize': title_fontsize_float, 
                     'fontstyle': title_fontstyle_string},
         pad = title_pad_float)   
        
    logx.save_plot_image(caption_string)
        
    plt.show()


# In[ ]:




