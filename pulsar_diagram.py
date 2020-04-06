import numpy as np, pandas as pd, requests, matplotlib.pyplot as plt, matplotlib as mpl
from bs4 import BeautifulSoup as bs
mpl.rcParams['font.family'] = 'Consolas'
plt.rcParams['font.size'] = 18
plt.rcParams['axes.linewidth'] = 2


page = requests.get("https://www.atnf.csiro.au/people/pulsar/psrcat/proc_form.php?version=1.63&Name=Name&P0=P0&P1=P1&Type=Type&Age=Age&Bsurf=Bsurf&Edot=Edot&startUserDefined=true&c1_val=&c2_val=&c3_val=&c4_val=&sort_attr=jname&sort_order=asc&condition=&pulsar_names=&ephemeris=short&coords_unit=raj%2Fdecj&radius=&coords_1=&coords_2=&style=Long+with+last+digit+error&no_value=*&fsize=3&x_axis=&x_scale=linear&y_axis=&y_scale=linear&state=query&table_bottom.x=35&table_bottom.y=34").content
lines = bs(page).find('pre').get_text().split('\n')

data = [pulsar for pulsar in [line.split() for line in lines] if len(pulsar) > 1]
for pulsar in data[2:]:
    for i in [10,8,7,5,4,2]:
        del pulsar[i]

data[1] = [None,None]+data[1]

pulsar_df = pd.DataFrame(data[2:], columns=data[0]).set_index('#')
pulsar_df.index.name = None
pulsar_df.rename(columns={"PSR": "TYPE"},inplace=True)
pulsar_df.drop(pulsar_df[pulsar_df.P1 == "*"].index, inplace=True)
pulsar_df


for i in pulsar_df.index:
    category = pulsar_df.loc[i,'TYPE']
    if '[' in category:
        pulsar_df.loc[i,'TYPE'] = category[:category.index('[')]
    category = pulsar_df.loc[i,'TYPE']
    if ',' in category:
        pulsar_df.loc[i,'TYPE'] = category[:category.index(',')]

colors = {'*':'cyan', # Unclassified
          'AXP':'darkgreen', # Anomalous X-ray Pulsar or Soft Gamma-ray Repeater with detected pulsations
          'BINARY':'black', # Pulsar has one or more stellar companion(s)
          'HE':'darkmagenta', # Spin-powered pulsar with pulsed emission from radio to infrared or higher frequencies
          'NRAD':'magenta', # Spin-powered pulsar with pulsed emission only at infrared or higher frequencies
          'RADIO':'orange', # Pulsars with pulsed emission in the radio band
          'RRAT':'gold', # Pulsars with intermittently pulsed radio emission
          'XINS':'mediumblue' # Isolated neutron stars with pulsed thermal X-ray emission but no detectable radio emission
         }

pulsar_df.P0 = pulsar_df.P0.apply(pd.to_numeric)
pulsar_df.P1 = pulsar_df.P1.apply(pd.to_numeric)
pulsar_df.BSURF = pulsar_df.BSURF.apply(pd.to_numeric, errors='coerce')
Paxis = np.linspace(1e-3,5e1,len(pulsar_df))


fig, ax = plt.subplots(figsize=(9,9))
ax.set_xlim((1e-3,4e1))
ax.set_ylim((1e-22,1e-8))

ax.xaxis.set_tick_params(which='major', size=10, width=2, direction='in', top='on')
ax.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in', top='on')
ax.yaxis.set_tick_params(which='major', size=10, width=2, direction='in', right='on')
#ax.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in', right='on')

ax.plot(Paxis,Paxis/(2e7*31557600),"k-",alpha=0.5)
ax.text(0.03, 0.32, 'τ = $10^7$ yr', fontsize=16, rotation=17, transform=ax.transAxes)
ax.plot(Paxis,1e12**2/(3.2e19**2*Paxis),"k-",alpha=0.5)
ax.text(0.04, 0.645, 'B = $10^{12}$ Gs', fontsize=16, rotation=-17.5, transform=ax.transAxes)
ax.plot(Paxis,1e33*Paxis**3/(4*np.pi*np.pi*0.4*2.78e33*1000000**2),"k-",alpha=0.5)
ax.text(0.09, 0.015, '$\dot{E} = 10^{33}$ erg/s', fontsize=16, rotation=42, transform=ax.transAxes)

for key, group in pulsar_df.groupby('TYPE'):
    group.plot(ax=ax, kind='scatter', x='P0', y='P1', label=key, color=colors[key]).set(xscale='log', yscale='log')

ax.set_ylabel("$\dot{P}$ (s$\cdot$s$^{-1}$)")
ax.set_xlabel("$P$ (s)")
fig.suptitle("Pulsar data (ATNF Catalogue)")

ax.legend(bbox_to_anchor=(1.25, 1))
plt.show()
fig.savefig("pulsarplot.png",dpi=300,bbox_inches="tight")