import numpy as np
import collections
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import csv
from matplotlib import rc
import pandas as pd
# from load import *

### rcParams are the default parameters for matplotlib
import matplotlib as mpl
rc('mathtext',default='regular')
fonts = 20;
fonts_title = 20
leng_fontsize = 17
mpl.rcParams['font.size'] = fonts
mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['axes.labelsize'] = fonts
mpl.rcParams['xtick.labelsize'] = fonts
mpl.rcParams['ytick.labelsize'] = fonts
mpl.rcParams['axes.linewidth'] = 0
mpl.rcParams['ytick.major.pad']='8'
mpl.rcParams['xtick.major.pad']='10'

xpos = -0.4
ypos = 0.5
lblsize = 20
boldness = 500
ticklblsize = 20
transparency = 1.0


labels = ['Updated model', 'Colman et al.', 'Courtemanche et al.', 'A305T', 'Y155C', 'D469E', 'P488S'];
files = ['None', 'D322H', 'E48G', 'A305T', 'Y155C', 'D469E', 'P488S'];
lnwidth = 0.6*np.array( [3.5, 		3.5 ,     3.5,       3.5,      5,      3.5,          3.5]);
colors = ['r',     'b',    'k',     'r',   '#00008B', 'cyan',  'magenta'];
markers = 7*'v'

fig = plt.figure(figsize=(19*1.3/2.54,19/2/2.54))
num_row = 1;
num_col = 2;
gs1 = gridspec.GridSpec(num_row,num_col
	# width_ratios=[1.15,1],
 #    height_ratios=[1,1]
	);
panel = {};

for i in np.arange(num_row):
	for j in np.arange(num_col):
		panel[i,j] = plt.subplot(gs1[i,j]);
		ax = panel[i,j];
CRN_AP = [];

# CRN_AP.append(np.loadtxt( 'Haibo_CRN_data/AP_files/BCL_1000_Model_0_Region_14_FB_0_0_Mut_' + files[i] + '_AF_0_AP.txt', unpack=True));
# CRN_AP.append(np.loadtxt( 'SR_IKurB_NO_INaB_No.dat', unpack=True));
# CRN_AP.append(np.loadtxt( 'AF_IKurB_NO_INaB_No.dat', unpack=True));

CRN_AP.append( pd.read_csv('SR_IKurB_NO_INaB_No.dat', sep=" ", header = None))
CRN_AP.append( pd.read_csv('Original_Colman_Model.dat', sep=" ", header = None))
CRN_AP.append( pd.read_csv('Original_CRN_Model.dat', sep=" ", header = None))

# print len(CRN_AP[1][:])
a = CRN_AP[0]
print len(a)
print len(a)
# print (a)
# print CRN_AP[0][:]

col = 0;
row = 0;
ax = panel[row,col];
i=1
ax.plot(CRN_AP[i][0]-48970,CRN_AP[i][1], colors[i], linewidth=lnwidth[i], label=labels[i])  #, label = labels[i]
i=2
ax.plot(CRN_AP[i][0]-98970,CRN_AP[i][1], colors[i], linewidth=lnwidth[i], label=labels[i])  #, label = labels[i]
i=0
ax.plot(CRN_AP[i][0]-1.49897e6,CRN_AP[i][1], colors[i], linewidth=lnwidth[i], label=labels[i])  #, label = labels[i]
# CRN_AP[0].plot(ax=ax)
leg = ax.legend(numpoints = 1, loc='best', fancybox=False, prop={'size':leng_fontsize}, labelspacing=0.22,handletextpad=0.5)
leg.draggable(state=True)
leg.draw_frame(False)
leg.get_frame().set_alpha(0.0)
col = 1;
row = 0;
ax = panel[row,col];
i=1
ax.plot(CRN_AP[i][0]-48970,1000*CRN_AP[i][2], colors[i], linewidth=lnwidth[i], label=labels[i])  #, label = labels[i]


i=2
ax.plot(CRN_AP[i][0]-98970,1000*CRN_AP[i][2], colors[i], linewidth=lnwidth[i], label=labels[i])  #, label = labels[i]

i=0
ax.plot(CRN_AP[i][0]-1.49897e6,1000*CRN_AP[i][2], colors[i], linewidth=lnwidth[i], label=labels[i])  #, label = labels[i]






# col = 1;
# row = 0;
# ax = panel[row,col];
# N=2;
# ind = np.arange(N)  # the x locations for the groups
# width = 0.6       # the width of the bars
# Data = (247.82, 157.34)
# ax.bar(ind,Data,width, color=('0.3', 'b'))
# ax.set_ylabel('APD$_{90}$ (ms)')




# col = 1;
# row = 1;
# ax = panel[row,col];
# N=2;
# ind = np.arange(N)  # the x locations for the groups
# width = 0.6       # the width of the bars
# Data = (0.367, 0.202)
# ax.bar(ind,Data,width,color=('0.3', 'b'))
# ax.set_ylabel('$\Delta CaT$ $(\mu M)$')


# CRN_AP[0].plot(ax=ax)
# for i in [0, 1,2,3]:
# 	ax.plot(CRN_AP[i][0]-29000,CRN_AP[i][1], colors[i], linewidth=lnwidth[i], label=labels[i])  #, label = labels[i]
# ax.legend();


# figure_title = 'Gain-of-function' 	#FF6103
# plt.text(0.5, 1.1, figure_title,
#          horizontalalignment='center',
#          fontsize=fonts_title,
#          transform = ax.transAxes)



# col = 1;
# row = 0;
# ax = panel[row,col];
# for i in [0, 4,5,6]:
# 	ax.plot(CRN_AP[i][0],CRN_AP[i][1], colors[i], linewidth=lnwidth[i], label=labels[i])  #, label = labels[i]
# ax.legend();

# leg = ax.legend(numpoints = 1, loc='best', fancybox=False, prop={'size':leng_fontsize}, labelspacing=0.22,handletextpad=0.05)
# leg.draggable(state=True)
# leg.draw_frame(False)
# leg.get_frame().set_alpha(0.0)

# figure_title = 'Loss-of-function' 	#FF6103
# plt.text(0.5, 1.1, figure_title,
#          horizontalalignment='center',
#          fontsize=fonts_title,
#          transform = ax.transAxes)




for i in np.arange(num_col*num_row):
	ax = fig.axes[i]
	ax.autoscale(enable=True, axis='x')  
	ax.autoscale(enable=True, axis='r')  
	ax.spines['right'].set_visible(False)
	#ax.spines['left'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.spines['bottom'].set_visible(True)
	ax.xaxis.set_ticks_position('bottom')
	ax.spines['bottom'].set_linewidth(1.5)
	ax.spines['left'].set_linewidth(1.5)
	ax.spines['right'].set_linewidth(1.5)
	ax.yaxis.tick_left()
	# ax.set_xlim(0,500)
	# # plt.xticks(np.linspace(0,600, 5))
	# ax.set_xticks([0, 250, 500])
	ax.yaxis.set_tick_params(width=1.5)
	ax.xaxis.set_tick_params(width=1.5)
	plt.subplots_adjust(left=0.1, bottom=0.08, right=0.98, top=0.95,
		wspace=0.32, hspace=0.16)
	ax.yaxis.set_label_coords(-0.15, 0.5)

# for i in [0,2]:
# 	ax = fig.axes[i]
# 	ax.set_ylim(-85, 40)
# 	ax.set_yticks(np.linspace(-80,40,3))
# 	ax.set_xlim(-50, 500)

fig.axes[0].set_ylim(-85,40)
fig.axes[0].set_yticks(np.linspace(-80,40,4))
fig.axes[0].set_xlim(0,550)

fig.axes[0].set_ylabel('Voltage (mV)')
fig.axes[0].spines['bottom'].set_linewidth(0)
fig.axes[0].xaxis.set_tick_params(width=0)
fig.axes[0].get_xaxis().set_ticklabels([])
fig.axes[0].plot([100, 200], [-84, -84], lw=3, color='k')

plt.text(0.27, -0.08+0.1+0.01, '100 ms',
         horizontalalignment='center',
         fontsize=fonts_title,
         transform = fig.axes[0].transAxes)

fig.axes[1].set_ylim(0.06,0.8)
fig.axes[1].set_yticks(np.linspace(0.1,0.8,8))
fig.axes[1].set_xlim(0,550)
# fig.axes[1].set_xlim(1.4989e6+50,1.4989e6+500)
fig.axes[1].set_ylabel('CaT ($\mu M$)')
fig.axes[1].spines['bottom'].set_linewidth(0)
fig.axes[1].xaxis.set_tick_params(width=0)
fig.axes[1].get_xaxis().set_ticklabels([])
fig.axes[1].plot([100, 200], [0.065,0.065], lw=3, color='k')
plt.text(0.27, -0.08+0.1+0.01, '100 ms',
         horizontalalignment='center',
         fontsize=fonts_title,
         transform = fig.axes[1].transAxes)


# fig.axes[3].set_xlim(-0.4,2.)
# fig.axes[3].set_ylim(0.1,0.4)
# fig.axes[3].set_yticks([0.1,0.2,0.3,0.4])
# fig.axes[1].set_xlim(-0.4,2.)
# fig.axes[1].set_ylim(100,300)
# fig.axes[1].get_xaxis().set_ticklabels([])
# fig.axes[3].get_xaxis().set_ticklabels([])
# fig.axes[1].xaxis.set_tick_params(width=0)
# fig.axes[3].xaxis.set_tick_params(width=0)
# fig.axes[3].set_xticks(ind+width/2)
# fig.axes[3].set_xticklabels(['SR', 'AF'])
# arrary = [1,3,5]
# for i in arrary:
# 	ax = fig.axes[i]
# 	a=[]
# 	# ax.set_ylabel(a)
# 	ax.axes.get_yaxis().set_ticklabels(a)

# fig.axes[0].set_ylabel('Activation Gate')
# fig.axes[2].set_ylabel('Inactivation Gate')
# fig.axes[4].set_ylabel('Normalised Current\n Density')
# fig.axes[4].yaxis.set_label_coords(-0.08, 0.5)


# fig.axes[4].set_xlabel('Potential (mV)')
# fig.axes[5].set_xlabel('Potential (mV)')
plt.savefig('Figure_APcmp.pdf')
plt.savefig('Figure_APcmp.png', doi=300)
plt.show();