
# coding: utf-8

# In[1]:


import pandas as pd
import csv


# In[2]:



pollution = 'pollution_us_2000_2016.csv'
pollution_data = pd.read_csv(pollution) 
print(pollution_data.columns)


# In[3]:


columns_of_interest=['State','City','O3 Mean','SO2 Mean','CO Mean','Date Local']
state_mean=pollution_data[columns_of_interest]


# In[4]:


state_mean.head(2)


# In[5]:



al_stat=state_mean.loc[pollution_data['State'] == "Alabama"]
ak_stat=state_mean.loc[pollution_data['State'] == "Alaska"]
az_stat=state_mean.loc[pollution_data['State'] == "Arizona"]
ar_stat=state_mean.loc[pollution_data['State'] == "Arkansas"]
ca_stat=state_mean.loc[pollution_data['State'] == "California"]
co_stat=state_mean.loc[pollution_data['State'] == "Colorado"]
ct_stat=state_mean.loc[pollution_data['State'] == "Connecticut"]
de_stat=state_mean.loc[pollution_data['State'] == "Delaware"]
fl_stat=state_mean.loc[pollution_data['State'] == "Florida"]
ga_stat=state_mean.loc[pollution_data['State'] == "Georgia"]
hi_stat=state_mean.loc[pollution_data['State'] == "Hawaii"]
id_stat=state_mean.loc[pollution_data['State'] == "Idaho"]
ill_stat=state_mean.loc[pollution_data['State'] == "Illinois"]
in_stat=state_mean.loc[pollution_data['State'] == "Indiana"]
ia_stat=state_mean.loc[pollution_data['State'] == "Iowa"]
ks_stat=state_mean.loc[pollution_data['State'] == "Kansas"]
kt_stat=state_mean.loc[pollution_data['State'] == "Kentucky"]
la_stat=state_mean.loc[pollution_data['State'] == "Loisiana"]
me_stat=state_mean.loc[pollution_data['State'] == "Maine"]
md_stat=state_mean.loc[pollution_data['State'] == "Maryland"]
ma_stat=state_mean.loc[pollution_data['State'] == "Massachusetts"]
mi_stat=state_mean.loc[pollution_data['State'] == "Michigan"]
mn_stat=state_mean.loc[pollution_data['State'] == "Minnesota"]
ms_stat=state_mean.loc[pollution_data['State'] == "Mississippi"]
mo_stat=state_mean.loc[pollution_data['State'] == "Missouri"]
mt_stat=state_mean.loc[pollution_data['State'] == "Montana"]
nb_stat=state_mean.loc[pollution_data['State'] == "Nebraska"]
nv_stat=state_mean.loc[pollution_data['State'] == "Nevada"]
nh_stat=state_mean.loc[pollution_data['State'] == "New Hampshire"]
nj_stat=state_mean.loc[pollution_data['State'] == "New Jersey"]
nm_stat=state_mean.loc[pollution_data['State'] == "New Mexico"]
ny_stat=state_mean.loc[pollution_data['State'] == "New York"]
nc_stat=state_mean.loc[pollution_data['State'] == "North Carolina"]
nd_stat=state_mean.loc[pollution_data['State'] == "North Dakota"]
oh_stat=state_mean.loc[pollution_data['State'] == "Ohio"]
or_stat=state_mean.loc[pollution_data['State'] == "Oregon"]
ok_stat=state_mean.loc[pollution_data['State'] == "Oklahoma"]
pa_stat=state_mean.loc[pollution_data['State'] == "Pennsylvania"]
ri_stat=state_mean.loc[pollution_data['State'] == "Rhode Island"]
sc_stat=state_mean.loc[pollution_data['State'] == "South Carolina"]
sd_stat=state_mean.loc[pollution_data['State'] == "South Dakota"]
tn_stat=state_mean.loc[pollution_data['State'] == "Tennessee"]
tx_stat=state_mean.loc[pollution_data['State'] == "Texas"]
ut_stat=state_mean.loc[pollution_data['State'] == "Utah"]
vt_stat=state_mean.loc[pollution_data['State'] == "Vermont"]
va_stat=state_mean.loc[pollution_data['State'] == "Virginia"]
wa_stat=state_mean.loc[pollution_data['State'] == "Washington"]
wv_stat=state_mean.loc[pollution_data['State'] == "West Virginia"]
wi_stat=state_mean.loc[pollution_data['State'] == "Wisconsin"]
wy_stat=state_mean.loc[pollution_data['State'] == "Wyoming"]            


# In[6]:


state_mean['Date Local'] = pd.to_datetime(state_mean['Date Local']) 


# In[129]:


n="2015-01-01"
m='2015-12-31'
mask1 =(al_stat['Date Local']> n) & (al_stat['Date Local'] <= m)
mask2=(ak_stat['Date Local'] > n) & (ak_stat['Date Local'] <= m)
mask3=(az_stat['Date Local'] > n) & (az_stat['Date Local'] <= m)
mask4=(ar_stat['Date Local'] > n) & (ar_stat['Date Local'] <= m)
mask5=(ca_stat['Date Local'] > n) & (ca_stat['Date Local'] <= m)
mask6=(co_stat['Date Local'] > n) & (co_stat['Date Local'] <= m)
mask7=(ct_stat['Date Local'] > n) & (ct_stat['Date Local'] <= m)
mask8=(de_stat['Date Local'] > n) & (de_stat['Date Local'] <= m)
mask9=(fl_stat['Date Local'] > n) & (fl_stat['Date Local'] <= m)
mask10=(ga_stat['Date Local'] > n) & (ga_stat['Date Local'] <=m)
mask11=(hi_stat['Date Local'] > n) & (hi_stat['Date Local'] <=m)
mask12=(ny_stat['Date Local'] > n) & (nm_stat['Date Local'] <= m)
mask13=(ill_stat['Date Local'] > n) & (ill_stat['Date Local'] <= m)
mask14=(id_stat['Date Local'] > n) & (id_stat['Date Local'] <= m)
mask15=(in_stat['Date Local'] > n) & (in_stat['Date Local'] <= m)
mask16=(ia_stat['Date Local'] > n) & (ia_stat['Date Local'] <= m)
mask17=(ks_stat['Date Local'] > n) & (ks_stat['Date Local'] <= m)
mask18=(kt_stat['Date Local'] > n) & (kt_stat['Date Local'] <= m)
mask19=(la_stat['Date Local'] > n) & (la_stat['Date Local'] <= m)
mask21=(ma_stat['Date Local'] > n) & (ma_stat['Date Local'] <= m)
mask22=(md_stat['Date Local'] > n) & (md_stat['Date Local'] <= m)
mask23=(me_stat['Date Local'] > n) & (me_stat['Date Local'] <= m)
mask24=(mn_stat['Date Local'] > n) & (mn_stat['Date Local'] <= m)
mask25=(ms_stat['Date Local'] > n) & (ms_stat['Date Local'] <= m)
mask26=(mo_stat['Date Local'] > n) & (mo_stat['Date Local'] <= m)
mask27=(mt_stat['Date Local'] > n) & (mt_stat['Date Local'] <= m)
mask28=(mi_stat['Date Local'] > n) & (mi_stat['Date Local'] <= m)
mask29=(nb_stat['Date Local'] >n) & (nb_stat['Date Local'] <= m)
mask30=(nv_stat['Date Local'] > n) & (nv_stat['Date Local'] <=m)
mask31=(nh_stat['Date Local'] > n) & (nh_stat['Date Local'] <= m)
mask32=(nj_stat['Date Local'] > n) & (nj_stat['Date Local'] <= m)
mask33=(nm_stat['Date Local'] > n) & (nm_stat['Date Local'] <= m)
mask34=(nd_stat['Date Local'] > n) & (nd_stat['Date Local'] <= m)
mask35=(nc_stat['Date Local'] > n) & (nc_stat['Date Local'] <= m)
mask36=(oh_stat['Date Local'] > n) & (oh_stat['Date Local'] <= m)
mask37=(or_stat['Date Local'] > n) & (or_stat['Date Local'] <= m)
mask38=(ok_stat['Date Local'] > n) & (ok_stat['Date Local'] <= m)
mask39=(pa_stat['Date Local'] > n) & (pa_stat['Date Local'] <= m)
mask40=(ri_stat['Date Local'] > n) & (ri_stat['Date Local'] <= m)
mask41=(sc_stat['Date Local'] > n) & (sc_stat['Date Local'] <= m)
mask42=(sd_stat['Date Local'] > n) & (sd_stat['Date Local'] <= m)
mask43=(tn_stat['Date Local'] > n) & (tn_stat['Date Local'] <= m)
mask44=(tx_stat['Date Local'] > n) & (tx_stat['Date Local'] <= m)
mask45=(ut_stat['Date Local'] > n) & (ut_stat['Date Local'] <= m)
mask46=(vt_stat['Date Local'] > n) & (vt_stat['Date Local'] <= m)
mask47=(va_stat['Date Local'] > n) & (va_stat['Date Local'] <= m)
mask48=(wa_stat['Date Local'] > n) & (wa_stat['Date Local'] <= m)
mask49=(wv_stat['Date Local'] > n) & (wv_stat['Date Local'] <= m)
mask50=(wi_stat['Date Local'] > n) & (wi_stat['Date Local'] <= m)
mask51=(wy_stat['Date Local'] > n) & (wy_stat['Date Local'] <= m)
#---------------------------------------------------------------------------------------#

ozal2000=al_stat.loc[mask1]
ozak2000=ak_stat.loc[mask2]
ozaz2000=az_stat.loc[mask3]
ozar2000=ar_stat.loc[mask4]
ozca2000=ca_stat.loc[mask5]
ozco2000=co_stat.loc[mask6]
ozct2000=ct_stat.loc[mask7]
ozde2000=de_stat.loc[mask8]
ozfl2000=fl_stat.loc[mask9]
ozga2000=ga_stat.loc[mask10]
ozhi2000=hi_stat.loc[mask11]
ozid2000=id_stat.loc[mask14]
ozill2000=ill_stat.loc[mask13]
ozin2000=in_stat.loc[mask15]
ozia2000=ia_stat.loc[mask16]
ozks2000=ks_stat.loc[mask17]
ozkt2000=kt_stat.loc[mask18]
ozla2000=la_stat.loc[mask19]
ozma2000=ma_stat.loc[mask21]
ozme2000=me_stat.loc[mask23]
ozms2000=ms_stat.loc[mask25]
ozmi2000=mi_stat.loc[mask28]
ozmt2000=mt_stat.loc[mask27]
ozmo2000=mo_stat.loc[mask26]
oznb2000=nb_stat.loc[mask29]
oznv2000=nv_stat.loc[mask30]
oznh2000=nh_stat.loc[mask31]
oznj2000=nj_stat.loc[mask32]
oznm2000=nm_stat.loc[mask33]
ozny2000=ny_stat.loc[mask12]
oznc2000=nc_stat.loc[mask35]
oznd2000=nd_stat.loc[mask34]
ozoh2000=oh_stat.loc[mask36]
ozok2000=ok_stat.loc[mask38]
ozpa2000=pa_stat.loc[mask39]
ozri2000=ri_stat.loc[mask40]
ozsc2000=sc_stat.loc[mask41]
ozsd2000=sd_stat.loc[mask42]
oztn2000=tn_stat.loc[mask43]
oztx2000=tx_stat.loc[mask44]
ozut2000=ut_stat.loc[mask45]
ozvt2000=vt_stat.loc[mask46]
ozva2000=va_stat.loc[mask47]
ozwa2000=wa_stat.loc[mask48]
ozwv2000=wv_stat.loc[mask49]
ozwi2000=wi_stat.loc[mask50]
ozwy2000=wy_stat.loc[mask51]
ozmn2000=mn_stat.loc[mask24]
ozmd2000=md_stat.loc[mask22]
ozor2000=or_stat.loc[mask37]


# In[130]:


highest=ozca2000.loc[oznj2000['O3 Mean'].idxmax()]
highest


# In[131]:


#oznj2000[oznj2000["City"]=="Newark"]


# In[122]:


lowest=nj_stat.loc[nj_stat['O3 Mean'].idxmin()]
lowest


# In[123]:


val=ozal2000["O3 Mean"].mean()
vak=ozak2000["O3 Mean"].mean()
var=ozar2000["O3 Mean"].mean()
vaz=ozaz2000["O3 Mean"].mean()
vca=ozca2000["O3 Mean"].mean()
vco=ozco2000["O3 Mean"].mean()
vde=ozde2000["O3 Mean"].mean()
vfl=ozfl2000["O3 Mean"].mean()
vga=ozga2000["O3 Mean"].mean()
vhi=ozhi2000["O3 Mean"].mean()
vks=ozks2000["O3 Mean"].mean()
vkt=ozkt2000["O3 Mean"].mean()
vla=ozla2000["O3 Mean"].mean()
vma=ozma2000["O3 Mean"].mean()
vme=ozme2000["O3 Mean"].mean()
vms=ozms2000["O3 Mean"].mean()
vmo=ozmo2000["O3 Mean"].mean()
vmt=ozmt2000["O3 Mean"].mean()
vmn=ozmn2000["O3 Mean"].mean()
vmi=ozmi2000["O3 Mean"].mean()
vmd=ozmd2000["O3 Mean"].mean()
vnb=oznb2000["O3 Mean"].mean()
vnc=oznc2000["O3 Mean"].mean()
vnj=oznj2000["O3 Mean"].mean()
vny=ozny2000["O3 Mean"].mean()
vnh=oznh2000["O3 Mean"].mean()
vnd=oznd2000["O3 Mean"].mean()
vnm=oznm2000["O3 Mean"].mean()
vor=ozor2000["O3 Mean"].mean()
voh=ozoh2000["O3 Mean"].mean()
vok=ozok2000["O3 Mean"].mean()
vpa=ozpa2000["O3 Mean"].mean()
vri=ozri2000["O3 Mean"].mean()
vsc=ozsc2000["O3 Mean"].mean()
vsd=ozsd2000["O3 Mean"].mean()
vtn=oztx2000["O3 Mean"].mean()
vut=ozut2000["O3 Mean"].mean()
vvt=ozvt2000["O3 Mean"].mean()
vva=ozva2000["O3 Mean"].mean()
vwa=ozwa2000["O3 Mean"].mean()
vwv=ozak2000["O3 Mean"].mean()
vwi=ozak2000["O3 Mean"].mean()
vwy=ozak2000["O3 Mean"].mean()
vid=ozid2000["O3 Mean"].mean()
vill=ozill2000["O3 Mean"].mean()
vin=ozin2000["O3 Mean"].mean()
via=ozia2000["O3 Mean"].mean()
vct=ozct2000["O3 Mean"].mean()
vnv=oznv2000["O3 Mean"].mean()
vtx=oztx2000["O3 Mean"].mean()
vtn=oztn2000["O3 Mean"].mean()


# In[124]:


vnj


# In[110]:


with open('oz2016.csv','w',newline='') as fp:
    a=csv.writer(fp,delimiter=',')
    data=[['state','value'],
         ['Alabama',val],["Alaska",vak],
         ["Arkansas",vak],["Arizona",vaz],
        ["California",vca],["Colorado",vco],
         ["Connecticut",vct],["Delaware",vde],
         ["District of Columbia",0],["Florida",vfl],["Georgia",vga],
         ["Hawaii",vhi],["Iowa",via],
         ["Idaho",vid],["Illinois",vill],
         ["Indiana",vin],["Kansas",vks],["Kentucky",vkt],
         ["Louisiana",vla],["Maine",vme],
         ["Maryland",vmd],["Massachusetts",vma],
         ["Michigan",vmi],["Minnesota",vmn],
         ["Missouri",vmo],["Mississippi",vms],
         ["Montana",vmo],["North Carolina",vnc],["North Dakota",vnd],
         ["Nebraska",vnb],["New Hampshire",vnh],["New Jersey",vnj],
         ["New Mexico",vnm],["Nevada",vnv],["New York",vny],
         ["Ohio",voh],["Oklahoma",vok],["Oregon",vor],
         ["Pennsylvania",vpa],["Rhode Island",vri],
         ["South Carolina",vsc],["South Dakota",vsd],
         ["Tennessee",vtn],["Texas",vtx],["Utah",vut],
         ["Virginia",vva],["Vermont",vvt],["Washington",vwa],
         ["Wisconsin",vwi],["West Virginia",vwv],["Wyoming",vwy]]
    
    a.writerows(data)


# In[136]:


o="O3 Mean"
c="NO2 Mean"
val=ozal2000[c].mean()
vak=ozak2000[c].mean()
var=ozar2000[c].mean()
vaz=ozaz2000[c].mean()
vca=ozca2000[c].mean()
vco=ozco2000[c].mean()
vde=ozde2000[c].mean()
vfl=ozfl2000[c].mean()
vga=ozga2000[c].mean()
vhi=ozhi2000[c].mean()
vks=ozks2000[c].mean()
vkt=ozkt2000[c].mean()
vla=ozla2000[c].mean()
vma=ozma2000[c].mean()
vme=ozme2000[c].mean()
vms=ozms2000[c].mean()
vmo=ozmo2000[c].mean()
vmt=ozmt2000[c].mean()
vmn=ozmn2000[c].mean()
vmi=ozmi2000[c].mean()
vmd=ozmd2000[c].mean()
vnb=oznb2000[c].mean()
vnc=oznc2000[c].mean()
vnj=oznj2000[c].mean()
vny=ozny2000[c].mean()
vnh=oznh2000[c].mean()
vnd=oznd2000[c].mean()
vnm=oznm2000[c].mean()
vor=ozor2000[c].mean()
voh=ozoh2000[c].mean()
vok=ozok2000[c].mean()
vpa=ozpa2000[c].mean()
vri=ozri2000[c].mean()
vsc=ozsc2000[c].mean()
vsd=ozsd2000[c].mean()
vtn=oztx2000[c].mean()
vut=ozut2000[c].mean()
vvt=ozvt2000[c].mean()
vva=ozva2000[c].mean()
vwa=ozwa2000[c].mean()
vwv=ozak2000[c].mean()
vwi=ozak2000[c].mean()
vwy=ozak2000[c].mean()
vid=ozid2000[c].mean()
vill=ozill2000[c].mean()
vin=ozin2000[c].mean()
via=ozia2000[c].mean()
vct=ozct2000[c].mean()
vnv=oznv2000[c].mean()
vtx=oztx2000[c].mean()
vtn=oztn2000[c].mean()

vid


# In[134]:


with open('no22015.csv','w',newline='') as fp:
    a=csv.writer(fp,delimiter=',')
    data=[['state','value'],
         ['Alabama',val],["Alaska",vak],
         ["Arkansas",vak],["Arizona",vaz],
        ["California",vca],["Colorado",vco],
         ["Connecticut",vct],["Delaware",vde],
         ["District of Columbia",0],["Florida",vfl],["Georgia",vga],
         ["Hawaii",vhi],["Iowa",via],
         ["Idaho",vid],["Illinois",vill],
         ["Indiana",vin],["Kansas",vks],["Kentucky",vkt],
         ["Louisiana",vla],["Maine",vme],
         ["Maryland",vmd],["Massachusetts",vma],
         ["Michigan",vmi],["Minnesota",vmn],
         ["Missouri",vmo],["Mississippi",vms],
         ["Montana",vmo],["North Carolina",vnc],["North Dakota",vnd],
         ["Nebraska",vnb],["New Hampshire",vnh],["New Jersey",vnj],
         ["New Mexico",vnm],["Nevada",vnv],["New York",vny],
         ["Ohio",voh],["Oklahoma",vok],["Oregon",vor],
         ["Pennsylvania",vpa],["Rhode Island",vri],
         ["South Carolina",vsc],["South Dakota",vsd],
         ["Tennessee",vtn],["Texas",vtx],["Utah",vut],
         ["Virginia",vva],["Vermont",vvt],["Washington",vwa],
         ["Wisconsin",vwi],["West Virginia",vwv],["Wyoming",vwy]]
    
    a.writerows(data)


# In[138]:


vwa

