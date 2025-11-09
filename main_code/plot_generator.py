import matplotlib.pyplot as plt
import seaborn as sns
from main_code.data_loader import loaded_data
import pandas as pd


loaded_data["day_id"] = pd.to_datetime(loaded_data["day_id"])
loaded_data["month"] = loaded_data["day_id"].dt.month_name()
loaded_data["day"] = loaded_data["day_id"].dt.day

default_format = {
    "fontname": "Arial",
    "color": "darkblue",
    "title_fontsize": 12,
    "fontsize": 8,
    "title_fontweight": "bold",
    "pad": 12,
    "xrotation": 45,
    "xha": "right"
}

def format_plot(title, xlabel, ylabel, format):
    plt.title(title, fontsize=format["title_fontsize"], fontname=format["fontname"], fontweight=format["title_fontweight"], pad=format["pad"])
    plt.xlabel(xlabel, fontsize=format["fontsize"], fontname=format["fontname"], color=format["color"])
    plt.ylabel(ylabel, fontsize=format["fontsize"], fontname=format["fontname"], color=format["color"])
    plt.xticks(fontsize=format["fontsize"], fontname=format["fontname"], color=format["color"], rotation=format["xrotation"], ha=format["xha"])
    plt.yticks(fontsize=format["fontsize"], fontname=format["fontname"], color=format["color"])
    plt.tight_layout()

def save_plot(name):
    plt.savefig(f"../plots/{name}.png", dpi=300, bbox_inches="tight")
    plt.close()

def filter_data_by_x(data, xdata, xfilter):
    if xfilter is not None:
        return data[data[xdata].isin(xfilter)]
    else:
        return data


def bar_plot(title, xlabel, ylabel, xdata, ydata, xfilter, xfilter_data, type, format=default_format, data=loaded_data):
    filtered_data = filter_data_by_x(data, xfilter_data, xfilter)
    if type is not None:
        match type:
            case "mean": filtered_data = filtered_data.groupby(xdata)[ydata].mean().reset_index()
            case "sum": filtered_data = filtered_data.groupby(xdata)[ydata].sum().reset_index()
            case "median": filtered_data = filtered_data.groupby(xdata)[ydata].median().reset_index()
            case "std": filtered_data = filtered_data.groupby(xdata)[ydata].std().reset_index()
            case _: filtered_data = filtered_data.groupby(xdata)[ydata].count().reset_index()
    sns.barplot(filtered_data, x=xdata, y=ydata)
    format_plot(title, xlabel, ylabel, format)
    plt.show()

def hist_plot(title, xlabel, ylabel, xdata, ydata, xfilter, xfilter_data, hue=None, hue_title=None, discrete=True, format=default_format, data=loaded_data):
    filtered_data = filter_data_by_x(data, xfilter_data, xfilter)
    if hue is not None:
        ax = sns.histplot(data=filtered_data, x=xdata, y=ydata, discrete=discrete, hue=hue, palette="tab10", multiple="stack")
        ax.get_legend().set_title(hue_title)
    else:
        sns.histplot(data=filtered_data, x=xdata, y=ydata, discrete=discrete, hue=hue)
    format_plot(title, xlabel, ylabel, format)
    plt.show()

def line_plot(title, xlabel, ylabel, xdata, ydata, xfilter, xfilter_data, hue=None, hue_title=None, format=default_format, data=loaded_data):
    filtered_data = filter_data_by_x(data, xfilter_data, xfilter)
    if hue is not None:
        ax = sns.lineplot(data=filtered_data, x=xdata, y=ydata, hue=hue, errorbar=None)
        ax.get_legend().set_title(hue_title)
    else:
        sns.lineplot(data=filtered_data, x=xdata, y=ydata, hue=hue, errorbar=None)
    format_plot(title, xlabel, ylabel, format)
    plt.show()

def linear_regression_plot(title, xlabel, ylabel, xdata, ydata, xfilter, xfilter_data, format=default_format, data=loaded_data):
    filtered_data = filter_data_by_x(data, xfilter_data, xfilter)
    sns.lmplot(data=filtered_data, x=xdata, y=ydata, scatter=True,  line_kws={"color": "orange"}, ci=None)
    format_plot(title, xlabel, ylabel, format)
    plt.show()