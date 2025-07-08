class filepaths():
    def __init__(self):
        self.W51dir = '/orange/adamginsburg/w51/TaehwaYoo/'
        #---------------------------------------- W51 B6 (old) ----------------------------------------
        self.W51_b6_cont_old = '/orange/adamginsburg/w51/TaehwaYoo/b6contfits/'
        self.w51e2_b6_briggs = self.W51_b6_cont_old+'W51e2_cont_bigbriggs.image.fits'
        self.w51e2_b6_robust0 = self.W51_b6_cont_old+'W51e2_cont_big_robust0.image.fits'
        self.w51e2_b6_uniform = self.W51_b6_cont_old+'W51e2_cont_biguniform.image.fits'
        self.w51e2_b6_superuniform = self.W51_b6_cont_old+'W51e2_cont_bigsuperuniform.image.fits'

        self.w51n_b6_briggs = self.W51_b6_cont_old+'W51n_cont_bigbriggs.image.fits'
        self.w51n_b6_robust0 = self.W51_b6_cont_old+'w51n_cont_big_robust0.image.fits'
        self.w51n_b6_uniform = self.W51_b6_cont_old+'W51n_cont_biguniform.image.fits'
        self.w51n_b6_superuniform = self.W51_b6_cont_old+'W51n_cont_bigsuperuniform.image.fits'
        self.w51n_b6_natural = self.W51_b6_cont_old+'W51n_cont_bignatural.image.fits'

        #---------------------------------------- W51 B6 (new) ----------------------------------------
        #self.w51e_b6_tt0 = '/orange/adamginsburg/w51/TaehwaYoo/w51e2.spw0thru19.14500.robust0.thr0.15mJy.mfs.I.startmod.selfcal7.image.tt0.pbcor.fits'
        #self.w51n_b6_tt0 = '/orange/adamginsburg/w51/TaehwaYoo/w51n.spw0thru19.14500.robust0.thr0.1mJy.mfs.I.startmod.selfcal7.image.tt0.pbcor.fits'
        self.w51e_b6_tt0 = '/orange/adamginsburg/w51/orange/adamginsburg/w51/TaehwaYoo/w51e_b6_imaging_2025/w51e2.spw0thru19.14500.robust0.thr0.1mJy.mfs.I.startmod.selfcal7.image.tt0.pbcor.fits'
        self.w51n_b6_tt0 = '/orange/adamginsburg/w51/orange/adamginsburg/w51/TaehwaYoo/w51_b6_imaging_2025/w51n.spw0thru19.14500.robust0.thr0.1mJy.mfs.I.startmod.selfcal7.image.tt0.pbcor.fits'
        #---------------------------------------- W51 B3 ----------------------------------------
        self.W51b3 = '/orange/adamginsburg/w51/TaehwaYoo/2017.1.00293.S_W51_B3_LB/may2021_successful_imaging/'
        self.w51n_b3_tt0 = self.W51b3+'w51n.spw0thru19.14500.robust0.thr0.075mJy.mfs.I.startmod.selfcal7.image.tt0.pbcor.fits'
        self.w51n_b3_tt1 = self.W51dir +'w51n.spw0thru19.14500.robust0.thr0.075mJy.mfs.I.startmod.selfcal7.image.tt1.pbcor.fits'
        self.w51n_b3_alpha = self.W51dir +'w51n.spw0thru19.14500.robust0.thr0.075mJy.mfs.I.startmod.selfcal7.alpha.pbcor.fits'
        self.w51n_b3_pb = self.W51dir +'w51n.spw0thru19.14500.robust0.thr0.075mJy.mfs.I.startmod.selfcal7.pb.tt0'
        self.w51n_b3_remove_reg = '/orange/adamginsburg/w51/TaehwaYoo/regions/w51n_b3_remove.reg' 

        self.w51e_b3_tt0 = self.W51b3+'w51e2.spw0thru19.14500.robust0.thr0.075mJy.mfs.I.startmod.selfcal7.image.tt0.pbcor.fits'
        self.w51e_b3_tt1 = self.W51dir+'w51e2.spw0thru19.14500.robust0.thr0.075mJy.mfs.I.startmod.selfcal7.image.tt1.pbcor.fits'
        self.w51e_b3_alpha = self.W51dir+'w51e2.spw0thru19.14500.robust0.thr0.075mJy.mfs.I.startmod.selfcal7.alpha.pbcor.fits'
        self.w51e_b3_pb = self.W51dir +'w51e2.spw0thru19.14500.robust0.thr0.075mJy.mfs.I.startmod.selfcal7.pb.tt0'
        self.w51e_b3_remove_reg = '/orange/adamginsburg/w51/TaehwaYoo/regions/w51e_b3_remove.reg' 


        #---------------------------------------- image convolved to the common beam size ----------------------------------------
        self.w51conv = '/orange/adamginsburg/w51/TaehwaYoo/convolved_new/'
        self.w51e_b6_conv = self.w51conv + 'w51e_new_B6_conv.fits'
        self.w51n_b6_conv = self.w51conv + 'w51n_new_B6_conv.fits'
      
        self.w51e_b6_almaimf_conv = '/orange/adamginsburg/w51/TaehwaYoo/w51_alma_imf/w51e_B6_conv.fits'
        self.w51e_b3_almaimf_conv = '/orange/adamginsburg/w51/TaehwaYoo/w51_alma_imf/w51e_B3_conv.fits'
        self.w51n_b3_almaimf_conv = '/orange/adamginsburg/w51/TaehwaYoo/w51_alma_imf/w51n_B3_conv.fits'
        self.w51n_b6_almaimf_conv = '/orange/adamginsburg/w51/TaehwaYoo/w51_alma_imf/w51n_B6_conv.fits'


        

        
        #---------------------------------------- ALMA-IMF W51 ----------------------------------------

        self.w51n_b6_almaimf = '/orange/adamginsburg/w51/TaehwaYoo/w51_alma_imf/W51-IRS2_B6_uid___A001_X1296_X187_continuum_merged_12M_robust0_selfcal9_finaliter.image.tt0.pbcor.fits'
        self.w51n_b3_almaimf = '/orange/adamginsburg/w51/TaehwaYoo/w51_alma_imf/W51-IRS2_B3_uid___A001_X1296_X18f_continuum_merged_12M_robust0_selfcal4_finaliter.image.tt0.pbcor.fits'
        self.w51e_b6_almaimf = '/orange/adamginsburg/w51/TaehwaYoo/w51_alma_imf/W51-E_B6_uid___A001_X1296_X213_continuum_merged_12M_robust0_selfcal7_finaliter.image.tt0.pbcor.fits'
        self.w51e_b3_almaimf = '/orange/adamginsburg/w51/TaehwaYoo/w51_alma_imf/W51-E_B3_uid___A001_X1296_X10b_continuum_merged_12M_robust0_selfcal7_finaliter.image.tt0.pbcor.fits'

        self.w51n_b6_almaimf_local = '/Users/dbahck37/W51data/alma_imf/W51-IRS2_B6_uid___A001_X1296_X187_continuum_merged_12M_robust0_selfcal9_finaliter.image.tt0.pbcor.fits'
        self.w51n_b3_almaimf_local = '/Users/dbahck37/W51data/alma_imf/W51-IRS2_B3_uid___A001_X1296_X18f_continuum_merged_12M_robust0_selfcal4_finaliter.image.tt0.pbcor.fits'
        self.w51e_b6_almaimf_local = '/Users/dbahck37/W51data/alma_imf/W51-E_B6_uid___A001_X1296_X213_continuum_merged_12M_robust0_selfcal7_finaliter.image.tt0.pbcor.fits'
        self.w51e_b3_almaimf_local = '/Users/dbahck37/W51data/alma_imf/W51-E_B3_uid___A001_X1296_X10b_continuum_merged_12M_robust0_selfcal7_finaliter.image.tt0.pbcor.fits'

        self.w51e_almaimf_catalog_local = '/Users/dbahck37/W51data/alma_imf/catalog/getsf-smoothed/W51-E-getsf.cat'
        self.w51n_almaimf_catalog_local = '/Users/dbahck37/W51data/alma_imf/catalog/getsf-smoothed/W51-IRS2-getsf.cat'
        self.w51e_almaimf_catalog = '/orange/adamginsburg/w51/TaehwaYoo/ALMA_IMF/catalogs/getsf-smoothed/W51-E-getsf.cat'
        self.w51n_almaimf_catalog = '/orange/adamginsburg/w51/TaehwaYoo/ALMA_IMF/catalogs/getsf-smoothed/W51-IRS2-getsf.cat'
        self.w51e_almaimf_coretemp = '/red/adamginsburg/t.yoo/w51/W51-E_core_temperature_smooth_catalog.dat'
        self.w51n_almaimf_coretemp = '/red/adamginsburg/t.yoo/w51/W51-IRS2_core_temperature_smooth_catalog.dat'


        #---------------------------------------- W51 background noises ----------------------------------------
        self.w51e_b6_background = '/red/adamginsburg/t.yoo/w51/w51_frag/dendrogram/background_noise_w51e_b6_pb.dat'
        self.w51e_b3_background = '/red/adamginsburg/t.yoo/w51/w51_frag/dendrogram/background_noise_w51e_b3_pb.dat'
        self.w51n_b6_background = '/red/adamginsburg/t.yoo/w51/w51_frag/dendrogram/background_noise_w51n_b6_pb.dat'
        self.w51n_b3_background = '/red/adamginsburg/t.yoo/w51/w51_frag/dendrogram/background_noise_w51n_b3_pb.dat'

        self.w51e_B3_catalog = '/red/adamginsburg/t.yoo/w51/w51_frag/dendrogram/dendro_w51e_b3_visual_inspection_merge_new.fits' #changed after 2025/04/29
        self.w51e_B6_catalog = '/red/adamginsburg/t.yoo/w51/w51_frag/dendrogram/dendro_w51e_b6_visual_inspection2_new.fits'
        self.w51n_B3_catalog = '/red/adamginsburg/t.yoo/w51/w51_frag/dendrogram/dendro_w51n_b3_visual_inspection.fits'
        self.w51n_B6_catalog = '/red/adamginsburg/t.yoo/w51/w51_frag/dendrogram/dendro_w51n_b6_visual_inspection.fits'


        #---------------------------------------- W51 catalogs ----------------------------------------
        #self.w51e_dendro_matched_catalog_old = '/red/adamginsburg/t.yoo/w51/w51_frag/dendrogram/dendro_w51e_matched.fits'
        self.w51e_dendro_matched_catalog_old = '/red/adamginsburg/t.yoo/w51/w51_frag/dendrogram/dendro_w51e_matched_new.fits'
        self.w51n_dendro_matched_catalog_old = '/red/adamginsburg/t.yoo/w51/w51_frag/dendrogram/dendro_w51n_matched_new.fits'
        self.w51e_dendro_matched_catalog_new = '/red/adamginsburg/t.yoo/w51/w51_frag_new/dendro/tables/dendro_w51e_matched_final.fits'
        self.w51n_dendro_matched_catalog_new = '/red/adamginsburg/t.yoo/w51/w51_frag_new/dendro/tables/dendro_w51n_matched.fits'
        # catalogs with flux file and dendro file combined
        self.w51e_dendro_master =  '/red/adamginsburg/t.yoo/w51/w51_frag/dendrogram/dendro_w51e_master.fits'
        self.w51n_dendro_master =  '/red/adamginsburg/t.yoo/w51/w51_frag/dendrogram/dendro_w51n_master.fits'
        #---------------------------------------- W51 catalogs (trimmed for shared use) ----------------------------------------
        self.w51e_dendro_matched_catalog1_trimmed = '/red/adamginsburg/t.yoo/w51/w51_frag/dendro_w51e_matched1.fits'
        self.w51e_dendro_matched_catalog2_trimmed = '/red/adamginsburg/t.yoo/w51/w51_frag/dendro_w51e_matched2.fits'
        self.w51n_dendro_matched_catalog1_trimmed = '/red/adamginsburg/t.yoo/w51/w51_frag/dendro_w51n_matched1.fits'
        self.w51n_dendro_matched_catalog2_trimmed = '/red/adamginsburg/t.yoo/w51/w51_frag/dendro_w51n_matched2.fits'

        #---------------------------------------- W51 flux ----------------------------------------
        self.w51e_b6_flux_old = '/red/adamginsburg/t.yoo/w51/w51_frag/photometry/flux_new/w51e_b6_test.fits'
        self.w51e_b3_flux_old = '/red/adamginsburg/t.yoo/w51/w51_frag/photometry/flux_new/w51e_b3_test.fits'
        self.w51e_b6_flux = '/red/adamginsburg/t.yoo/w51/w51_frag/photometry/flux_new/w51e_b6_test.fits'
        self.w51e_b3_flux = '/red/adamginsburg/t.yoo/w51/w51_frag/photometry/flux_new/w51e_b3_test.fits'
        
        self.w51n_b6_flux = '/red/adamginsburg/t.yoo/w51/w51_frag/photometry/flux_new/w51n_b6_test.fits'
        self.w51n_b3_flux = '/red/adamginsburg/t.yoo/w51/w51_frag/photometry/flux_new/w51n_b3_test.fits'
        self.w51e_b6_conv_flux_old = '/red/adamginsburg/t.yoo/w51/w51_frag/photometry/flux_new/w51e_b6_conv_test.fits'
        self.w51e_b6_conv_flux = '/red/adamginsburg/t.yoo/w51/w51_frag/photometry/flux_new/w51e_b6_conv_test.fits'
        self.w51n_b6_conv_flux = '/red/adamginsburg/t.yoo/w51/w51_frag/photometry/flux_new/w51n_b6_conv_test.fits'


        self.w51e_b6_flux_local = '/Users/dbahck37/w51_jupyter/w51/w51_frag/photometry/w51e_b6_test.fits'
        self.w51e_b3_flux_local = '/Users/dbahck37/w51_jupyter/w51/w51_frag/photometry/w51e_b3_test.fits'
        self.w51n_b6_flux_local = '/Users/dbahck37/w51_jupyter/w51/w51_frag/photometry/w51n_b6_test.fits'
        self.w51n_b3_flux_local = '/Users/dbahck37/w51_jupyter/w51/w51_frag/photometry/w51n_b3_test.fits'
        self.w51e_b6_conv_flux_local = '/Users/dbahck37/w51_jupyter/w51/w51_frag/photometry/w51e_b6_conv_test.fits'
        self.w51n_b6_conv_flux_local = '/Users/dbahck37/w51_jupyter/w51/w51_frag/photometry/w51n_b6_conv_test.fits'

        #---------------------------------------- W51 noise region ----------------------------------------
        self.w51e_b6_noise_region = '/orange/adamginsburg/w51/TaehwaYoo/w51e_b6_std_sky_new.reg'
        self.w51e_b3_noise_region = '/orange/adamginsburg/w51/TaehwaYoo/w51e_b3_std_sky_new.reg'
        self.w51n_b6_noise_region = '/orange/adamginsburg/w51/TaehwaYoo/w51n_b6_std_sky_new.reg'
        self.w51n_b3_noise_region = '/orange/adamginsburg/w51/TaehwaYoo/w51n_b3_std_sky_new.reg'

        self.w51e_b6_noise_region_local = '/Users/dbahck37/w51data/w51e_b6_std_sky_new.reg'
        self.w51e_b3_noise_region_local = '/Users/dbahck37/w51data/w51e_b3_std_sky_new.reg'
        self.w51n_b6_noise_region_local = '/Users/dbahck37/w51data/w51n_b6_std_sky_new.reg'
        self.w51n_b3_noise_region_local = '/Users/dbahck37/w51data/w51n_b3_std_sky_new.reg'

        #---------------------------------------- localdir ----------------------------------------
        self.localdir = '/Users/dbahck37/w51data'
        self.w51e_b6_cont_local = self.localdir + '/w51e2.spw0thru19.14500.robust0.thr0.15mJy.mfs.I.startmod.selfcal7.image.tt0.pbcor.fits'
        self.w51n_b6_cont_local = self.localdir + '/w51n.spw0thru19.14500.robust0.thr0.1mJy.mfs.I.startmod.selfcal7.image.tt0.pbcor.fits'
        self.w51e_b3_cont_local = self.localdir + '/b3data/w51e2.spw0thru19.14500.robust0.thr0.075mJy.mfs.I.startmod.selfcal7.image.tt0.pbcor.fits'
        self.w51n_b3_cont_local = self.localdir + '/b3data/w51n.spw0thru19.14500.robust0.thr0.075mJy.mfs.I.startmod.selfcal7.image.tt0.pbcor.fits'
        self.w51e_b6_conv_local = self.localdir + '/convolved_new/w51e_new_B6_conv.fits'
        self.w51n_b6_conv_local = self.localdir + '/convolved_new/w51n_new_B6_conv.fits'    

        self.w51e_dendro_matched_catalog_local = '/Users/dbahck37/w51_jupyter/w51/w51_frag/dendrogram/dendro_w51e_matched.fits'
        self.w51n_dendro_matched_catalog_local = '/Users/dbahck37/w51_jupyter/w51/w51_frag/dendrogram/dendro_w51n_matched.fits'

        #---------------------------------------- W51 JWST MIRI ----------------------------------------
        self.jwstdir = '/orange/adamginsburg/w51/TaehwaYoo/jwst_w51/'
        self.w51_F560W = self.jwstdir + 'F560W/pipeline/jw06151-o002_t001_miri_f560w_i2d.fits'
        self.w51_F770W = self.jwstdir + 'F770W/pipeline/jw06151-o002_t001_miri_f770w_i2d.fits'
        self.w51_F1000W = self.jwstdir + 'F1000W/pipeline/jw06151-o002_t001_miri_f1000w_i2d.fits'
        self.w51_F1280W = self.jwstdir + 'F1280W/pipeline/jw06151-o002_t001_miri_f1280w_i2d.fits'
        self.w51_F2100W = self.jwstdir + 'F2100W/pipeline/jw06151-o002_t001_miri_f2100w_i2d.fits'