# FATES Parameter
# Xinyuan Wei
# 2020/10/23

import netCDF4
import shutil

para_file='fates_LUQ_params.nc'

# Read the template.
para_template='fates_params_cp_template.nc'
shutil.copyfile(para_template, para_file)
para=netCDF4.Dataset(para_file,mode='r+',format='netCDF3')
para_var=para.variables
para_list=list(para_var)
#print(para_list)
#print(para.file_format)
print('FATES Parameters:')

#######################################
  ### Carbon only? Coupled? ###
#######################################
#para_var['fates_prescribed_nuptake'][:]=[1]
#para_var['fates_prescribed_puptake'][:]=[1]
#print('Prescribed N:',para_var['fates_prescribed_nuptake'][:])
#print('Prescribed P:',para_var['fates_prescribed_puptake'][:])
print('')

#######################################
  ### Allometric Parameters 1 ###
#######################################
# DBH to AGB.
para_var['fates_allom_amode'][:]=[3.0]     #3.0           #2
para_var['fates_allom_agb1'][:]=[0.0673]   #0.0673        #11.0122
para_var['fates_allom_agb2'][:]=[0.976]    #0.976         #2.475
para_var['fates_allom_agb3'][:]=['NaN']
para_var['fates_allom_agb4'][:]=['NaN']

# DBH to leaf biomass.
para_var['fates_allom_lmode'][:]=[3.0]         #3             #2.0
para_var['fates_allom_d2bl1'][:]=[0.1266844]   #0.1266844     #0.55061
para_var['fates_allom_d2bl2'][:]=[1.281329]    #1.281329      #2.475
para_var['fates_allom_d2bl3'][:]=['Nan']

# DBH to height.
para_var['fates_allom_hmode'][:]=[5.0]
para_var['fates_allom_d2h1'][:]=[57.6]
para_var['fates_allom_d2h2'][:]=[0.74]
para_var['fates_allom_d2h3'][:]=[21.6]

# DBh to sapwood biomass.
para_var['fates_allom_la_per_sa_int'][:]=[4.0]     #0.027
para_var['fates_allom_la_per_sa_slp'][:]=[0]       #0.026

# DBh to canopy.
para_var['fates_allom_d2ca_coefficient_max'][:]=[0.768654]     #0.768654 1.0
para_var['fates_allom_d2ca_coefficient_min'][:]=[0.768654]    #0.768654  0.21

# Leaf to fine root.
para_var['fates_allom_fmode'][:]=[2.0]              # 1: trim, 2: untrim
para_var['fates_allom_l2fr_min'][:]=[0.186]             #0.386, 0.486
para_var['fates_allom_l2fr_max'][:]=[0.886]             #0.386, 0.486

print('Above ground woody biomass allometry:',
      para_var['fates_allom_agb1'][:],
      para_var['fates_allom_agb2'][:],
      para_var['fates_allom_agb3'][:],
      para_var['fates_allom_agb4'][:])

print('DBH to leaf biomass allometry:',
      para_var['fates_allom_d2bl1'][:],
      para_var['fates_allom_d2bl2'][:],
      para_var['fates_allom_d2bl3'][:])

print('Diameter to height allometry:',
      para_var['fates_allom_d2h1'][:],
      para_var['fates_allom_d2h2'][:],
      para_var['fates_allom_d2h3'][:])

print('Leaf area/Sapwood area int and slp:',
      para_var['fates_allom_la_per_sa_int'][:],
      para_var['fates_allom_la_per_sa_slp'][:])

print('DBH to canopy:',
      para_var['fates_allom_d2ca_coefficient_max'][:],
      para_var['fates_allom_d2ca_coefficient_min'][:])

print('Fine root C per leaf C:',
      para_var['fates_allom_l2fr_max'][:],
      para_var['fates_allom_l2fr_min'][:])
print('')

#######################################
  ### Allometric Parameters 2 ###
#######################################
para_var['fates_allom_agb_frac'][:]=[0.75]

para_var['fates_allom_sai_scaler'][:]=[0.2062]

para_var['fates_alloc_storage_cushion'][:]=[3.0]

para_var['fates_allom_dbh_maxheight'][:]=[160]

para_var['fates_allom_frbstor_repro'][:]=[0.0]

print('Above ground woody biomass ratio (%): ',
      para_var['fates_allom_agb_frac'][:])

print('Allometric ratio of SAI per LAI:',
      para_var['fates_allom_sai_scaler'][:])

print('Storage C pool relative to maximum size leaf C pool:',
      para_var['fates_alloc_storage_cushion'][:])

print('The maximum height (diameters may increase beyond this):',
      para_var['fates_allom_dbh_maxheight'][:])

print('Fraction of storage carbon to seed:',
      para_var['fates_allom_frbstor_repro'][:])

print('')

#######################################
  ### NP Stoichiometry Parameters ###
#######################################

para_var['fates_prt_nitr_stoich_p1'][:]=[[0.0466],[0.01435],[0.004243],[0.002829]]
para_var['fates_prt_nitr_stoich_p2'][:]=[[0.0466],[0.01435],[0.004243],[0.002829]]
para_var['fates_prt_phos_stoich_p1'][:]=[[0.0081],[0.000599],[0.000144],[0.000096]]
para_var['fates_prt_phos_stoich_p2'][:]=[[0.0081],[0.000599],[0.000144],[0.000096]]

para_var['fates_nitr_store_ratio'][:]=[3.0]
para_var['fates_phos_store_ratio'][:]=[3.0]

print('N Stoichiometry:',para_var['fates_prt_nitr_stoich_p1'][:].tolist())
print('P Stoichiometry:',para_var['fates_prt_phos_stoich_p1'][:].tolist())

print('Ratio of storable N to fine root N',
      para_var['fates_nitr_store_ratio'][:])
print('Ratio of storable P to fine root P',
      para_var['fates_phos_store_ratio'][:])
print('')

#######################################
  ### Cohort Boundary ###
#######################################
para_var['fates_cohort_age_fusion_tol'][:]=[0.08]
para_var['fates_cohort_size_fusion_tol'][:]=[0.08]
para_var['fates_history_sizeclass_bin_edges'][:]=[[0],[1],[3],[5],[10],[20],
                                                  [30],[40],[60],[80],[100],
                                                  [150],[250]]
para_var['fates_patch_fusion_tol'][:]=[0.05]

print('Cohort age:',para_var['fates_cohort_age_fusion_tol'][:])
print('Cohort size:',para_var['fates_cohort_size_fusion_tol'][:])
print('Cohort boundary:',para_var['fates_history_sizeclass_bin_edges'][:])
print('Patch:',para_var['fates_patch_fusion_tol'][:])
print('')

#######################################
  ### Mortality ###
#######################################                     
#para_var['fates_mort_r_age_senescence'][:]=[0.004]              #Nan
#para_var['fates_mort_r_size_senescence'][:]=[0.00991]           #Nan

para_var['fates_mort_bmort'][:]=[0.033]                          #0.014, 0.033
para_var['fates_mort_scalar_cstarvation'][:]=[0.03]              #0.02955

para_var['fates_mort_understorey_death'][:]=[0.56]                #0.56
para_var['fates_prescribed_mortality_canopy'][:]=[0.02]          #0.0194, 0.02
para_var['fates_prescribed_mortality_understory'][:]=[0.02]       #0.025, 0.02

print('Background mortality rate:',
      para_var['fates_mort_bmort'][:])

print('Fraction of understory plants impacted by overstorey treefall:',
      para_var['fates_mort_understorey_death'][:])

print('Caron starvation mortality:',
      para_var['fates_mort_scalar_cstarvation'][:])

print('Prescribed canopy mortality:',
      para_var['fates_prescribed_mortality_canopy'][:])

print('Prescribed understory mortality:',
      para_var['fates_prescribed_mortality_understory'][:])

print('')

#######################################
  ### Maintenance Respiration ###
#######################################                     
para_var['fates_q10_mr'][:]=[1.7]
para_var['fates_base_mr_20'][:]=[0.00000116]
para_var['fates_grperc'][:]=[0.11]

print('Maintenance respiration Q10: ',
      para_var['fates_q10_mr'][:])

print('Maintenance respiration rate (C/N): ',
      para_var['fates_base_mr_20'][:])

print('Growth respiration factor:',
      para_var['fates_grperc'][:])

print('')

#######################################
  ### Wood ###
#######################################  
para_var['fates_wood_density'][:]=[0.75]
para_var['fates_branch_turnover'][:]=[200]  #200

print('Wood density: ',para_var['fates_wood_density'][:])
print('Branch  longevity:',para_var['fates_branch_turnover'][:])

#######################################
  ### Leaf ###
#######################################  
para_var['fates_leaf_long'][:]=[1.2]       #1.4
para_var['fates_leaf_diameter'][:]=[0.04]   #0.04
para_var['fates_leaf_slamax'][:]=[0.039916]
para_var['fates_leaf_slatop'][:]=[0.01995]
para_var['fates_leaf_vcmax25top'][:]=[49.99]

para_var['fates_trim_inc'][:]=[0.03]
para_var['fates_trim_limit'][:]=[0.3]

para_var['fates_lf_fcel'][:]=[0.5]
para_var['fates_lf_flab'][:]=[0.25]
para_var['fates_lf_flig'][:]=[0.25]

print('Leaf Longevity: ',para_var['fates_leaf_long'][:])
print('Characteristic leaf dimension:',para_var['fates_leaf_diameter'][:])
print('Maximum specific leaf area:',para_var['fates_leaf_slamax'][:])
print('Specific leaf area at top of canopy projected area basis:',
      para_var['fates_leaf_slatop'][:])
print('Maximum carboxylation rate of Rub. at 25C canopy top:',
      para_var['fates_leaf_vcmax25top'][:])


print('Leaf litter cellulose fraction:',para_var['fates_lf_fcel'][:])
print('Leaf litter labile fraction:',para_var['fates_lf_flab'][:])
print('Leaf litter lignin fraction:',para_var['fates_lf_flig'][:])
print('')

#######################################
  ### Root ###
#######################################  
para_var['fates_root_long'][:]=[1.0] #1.0

para_var['fates_fnrt_prof_mode'][:]=[1] # 3, 7, 1
para_var['fates_fnrt_prof_a'][:]=[0.962]
para_var['fates_fnrt_prof_b'][:]=['NaN']

para_var['fates_fr_fcel'][:]=[0.5]
para_var['fates_fr_flab'][:]=[0.25]
para_var['fates_fr_flig'][:]=[0.25]

print('Root Longevity',para_var['fates_root_long'][:])

print('Fine root profile model',para_var['fates_fnrt_prof_mode'][:])
print('Fine root profile function parameter a',para_var['fates_fnrt_prof_a'][:])
print('Fine root profile function parameter b',para_var['fates_fnrt_prof_b'][:])

print('Fine root litter cellulose fraction',para_var['fates_fr_fcel'][:])
print('Fine root litter labile fraction',para_var['fates_fr_flab'][:])
print('Fine root litter lignin fraction',para_var['fates_fr_flig'][:])

print('')
                                    
#######################################
  ### Seed ###
####################################### 
para_var['fates_seed_alloc'][:]=[0.0522]
para_var['fates_seed_decay_rate'][:]=[0.51]
para_var['fates_seed_germination_rate'][:]=[0.5]  
para_var['fates_seed_suppl'][:]=[0.001]

print('Fraction of available carbon balance allocated to seeds:',
      para_var['fates_seed_alloc'][:])
print('Fraction of seeds that decay per year:',
      para_var['fates_seed_decay_rate'][:])
print('Fraction of seeds that germinate per year:',
      para_var['fates_seed_germination_rate'][:])
print('Supplemental external seed rain source term:',
      para_var['fates_seed_suppl'][:])
print('')
  
#######################################
  ### Retranslocation ###
#######################################
para_var['fates_turnover_carb_retrans'][:]=[[0.25],[0.0],[0.0],[0.0]]
para_var['fates_turnover_nitr_retrans'][:]=[[0.45],[0.25],[0.0],[0.0]] # 0.45 0.25 0 0 
para_var['fates_turnover_phos_retrans'][:]=[[0.25],[0.25],[0.0],[0.0]] # 0.25 0.25 0 0

print('Retranslocation carbon:',para_var['fates_turnover_carb_retrans'][:].tolist())
print('Retranslocation nitrogen:',para_var['fates_turnover_nitr_retrans'][:].tolist())
print('Retranslocation phosphorous:',para_var['fates_turnover_phos_retrans'][:].tolist())
print('')

#######################################
  ### AD ###
#######################################

para_var['fates_eca_vmax_p'][:]=[0.000000001]

para.close()
