import seaborn as sns
import matplotlib.pyplot as plt


#Kernel Density Plot vs others
sns.set(style="white")
df = sns.load_dataset("iris")

g = sns.PairGrid(df, diag_sharey=False)

g.map_lower(sns.kdeplot,cmap="Blues_d")
g.map_upper(plt.scatter)
g.map_diag(sns.kdeplot,lw=3)

##Kernel Type 2
import numpy as np
sns.set(style="dark")
rs = np.random.RandomState(50)

#Set up matplotlib figure
f, axes = plt.subplots(3,3,figsize = (9,9),sharex=True, sharey=True)

for ax, s in zip(axes.flat, np.linspace(0,3,10)):
    #create a cubehelix colormap to use with kdeplot
    cmap=sns.cubehelix_palette(start=s,light=1,as_cmap=True)
    #Generate and plot a random biv dataset
    x,y = rs.randn(2,50)
    sns.kdeplot(x,y,cmap=cmap,shade=True,cut=5,ax=ax)
    ax.set(xlim=(-3,3),ylim=(-3,3))

f.tight_layout()

##Density Charts
import pandas as pd
sns.set(style="white", rc={"axes.facecolor":(0,0,0,0)})

#create data
rs = np.random.RandomState(1979)
x = rs.randn(500)
g = np.tile(list("ABCDEFGHIJ"), 50)
df = pd.DataFrame(dict(x=x, g=g))
m = df.g.map(ord)
df["x"] += m

# Initialize the FacetGrid object
pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
g = sns.FacetGrid(df, row="g", hue="g", aspect=15, size=.5, palette=pal)

# Draw the densities in a few steps
g.map(sns.kdeplot, "x", clip_on=False, shade=True, alpha=1, lw=1.5, bw=.2)
g.map(sns.kdeplot, "x", clip_on=False, color="w", lw=2, bw=.2)
g.map(plt.axhline, y=0, lw=2, clip_on=False)

# Define and use a simple function to label the plot in axes coordinates
def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .2, label, fontweight="bold", color=color,
            ha="left", va="center", transform=ax.transAxes)

g.map(label, "x")

# Set the subplots to overlap
g.fig.subplots_adjust(hspace=-.25)

# Remove axes details that don't play will with overlap
g.set_titles("")
g.set(yticks=[])
g.despine(bottom=True, left=True)

#Plot Microsoft ticker chart
import math
import bokeh
bokeh.sampledata.download()
from math import pi
from bokeh.plotting import figure,show,output_file
from bokeh.sampledata.stocks import MSFT

df = pd.DataFrame(MSFT)[:50]

df["date"] = pd.to_datetime(df["date"])

inc = df.close > df.open
dec = df.open > df.close
w = 12*60*60*1000

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

p = figure(x_axis_type="datetime",tools=TOOLS,plot_width=1000,title = "MSFT Candlestick")
p.xaxis.major_label_orientation = pi/4
p.grid.grid_line_alpha=0.3

p.segment(df.date,df.high,df.date,df.low,color="black")
p.vbar(df.date[inc],w,df.open[inc],df.close[inc],fill_color="#D5E1DD",line_color="black")
p.vbar(df.date[dec],w,df.open[dec],df.close[dec],fill_color="#F2583E",line_color="black")

output_file("candlestick.html",title="candlestick.py example")

show(p)


def datetime(x):
    return np.array(x,dtype=np.datetime64)

