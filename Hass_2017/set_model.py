from name2idx import parameters as C
from name2idx import species as V

class DifferentialEquation(object):
    def __init__(self, pertubation): #dunder-> double underscores
        self.pertubation = pertubation

    #Defined Model
    def diffeq(self, t, y, *x):
        v = [0]*114
        # Rate equations
        ## Production
        #v[1] = x[C.EGFR_prod]
        v[1] =  2*(x[C.EGFR_basal_activation]* x[C.init_EGFR]**2/(x[C.init_RTKph]* x[C.pEGFR_phosphatase_binding]+ x[C.pEGFR_degradation]))* \
                x[C.pEGFR_degradation]+ (x[C.EGFR_ErbB2_basal_act]*	x[C.init_EGFR]*	x[C.init_ErbB2]/(x[C.init_RTKph]* x[C.pErbB12i_phosphatase]	+ \
                x[C.pErbB12_degradation]))* x[C.pErbB12_degradation]+ (x[C.EGFR_ErbB3_basal_act]* x[C.init_EGFR]* x[C.init_ErbB3]/ (x[C.init_RTKph]* \
                x[C.pErbB13i_phosphatase]+ x[C.pErbB13_degradation]))* x[C.pErbB13_degradation]+ (x[C.Met_EGFR_basal_act]* x[C.init_EGFR]* x[C.init_Met]/ \
                (x[C.init_RTKph]* x[C.pMetEGFRi_phosphatase]+x [C.pMetEGFR_degradation]))* x[C.pMetEGFR_degradation]
        #v[2] = x[C.ErbB2_prod]
        v[2] = (x[C.EGFR_ErbB2_basal_act]* x[C.init_EGFR]* x[C.init_ErbB2]/ (x[C.init_RTKph]* x[C.pErbB12i_phosphatase]	+ x[C.pErbB12_degradation]))* \
                x[C.pErbB12_degradation]+ 2*(x[C.ErbB2_dimerize]* x[C.init_ErbB2]**2/ (x[C.init_RTKph]* x[C.pErbB2i_phosphatase]+ x[C.pErbB2_degradation]))* \
                x[C.pErbB2_degradation]+ (x[C.ErbB3_ErbB2_basal_act]* x[C.init_ErbB2]* x[C.init_ErbB3]/	(x[C.init_RTKph]* x[C.pErbB32i_phosphatase]+ \
                x[C.pErbB32_degradation]))* x[C.pErbB32_degradation]
        #v[3] = x[C.ErbB3_prod]
        v[3] =  (x[C.EGFR_ErbB3_basal_act]* x[C.init_EGFR]*	x[C.init_ErbB3]/(x[C.init_RTKph]* x[C.pErbB13i_phosphatase]+ x[C.pErbB13_degradation]))* \
                x[C.pErbB13_degradation]+ (x[C.ErbB3_ErbB2_basal_act]* x[C.init_ErbB2]* x[C.init_ErbB3]/ (x[C.init_RTKph]* x[C.pErbB32i_phosphatase]+ \
                x[C.pErbB32_degradation]))*	x[C.pErbB32_degradation]+ (x[C.Met_ErbB3_basal_act]* x[C.init_ErbB3]* x[C.init_Met]/ (x[C.init_RTKph]* \
                x[C.pMetErbB3i_phosphatase]+ x[C.pMetErbB3_degradation]))* x[C.pMetErbB3_degradation]
        #v[4] = x[C.IGF1R_prod]
        v[4] = 2* (x[C.IGF1R_basal_activation]*	x[C.init_IGF1R]**2/ (x[C.init_RTKph]* x[C.pIGF1Ri_phosphatase]+ x[C.pIGF1R_degradation]))* x[C.pIGF1R_degradation]
        #v[5] = x[C.Met_prod]
        v[5] = (x[C.Met_EGFR_basal_act]* x[C.init_EGFR]* x[C.init_Met]/ (x[C.init_RTKph]* x[C.pMetEGFRi_phosphatase]+ x[C.pMetEGFR_degradation]))* \
                x[C.pMetEGFR_degradation]+	(x[C.Met_ErbB3_basal_act]*	x[C.init_ErbB3]* x[C.init_Met]/	(x[C.init_RTKph]* x[C.pMetErbB3i_phosphatase]+ \
                x[C.pMetErbB3_degradation]))* x[C.pMetErbB3_degradation]+ 2*(x[C.Met_basal_act]* x[C.init_Met]**2/ (x[C.init_RTKph]* x[C.pMeti_phosphatase]	+	\
                x[C.pMet_degradation]))* x[C.pMet_degradation]

        ## Ligand binding
        v[6] = y[V.EGFR]* x[C.EGFR_lig_binding]* y[V.dose_EGF]
        v[7] = y[V.EGFR_EGF]* x[C.EGFR_lig_binding]* x[C.EGF_kD]
        v[8] = y[V.EGFR]* x[C.EGFR_BTC_binding]* y[V.dose_BTC]
        v[9] = y[V.EGFR_BTC]* x[C.EGFR_BTC_binding]* x[C.EGF_kD]

        v[10] = y[V.ErbB3]* x[C.ErbB3_lig_binding]* y[V.dose_HRG]        
        v[11] = y[V.ErbB3_HRG]* x[C.ErbB3_lig_binding]* x[C.HRG_kD]
        v[12] = y[V.IGF1R]* x[C.IGF1R_lig_binding]* y[V.dose_IGF1]
        v[13] = y[V.IGF1R_IGF1]* x[C.IGF1R_lig_binding]* x[C.IGF1_kD]
        v[14] = y[V.Met]* x[C.Met_lig_binding]* y[V.dose_HGF]
        v[15] = x[C.HGF_kD]* y[V.Met_HGF]* x[C.Met_lig_binding]

        ##Dimerization
        v[16] = (y[V.EGFR_EGF]**2)* x[C.EGFR_dimerize]
        v[17] = (y[V.EGFR_BTC]**2)* x[C.EGFR_BTC_dimerize]

        v[18] = (y[V.ErbB2]**2)* x[C.ErbB2_dimerize]

        v[19] = (y[V.ErbB3_HRG]**2)* x[C.ErbB3_dimerize]

        v[20] = (y[V.IGF1R_IGF1]**2)* x[C.IGF1R_dimerize]

        v[21] = y[V.EGFR_EGF]* x[C.EGFR_ErbB2_dimerize]* y[V.ErbB2]
        v[22] = y[V.EGFR_BTC]* x[C.EGFR_ErbB2_BTC_dimerize]* y[V.ErbB2]

        v[23] = y[V.EGFR_EGF]* x[C.EGFR_ErbB3_dimerize]* y[V.ErbB3_HRG]
        v[24] = y[V.EGFR_BTC]* x[C.EGFR_ErbB3_BTC_dimerize]* y[V.ErbB3_HRG]
        v[25] = y[V.EGFR_BTC]* x[V.EGFR_ErbB3_dimerize_noHRG]* y[V.ErbB3]

        v[26] = y[V.ErbB2]* x[C.ErbB2_ErbB3_dimerize]* y[V.ErbB3_HRG]

        v[27] = (y[V.Met_HGF]**2)* x[C.Met_dimerize]

        v[28] = y[V.ErbB3_HRG]* y[V.Met]* x[C.Met_ErbB3_dimerize]

        v[29] = y[V.ErbB3_HRG]* y[V.Met_HGF]* x[C.Met_lig_ErbB3_dimerize]

        v[30] = y[V.EGFR_EGF]* x[C.Met_EGFR_dimerize]* y[V.Met_HGF]
        v[31] = y[V.EGFR_BTC]* x[C.Met_EGFR_BTC_dimerize]* y[V.Met_HGF]

        ##Basal phosphorylations
        v[32] = (y[V.EGFR]**2)* x[C.EGFR_basal_activation]
        v[33] = (y[V.ErbB3]**2)* x[C.ErbB3_basal_activation]
        v[34] = (y[V.IGF1R]**2)* x[C.IGF1R_basal_activation]

        v[35] = y[V.EGFR]* x[C.EGFR_ErbB2_basal_act]* y[V.ErbB2]
        v[36] = y[V.EGFR]* x[C.EGFR_ErbB3_basal_act]* y[V.ErbB3]
        v[37] = y[V.ErbB2]* y[V.ErbB3]* x[C.ErbB3_ErbB2_basal_act]
        v[38] = y[V.ErbB3]* y[V.Met]* x[C.Met_ErbB3_basal_act]
        v[39] = (y[V.Met]**2)*x[C.Met_basal_act]
        v[40] = y[V.EGFR]* y[V.Met]* x[C.Met_EGFR_basal_act]

        ##Phosphorylation
        ###EGFR homodimers
        v[41] = x[C.pEGFR_internalize]* y[V.pEGFRd]
        v[42] = x[C.pEGFR_degradation]* y[V.pEGFRi]
        v[43] = y[V.RTKph]* x[C.pEGFR_phosphatase_binding]* y[V.pEGFRi]
        v[44] = x[C.pEGFRi_dephosph]* y[V.pEGFRi_ph]
        v[45] = x[C.EGFR_basal_recycle]* y[V.EGFRi]

        ###ErbB2 homodimers
        v[46] = y[V.pErbB2]* x[C.pErbB2_internalize]
        v[47] = y[V.RTKph]* y[V.pErbB2i]* x[C.pErbB2i_phosphatase]
        v[48] = x[C.pErbB2i_dephosph]* y[V.pErbB2i_ph]
        v[49] = x[C.pErbB2_degradation]* y[V.pErbB2i]
        v[50] = x[C.ErbB2_recycle]* y[V.ErbB2i]

        ###ErbB3 homodimers
        v[51] = x[C.pErbB3_internalize]* y[V.pErbB3d]
        v[52] = x[C.pErbB3_degradation]* y[V.pErbB3i]
        v[53] = y[V.RTKph]* y[V.pErbB3i]* x[C.pErbB3i_phosphatase]
        v[54] = x[C.pErbB3i_dephosph]* y[V.pErbB3i_ph]
        v[55] = x[C.ErbB3_basal_recycle]* y[V.ErbB3i]

        ###IGF1R homodimers
        v[56] = x[C.pIGF1R_internalize]* y[V.pIGF1Rd]
        v[57] = x[C.pIGF1R_degradation]* y[V.pIGF1Ri]
        v[58] = y[V.RTKph]* y[V.pIGF1Ri]* x[C.pIGF1Ri_phosphatase]
        v[59] = x[C.pIGF1Ri_dephosph]* y[V.pIGF1Ri_ph]
        v[60] = x[C.IGF1R_basal_recycle]* y[V.IGF1Ri]

        ###EGFR-ErbB2 heterodimers
        v[61] = y[V.pErbB12]* x[C.pErbB12_internalize]
        v[62] = x[C.pErbB12_degradation]* y[V.pErbB12i]
        v[63] = y[V.RTKph]* y[V.pErbB12i]* x[C.pErbB12i_phosphatase]
        v[64] = x[C.pErbB12i_dephosph]* y[V.pErbB12i_ph]

        ###ErbB2 - ErbB3 heterodimers
        v[65] = y[V.pErbB32]* x[C.pErbB32_internalize]
        v[66] = x[C.pErbB32_degradation]* y[V.pErbB32i]
        v[67] = y[V.RTKph]* y[V.pErbB32i]* x[C.pErbB32i_phosphatase]
        v[68] = x[C.pErbB32i_dephosph]* y[V.pErbB32i_ph]

        ###EGFR-ErbB3 heterodimers
        v[69] = y[V.pErbB13]* x[C.pErbB13_internalize]
        v[70] = x[C.pErbB13_degradation]* y[V.pErbB13i]
        v[71] = y[V.RTKph]* y[V.pErbB13i]* x[C.pErbB13i_phosphatase]
        v[72] = x[C.pErbB13i_dephosph]* y[V.pErbB13i_ph]

        ###MET homodimers
        v[73] = x[C.pMet_internalize]* y[V.pMetd]
        v[74] = x[C.pMet_degradation]* y[V.pMeti]
        v[75] = y[V.RTKph]* y[V.pMeti]* x[C.pMeti_phosphatase]
        v[76] = x[C.pMeti_dephosph]* y[V.pMeti_ph]
        v[77] = x[C.Met_recycle]* y[V.Meti]

        ###MET-ErbB3 heterodimers
        v[78] = y[V.pMetErbB3]* x[C.pMetErbB3_internalize]
        v[79] = x[C.pMetErbB3_degradation]* y[V.pMetErbB3i]
        v[80] = y[V.RTKph]* y[V.pMetErbB3i]* x[C.pMetErbB3i_phosphatase]
        v[81] = x[C.pMetErbB3i_dephosph]* y[V.pMetErbB3i_ph]

        ###MET-EGFR heterodimers
        v[82] = y[V.pMetEGFR]* x[C.pMetEGFR_internalize]
        v[83] = x[C.pMetEGFR_degradation]* y[V.pMetEGFRi]
        v[84] = y[V.RTKph]* y[V.pMetEGFRi]* x[C.pMetEGFRi_phosphatase]
        v[85] = x[C.pMetEGFRi_dephosph]* y[V.pMetEGFRi_ph]

        ##DOWNSTREAM
        ###ERK branch !init_pAKT, init_pEGFRd, init_pErbB12,init_pErbB13,init_pErbB32,init_pIGF1Ri, init_pIGF1Rd, init_pMetEGFR=Init_pMET_EGFR, init_pMetErbB3,init_pMetd
        v[86] = (y[V.MEK]* x[C.MEK_phosphorylation_pEGFR]* y[V.pEGFRd])/ (1+ x[C.feedback_pAKT]* (x[C.init_AKT]* (x[C.AKT_activation_pEGFR]* \
                (x[C.EGFR_basal_activation]* x[C.init_EGFR]**2/ x[C.pEGFR_internalize])+ x[C.AKT_activation_pErbB12]* (x[C.EGFR_ErbB2_basal_act]* \
                x[C.init_EGFR]* x[C.init_ErbB2]/ x[C.pErbB12_internalize])+ x[C.AKT_activation_pErbB13]* (x[C.EGFR_ErbB3_basal_act]* x[C.init_EGFR]* \
                x[C.init_ErbB3]/ x[C.pErbB13_internalize])+	x[C.AKT_activation_pErbB32]* (x[C.ErbB3_ErbB2_basal_act]* x[C.init_ErbB2]* x[C.init_ErbB3]/ \
                x[C.pErbB32_internalize])+ x[C.AKT_activation_pIGF1R]* x[C.AKT_internIGF1R_effect]* (x[C.IGF1R_basal_activation]* x[C.init_IGF1R]**2/ \
                (x[C.init_RTKph]* x[C.pIGF1Ri_phosphatase]+	x[C.pIGF1R_degradation]))+ x[C.AKT_activation_pIGF1R]* (x[C.IGF1R_basal_activation]* \
                x[C.init_IGF1R]**2/ x[C.pIGF1R_internalize])+ x[C.AKT_activation_pMetEGFR]*	(x[C.Met_EGFR_basal_act]* x[C.init_EGFR]* x[C.init_Met]/ \
                x[C.pMetEGFR_internalize])+	x[C.AKT_activation_pMetErbB3]* (x[C.Met_ErbB3_basal_act]* x[C.init_ErbB3]* x[C.init_Met]/ x[C.pMetErbB3_internalize])+ \
                x[C.AKT_activation_pMetd]* (x[C.Met_basal_act]*	x[C.init_Met]**2/ x[C.pMet_internalize]))/ (x[C.pAKT_deactivation]* (x[C.feedback_pERK_on_AKT]* \
                x[C.init_pERK]+	x[C.feedback_pS6K1]* x[C.init_pS6K1]+ 1)))+ x[C.feedback_pERK]* y[V.pERK])

        v[87] = (y[V.MEK]* x[C.MEK_phosphorylation_pErbB12]* y[V.pErbB12])/ (1+ x[C.feedback_pAKT]* (x[C.init_AKT]* (x[C.AKT_activation_pEGFR]*	\
                (x[C.EGFR_basal_activation]* x[C.init_EGFR]**2/ x[C.pEGFR_internalize])+ x[C.AKT_activation_pErbB12]* (x[C.EGFR_ErbB2_basal_act]* \
                x[C.init_EGFR]*	x[C.init_ErbB2]/ x[C.pErbB12_internalize])+ x[C.AKT_activation_pErbB13]* (x[C.EGFR_ErbB3_basal_act]* x[C.init_EGFR]* \
                x[C.init_ErbB3]/ x[C.pErbB13_internalize])+	x[C.AKT_activation_pErbB32]* (x[C.ErbB3_ErbB2_basal_act]* x[C.init_ErbB2]* x[C.init_ErbB3]/ \
                x[C.pErbB32_internalize])+ x[C.AKT_activation_pIGF1R]* x[C.AKT_internIGF1R_effect]*	(x[C.IGF1R_basal_activation]* x[C.init_IGF1R]**2/ \
                (x[C.init_RTKph]* x[C.pIGF1Ri_phosphatase]+	x[C.pIGF1R_degradation]))+ x[C.AKT_activation_pIGF1R]* (x[C.IGF1R_basal_activation]* \
                x[C.init_IGF1R]**2/ x[C.pIGF1R_internalize])+ x[C.AKT_activation_pMetEGFR]*	(x[C.Met_EGFR_basal_act]* x[C.init_EGFR]* x[C.init_Met]/ \
                x[C.pMetEGFR_internalize])+	x[C.AKT_activation_pMetErbB3]* (x[C.Met_ErbB3_basal_act]* x[C.init_ErbB3]* x[C.init_Met]/ x[C.pMetErbB3_internalize])+ \
                x[C.AKT_activation_pMetd]* (x[C.Met_basal_act]*	x[C.init_Met]**2/ x[C.pMet_internalize]))/ (x[C.pAKT_deactivation]* (x[C.feedback_pERK_on_AKT]* \
                x[C.init_pERK]+ x[C.feedback_pS6K1]* x[C.init_pS6K1]+ 1)))+ x[C.feedback_pERK]* y[V.pERK])

        v[88] = (y[V.MEK]* x[C.MEK_phosphorylation_pErbB13]* y[V.pErbB13])/ (1+ x[C.feedback_pAKT]* (x[C.init_AKT]*	(x[C.AKT_activation_pEGFR]*	\
                (x[C.EGFR_basal_activation]* x[C.init_EGFR]**2/ x[C.pEGFR_internalize])+ x[C.AKT_activation_pErbB12]* (x[C.EGFR_ErbB2_basal_act]* \
                x[C.init_EGFR]*	x[C.init_ErbB2]/ x[C.pErbB12_internalize])+ x[C.AKT_activation_pErbB13]* (x[C.EGFR_ErbB3_basal_act]* x[C.init_EGFR]* \
                x[C.init_ErbB3]/ x[C.pErbB13_internalize])+	x[C.AKT_activation_pErbB32]* (x[C.ErbB3_ErbB2_basal_act]* x[C.init_ErbB2]* x[C.init_ErbB3]/ \
                x[C.pErbB32_internalize])+ x[C.AKT_activation_pIGF1R]* x[C.AKT_internIGF1R_effect]* (x[C.IGF1R_basal_activation]* x[C.init_IGF1R]**2/ \
                (x[C.init_RTKph]* x[C.pIGF1Ri_phosphatase]+	x[C.pIGF1R_degradation]))+ x[C.AKT_activation_pIGF1R]* (x[C.IGF1R_basal_activation]* \
                x[C.init_IGF1R]**2/ x[C.pIGF1R_internalize])+ x[C.AKT_activation_pMetEGFR]* (x[C.Met_EGFR_basal_act]* x[C.init_EGFR]* x[C.init_Met]/ \
                x[C.pMetEGFR_internalize])+ x[C.AKT_activation_pMetErbB3]* (x[C.Met_ErbB3_basal_act]* x[C.init_ErbB3]* x[C.init_Met]/ x[C.pMetErbB3_internalize])+ \
                x[C.AKT_activation_pMetd]* (x[C.Met_basal_act]* x[C.init_Met]**2/ x[C.pMet_internalize]))/ (x[C.pAKT_deactivation]* (x[C.feedback_pERK_on_AKT]* \
                x[C.init_pERK]+ x[C.feedback_pS6K1]* x[C.init_pS6K1]+ 1)))+ x[C.feedback_pERK]* y[V.pERK])

        v[89] = (y[V.MEK]* x[C.MEK_phosphorylation_pErbB32]* y[V.pErbB32])/ (1+ x[C.feedback_pAKT]* (x[C.init_AKT]*	(x[C.AKT_activation_pEGFR]*	\
                (x[C.EGFR_basal_activation]* x[C.init_EGFR]**2/ x[C.pEGFR_internalize])+ x[C.AKT_activation_pErbB12]* (x[C.EGFR_ErbB2_basal_act]* \
                x[C.init_EGFR]* x[C.init_ErbB2]/ x[C.pErbB12_internalize])+ x[C.AKT_activation_pErbB13]* (x[C.EGFR_ErbB3_basal_act]* x[C.init_EGFR]* \
                x[C.init_ErbB3]/ x[C.pErbB13_internalize])+	x[C.AKT_activation_pErbB32]* (x[C.ErbB3_ErbB2_basal_act]* x[C.init_ErbB2]* x[C.init_ErbB3]/ \
                x[C.pErbB32_internalize])+ x[C.AKT_activation_pIGF1R]* x[C.AKT_internIGF1R_effect]*	(x[C.IGF1R_basal_activation]* x[C.init_IGF1R]**2/ \
                (x[C.init_RTKph]* x[C.pIGF1Ri_phosphatase]+	x[C.pIGF1R_degradation]))+ x[C.AKT_activation_pIGF1R]* (x[C.IGF1R_basal_activation]* \
                x[C.init_IGF1R]**2/ x[C.pIGF1R_internalize])+ x[C.AKT_activation_pMetEGFR]*	(x[C.Met_EGFR_basal_act]* x[C.init_EGFR]* x[C.init_Met]/ \
                x[C.pMetEGFR_internalize])+ x[C.AKT_activation_pMetErbB3]* (x[C.Met_ErbB3_basal_act]* x[C.init_ErbB3]* x[C.init_Met]/ x[C.pMetErbB3_internalize])+ \
                x[C.AKT_activation_pMetd]* (x[C.Met_basal_act]*	x[C.init_Met]**2/ x[C.pMet_internalize]))/ (x[C.pAKT_deactivation]* (x[C.feedback_pERK_on_AKT]* \
                x[C.init_pERK]+ x[C.feedback_pS6K1]* x[C.init_pS6K1]+ 1)))+ x[C.feedback_pERK]* y[V.pERK])

        v[90] = (y[V.MEK]* x[C.MEK_phosphorylation_pMetd]* y[V.pMetd])/ (1+ x[C.feedback_pAKT]* (x[C.init_AKT]* (x[C.AKT_activation_pEGFR]* \
                (x[C.EGFR_basal_activation]* x[C.init_EGFR]**2/ x[C.pEGFR_internalize])+ x[C.AKT_activation_pErbB12]* (x[C.EGFR_ErbB2_basal_act]* \
                x[C.init_EGFR]*	x[C.init_ErbB2]/ x[C.pErbB12_internalize])+ x[C.AKT_activation_pErbB13]* (x[C.EGFR_ErbB3_basal_act]* x[C.init_EGFR]* \
                x[C.init_ErbB3]/ x[C.pErbB13_internalize])+	x[C.AKT_activation_pErbB32]* (x[C.ErbB3_ErbB2_basal_act]* x[C.init_ErbB2]* x[C.init_ErbB3]/ \
                x[C.pErbB32_internalize])+ x[C.AKT_activation_pIGF1R]* x[C.AKT_internIGF1R_effect]* (x[C.IGF1R_basal_activation]* x[C.init_IGF1R]**2/ \
                (x[C.init_RTKph]* x[C.pIGF1Ri_phosphatase]+ x[C.pIGF1R_degradation]))+ x[C.AKT_activation_pIGF1R]* (x[C.IGF1R_basal_activation]* \
                x[C.init_IGF1R]**2/ x[C.pIGF1R_internalize])+ x[C.AKT_activation_pMetEGFR]* (x[C.Met_EGFR_basal_act]* x[C.init_EGFR]* x[C.init_Met]/ \
                x[C.pMetEGFR_internalize])+ x[C.AKT_activation_pMetErbB3]* (x[C.Met_ErbB3_basal_act]* x[C.init_ErbB3]* x[C.init_Met]/ x[C.pMetErbB3_internalize])+ \
                x[C.AKT_activation_pMetd]* (x[C.Met_basal_act]* x[C.init_Met]**2/ x[C.pMet_internalize]))/ (x[C.pAKT_deactivation]* (x[C.feedback_pERK_on_AKT]* \
                x[C.init_pERK]+ x[C.feedback_pS6K1]* x[C.init_pS6K1]+ 1)))+ x[C.feedback_pERK]* y[V.pERK])

        v[91] = (y[V.MEK]* x[C.MEK_phosphorylation_pMetEGFR]* y[V.pMetEGFR])/ (1+ x[C.feedback_pAKT]* (x[C.init_AKT]* (x[C.AKT_activation_pEGFR]* \
                (x[C.EGFR_basal_activation]* x[C.init_EGFR]**2/ x[C.pEGFR_internalize])+ x[C.AKT_activation_pErbB12]* (x[C.EGFR_ErbB2_basal_act]* \
                x[C.init_EGFR]*	x[C.init_ErbB2]/ x[C.pErbB12_internalize])+ x[C.AKT_activation_pErbB13]* (x[C.EGFR_ErbB3_basal_act]* x[C.init_EGFR]* \
                x[C.init_ErbB3]/ x[C.pErbB13_internalize])+ x[C.AKT_activation_pErbB32]* (x[C.ErbB3_ErbB2_basal_act]* x[C.init_ErbB2]* x[C.init_ErbB3]/ \
                x[C.pErbB32_internalize])+ x[C.AKT_activation_pIGF1R]* x[C.AKT_internIGF1R_effect]*	(x[C.IGF1R_basal_activation]* x[C.init_IGF1R]**2/ \
                (x[C.init_RTKph]* x[C.pIGF1Ri_phosphatase]+	x[C.pIGF1R_degradation]))+ x[C.AKT_activation_pIGF1R]* (x[C.IGF1R_basal_activation]* \
                x[C.init_IGF1R]**2/ x[C.pIGF1R_internalize])+ x[C.AKT_activation_pMetEGFR]* (x[C.Met_EGFR_basal_act]* x[C.init_EGFR]* x[C.init_Met]/ \
                x[C.pMetEGFR_internalize])+ x[C.AKT_activation_pMetErbB3]* (x[C.Met_ErbB3_basal_act]* x[C.init_ErbB3]* x[C.init_Met]/ x[C.pMetErbB3_internalize])+ \
                x[C.AKT_activation_pMetd]* (x[C.Met_basal_act]*	x[C.init_Met]**2/ x[C.pMet_internalize]))/ (x[C.pAKT_deactivation]* (x[C.feedback_pERK_on_AKT]* \
                x[C.init_pERK]+ x[C.feedback_pS6K1]* x[C.init_pS6K1]+ 1)))+ x[C.feedback_pERK]* y[V.pERK])
                
        v[92] = (y[V.MEK]* x[C.MEK_phosphorylation_pIGF1R]* y[V.pIGF1Rd])/( 1+ x[C.feedback_pAKT]* (x[C.init_AKT]* (x[C.AKT_activation_pEGFR]* \
                (x[C.EGFR_basal_activation]* x[C.init_EGFR]**2/ x[C.pEGFR_internalize])+ x[C.AKT_activation_pErbB12]* (x[C.EGFR_ErbB2_basal_act]* \
                x[C.init_EGFR]*	x[C.init_ErbB2]/ x[C.pErbB12_internalize])+ x[C.AKT_activation_pErbB13]* (x[C.EGFR_ErbB3_basal_act]* x[C.init_EGFR]* \
                x[C.init_ErbB3]/ x[C.pErbB13_internalize])+ x[C.AKT_activation_pErbB32]* (x[C.ErbB3_ErbB2_basal_act]* x[C.init_ErbB2]* x[C.init_ErbB3]/ \
                x[C.pErbB32_internalize])+ x[C.AKT_activation_pIGF1R]* x[C.AKT_internIGF1R_effect]* (x[C.IGF1R_basal_activation]* x[C.init_IGF1R]**2/ \
                (x[C.init_RTKph]* x[C.pIGF1Ri_phosphatase]+ x[C.pIGF1R_degradation]))+ x[C.AKT_activation_pIGF1R]* (x[C.IGF1R_basal_activation]* \
                x[C.init_IGF1R]**2/ x[C.pIGF1R_internalize])+ x[C.AKT_activation_pMetEGFR]* (x[C.Met_EGFR_basal_act]* x[C.init_EGFR]* x[C.init_Met]/ \
                x[C.pMetEGFR_internalize])+ x[C.AKT_activation_pMetErbB3]* (x[C.Met_ErbB3_basal_act]* x[C.init_ErbB3]* x[C.init_Met]/x[C.pMetErbB3_internalize])+ \
                x[C.AKT_activation_pMetd]* (x[C.Met_basal_act]*	x[C.init_Met]**2/ x[C.pMet_internalize]))/ (x[C.pAKT_deactivation]* (x[C.feedback_pERK_on_AKT]* \
                x[C.init_pERK]+ x[C.feedback_pS6K1]* x[C.init_pS6K1]+ 1)))+ x[C.feedback_pERK]* y[V.pERK])
                
        v[93] = (y[V.MEK]* x[C.MEK_phosphorylation_pMetErbB3]* y[V.pMetErbB3])/ (1+ x[C.feedback_pAKT]* (x[C.init_AKT]* (x[C.AKT_activation_pEGFR]* \
                (x[C.EGFR_basal_activation]* x[C.init_EGFR]**2/ x[C.pEGFR_internalize])+ x[C.AKT_activation_pErbB12]* (x[C.EGFR_ErbB2_basal_act]* \
                x[C.init_EGFR]*	x[C.init_ErbB2]/ x[C.pErbB12_internalize])+ x[C.AKT_activation_pErbB13]* (x[C.EGFR_ErbB3_basal_act]* x[C.init_EGFR]* \
                x[C.init_ErbB3]/ x[C.pErbB13_internalize])+ x[C.AKT_activation_pErbB32]* (x[C.ErbB3_ErbB2_basal_act]* x[C.init_ErbB2]* x[C.init_ErbB3]/ \
                x[C.pErbB32_internalize])+ x[C.AKT_activation_pIGF1R]* x[C.AKT_internIGF1R_effect]* (x[C.IGF1R_basal_activation]* x[C.init_IGF1R]**2/ \
                (x[C.init_RTKph]* x[C.pIGF1Ri_phosphatase]+ x[C.pIGF1R_degradation]))+ x[C.AKT_activation_pIGF1R]* (x[C.IGF1R_basal_activation]* \
                x[C.init_IGF1R]**2/ x[C.pIGF1R_internalize])+ x[C.AKT_activation_pMetEGFR]* (x[C.Met_EGFR_basal_act]* x[C.init_EGFR]* x[C.init_Met]/ \
                x[C.pMetEGFR_internalize])+ x[C.AKT_activation_pMetErbB3]* (x[C.Met_ErbB3_basal_act]* x[C.init_ErbB3]* x[C.init_Met]/ x[C.pMetErbB3_internalize])+ \
                x[C.AKT_activation_pMetd]* (x[C.Met_basal_act]*	x[C.init_Met]**2/ x[C.pMet_internalize]))/ (x[C.pAKT_deactivation]* (x[C.feedback_pERK_on_AKT]* \
                x[C.init_pERK]+	x[C.feedback_pS6K1]* x[C.init_pS6K1]+ 1)))+ x[C.feedback_pERK]* y[V.pERK])

        v[94] = (y[V.MEK]* x[C.MEK_internIGF1R_effect]* x[C.MEK_phosphorylation_pIGF1R]* y[V.pIGF1Ri])/(1+x[C.feedback_pAKT]* (x[C.init_AKT]* (x[C.AKT_activation_pEGFR]* \
                (x[C.EGFR_basal_activation]* x[C.init_EGFR]**2/ x[C.pEGFR_internalize])+ x[C.AKT_activation_pErbB12]* (x[C.EGFR_ErbB2_basal_act]* \
                x[C.init_EGFR]*	x[C.init_ErbB2]/ x[C.pErbB12_internalize])+ x[C.AKT_activation_pErbB13]* (x[C.EGFR_ErbB3_basal_act]* x[C.init_EGFR]* \
                x[C.init_ErbB3]/x[C.pErbB13_internalize])+ x[C.AKT_activation_pErbB32]* (x[C.ErbB3_ErbB2_basal_act]* x[C.init_ErbB2]* x[C.init_ErbB3]/ \
                x[C.pErbB32_internalize])+ x[C.AKT_activation_pIGF1R]* x[C.AKT_internIGF1R_effect]* (x[C.IGF1R_basal_activation]* x[C.init_IGF1R]**2/ \
                (x[C.init_RTKph]* x[C.pIGF1Ri_phosphatase]+ x[C.pIGF1R_degradation]))+ x[C.AKT_activation_pIGF1R]* (x[C.IGF1R_basal_activation]* \
                x[C.init_IGF1R]**2/ x[C.pIGF1R_internalize])+ x[C.AKT_activation_pMetEGFR]* (x[C.Met_EGFR_basal_act]* x[C.init_EGFR]* x[C.init_Met]/ \
                x[C.pMetEGFR_internalize])+ x[C.AKT_activation_pMetErbB3]* (x[C.Met_ErbB3_basal_act]* x[C.init_ErbB3]* x[C.init_Met]/ x[C.pMetErbB3_internalize])+ \
                x[C.AKT_activation_pMetd]* (x[C.Met_basal_act]*	x[C.init_Met]**2/ x[C.pMet_internalize]))/ (x[C.pAKT_deactivation]* (x[C.feedback_pERK_on_AKT]* \
                x[C.init_pERK]+ x[C.feedback_pS6K1]* x[C.init_pS6K1]+ 1)))+ x[C.feedback_pERK]* y[V.pERK])

        v[95] = y[V.pMEK]* x[C.pMEK_dephosphorylation]

        v[96] = y[V.ERK]* x[C.ERK_phosphorylation_pMEK]* y[V.pMEK]
        v[97] = y[V.pERK]* x[C.pERK_dephosphorylation]
        
        ###AKT branch
        v[98] = (y[V.AKT]* x[C.AKT_activation_pEGFR]* y[V.pEGFRd])/(x[C.feedback_pERK_on_AKT]* y[V.pERK] + x[C.feedback_pS6K1]* y[V.pS6K1] + 1)
        v[99] = (y[V.AKT]* x[C.AKT_activation_pErbB12]* y[V.pErbB12])/(x[C.feedback_pERK_on_AKT]* y[V.pERK] + x[C.feedback_pS6K1]* y[V.pS6K1] + 1)
        v[100] = (y[V.AKT]* x[C.AKT_activation_pErbB13]* y[V.pErbB13])/(x[C.feedback_pERK_on_AKT]* y[V.pERK] + x[C.feedback_pS6K1]* y[V.pS6K1] + 1)
        v[101] = (y[V.AKT]* x[C.AKT_activation_pErbB32]* y[V.pErbB32])/(x[C.feedback_pERK_on_AKT]* y[V.pERK] + x[C.feedback_pS6K1]* y[V.pS6K1] + 1)
        v[102] = (y[V.AKT]* x[C.AKT_activation_pMetEGFR]* y[V.pMetEGFR])/(x[C.feedback_pERK_on_AKT]* y[V.pERK] + x[C.feedback_pS6K1]* y[V.pS6K1] + 1)
        v[103] = (y[V.AKT]* x[C.AKT_activation_pMetd]* y[V.pMetd])/(x[C.feedback_pERK_on_AKT]* y[V.pERK] + x[C.feedback_pS6K1]* y[V.pS6K1] + 1)
        v[104] = (y[V.AKT]* x[C.AKT_activation_pIGF1R]* y[V.pIGF1Rd])/(x[C.feedback_pERK_on_AKT]* y[V.pERK] + x[C.feedback_pS6K1]* y[V.pS6K1] + 1)
        v[105] = (y[V.AKT]* x[C.AKT_activation_pMetErbB3]* y[V.pMetErbB3])/(x[C.feedback_pERK_on_AKT]* y[V.pERK] + x[C.feedback_pS6K1]* y[V.pS6K1] + 1)
        v[106] = (y[V.AKT]* x[C.AKT_activation_pIGF1R]* x[C.AKT_internIGF1R_effect]* y[V.pIGF1Ri])/(x[C.feedback_pERK_on_AKT]* y[V.pERK] + x[C.feedback_pS6K1]* y[V.pS6K1] + 1)
        v[107] = y[V.pAKT]* x[C.pAKT_deactivation]

        ###GSK3-S6K-S6 
        v[108] = y[V.S6K1]* x[C.S6K1_phosphorylation_pAKT]* y[V.pAKT]
        v[109] = y[V.S6K1]* x[C.S6K1_phosphorylation_pERK]* y[V.pERK]
        v[110] = y[V.pS6K1]* x[C.pS6K1_dephosphorylation]

        v[111] = y[V.S6]* x[C.S6_phosphorylation_pS6K1]* y[V.pS6K1]
        v[112] = y[V.S6]* x[C.S6_phosphorylation_pERK]* y[V.pERK]
        v[113] = y[V.pS6]* x[C.pS6_dephosphorylation]

        #ODE of the law of the mass action
        dydt = [0]* V.NUM
        dydt[V.dose_EGF] = -v[6] + v[7]
        dydt[V.dose_HGF] = -v[14] + v[15]
        dydt[V.RTKph] = -v[43] + v[44] - v[47] + v[48] - v[53] + v[54] - v[58] + v[59] - v[63] + v[64] - v[67] + v[68] - v[71] + v[72] - v[75] + v[76] - v[80] + v[81] - v[84] + v[85] 
        dydt[V.dose_IGF1] = - v[12] + v[13]
        dydt[V.dose_HRG] = -v[10] + v[11]
        dydt[V.dose_BTC] = -v[8] + v[9]
        dydt[V.EGFR] = v[1] - v[6] + v[7] - v[8] + v[9] - 2*v[32] - v[35] - v[36] - v[40] + v[45]
        dydt[V.EGFR_EGF] = v[6] - v[7] - 2*v[16] - v[21] - v[23] - v[30]
        dydt[V.EGFR_BTC] = v[8] - v[9] - 2*v[17] - v[22] - v[24] - v[25] - v[31]
        dydt[V.pEGFRd] = v[16] + v[17] + v[32] - v[41]
        dydt[V.pEGFRi] = v[41] - v[42] - v[43]
        dydt[V.pEGFRi_ph] = v[43] - v[44]
        dydt[V.EGFRi] = +2*v[44] - v[45] + v[64] + v[72] + v[85]
        dydt[V.ErbB2] = v[2] - 2*v[18] - v[21] - v[22] - v[26] - v[35] - v[37] + v[50]
        dydt[V.pErbB2] = v[18] - v[46]
        dydt[V.pErbB2i] = v[46] - v[47] - v[49]
        dydt[V.ErbB2i] = +2*v[48] - v[50] + v[64] + v[68]
        dydt[V.pErbB2i_ph] = v[47] - v[48]
        dydt[V.pErbB12] = v[21] + v[22] + v[35] - v[61]
        dydt[V.pErbB12i] = v[61] - v[62] - v[63]
        dydt[V.pErbB12i_ph] = v[63] - v[64]
        dydt[V.ErbB3] = v[3] - v[10] + v[11] - v[25] - 2*v[33] - v[36] - v[37] - v[38] + v[55]
        dydt[V.ErbB3_HRG] = v[10] - v[11] - 2*v[19] - v[23] - v[24] - v[26] - v[28] - v[29]
        dydt[V.pErbB3d] = v[19] + v[33] - v[51]
        dydt[V.pErbB3i] = v[51] - v[52] - v[53]
        dydt[V.pErbB3i_ph] = v[53] - v[54]
        dydt[V.ErbB3i] = +2*v[54] - v[55] + v[68] + v[72] + v[81]
        dydt[V.pErbB13] = v[23] + v[24] + v[25] + v[36] - v[69]
        dydt[V.pErbB13i] = v[69] - v[70] - v[71]
        dydt[V.pErbB13i_ph] = v[71] - v[72]
        dydt[V.pErbB32] = v[26] + v[37] - v[65]
        dydt[V.pErbB32i] = v[65] - v[66] - v[67]
        dydt[V.pErbB32i_ph] = v[67] - v[68]
        dydt[V.IGF1R] = v[4] - v[12] + v[13] -2*v[34] + v[60]
        dydt[V.IGF1R_IGF1] = v[12] - v[13] -2*v[20]
        dydt[V.pIGF1Rd] = v[20] + v[34] - v[56]
        dydt[V.pIGF1Ri] = v[56] - v[57] - v[58]
        dydt[V.pIGF1Ri_ph] = v[58] - v[59]
        dydt[V.IGF1Ri] = +2*v[59 ] - v[60]
        dydt[V.Met] = v[5] - v[14] + v[15] - v[28] - v[38] - 2*v[39] - v[40] + v[77]
        dydt[V.Met_HGF] = v[14] - v[15] - 2*v[27] - v[29] - v[30] - v[31]
        dydt[V.pMetd] = v[27] + v[39] - v[73]
        dydt[V.pMeti] = v[73] - v[74] - v[75]
        dydt[V.pMeti_ph] = v[75] - v[76]
        dydt[V.Meti] = +2*v[76] - v[77] + v[81] + v[85]
        dydt[V.pMetErbB3] = v[28] + v[29] + v[38] - v[78]
        dydt[V.pMetErbB3i] = v[78] - v[79] - v[80]
        dydt[V.pMetErbB3i_ph] = v[80] - v[81]
        dydt[V.pMetEGFR] = v[30] + v[31] + v[40] - v[82]
        dydt[V.pMetEGFRi] = v[82] - v[83] - v[84]
        dydt[V.pMetEGFRi_ph] = v[84] - v[85]
        dydt[V.MEK] = -v[86] - v[87] - v[88] - v[89] - v[90] - v[91] - v[92] - v[93] - v[94] + v[95]
        dydt[V.pMEK] = v[86] + v[87] + v[88] + v[89] + v[90] + v[91] + v[92] + v[93] + v[94] - v[95]
        dydt[V.ERK] = -v[96] + v[97]
        dydt[V.pERK] = v[96] - v[97]
        dydt[V.AKT] = -v[98] - v[99] - v[100] - v[101] - v[102] - v[103] - v[104] - v[105] - v[106] + v[107]
        dydt[V.pAKT] = v[98] + v[99] + v[100] + v[101] + v[102] + v[103] + v[104] + v[105] + v[106] - v[107]
        dydt[V.S6K1] = -v[108] - v[109] + v[110]
        dydt[V.pS6K1] = v[108] + v[109] - v[110]
        dydt[V.S6] = -v[111] - v[112] + v[113]
        dydt[V.pS6] = v[111] + v[112] - v[113]

        return dydt

def param_values():
    x = [0]*C.NUM
    # 1-82
    
    x[C.AKT_activation_pEGFR] = 1.00*10**(-5) 
    x[C.AKT_activation_pErbB12] = 6.40*10**(-2) 
    x[C.AKT_activation_pErbB13] = 1.31*10**(1)
    x[C.AKT_activation_pErbB32] = 5.61*10**(-1)
    x[C.AKT_activation_pIGF1R] = 6.85*10**(-1)
    x[C.AKT_activatio_pMetEGFR] = 1.00*10**(-5)
    x[C.AKT_activation_pMetErbB3] = 3.70*10**(-2)
    x[C.AKT_activation_pMetd] = 8.96*10**(-1)
    x[C.AKT_internIGF1R_effect] = 1.02*10**(-5)
    x[C.EGFR_BTC_binding] = 2.24*10**(-5)
    x[C.EGFR_BTC_dimerize] = 1.00*10**(3)
    x[C.EGFR_ErbB2_BTC_dimerize] = 1.61*10**(0)
    x[C.EGFR_ErbB2_basal_act] = 1.00*10**(-5)
    x[C.EGFR_ErbB2_dimerize] = 1.57*10**(-2)
    x[C.EGFR_ErbB3_BTC_dimerize] = 3.52*10**(-2)
    x[C.EGFR_ErbB3_basal_act] = 7.51*10**(-4)
    x[C.EGFR_ErbB3_dimerize] = 1.18*10**(-3)
    x[C.EGFR_ErbB3_dimerize_noHRG] = 1.00*10**(-5)
    x[C.EGFR_basal_activation] = 1.00*10**(-5)
    x[C.EGFR_basal_recycle] = 5.19*10**(5)
    x[C.EGFR_dimerize] = 6.30*10**(-2)
    x[C.EGFR_lig_binding] = 1.89*10**(-5)
    x[C.EGF_kD] = 1.00*10**(0)
    x[C.ERK_phosphorylation_pMEK] = 2.58*10**(-4)
    x[C.ErbB2_ErbB3_dimerize] = 3.03*10**(-2)
    x[C.ErbB2_dimerize] = 6.79*10**(-3)
    x[C.ErbB2_recycle] = 6.57*10**(-3)
    x[C.ErbB3_ErbB2_basal_act] = 1.00*10**(-5)
    x[C.ErbB3_basal_activation] = 2.93*10**(-2)
    x[C.ErbB3_basal_recycle] = 7.37*10**(-1)
    x[C.ErbB3_dimerize] = 4.46*10**(-2)
    x[C.ErbB3_lig_binding] = 5.71*10**(-5)
    x[C.HGF_kD] = 3.00*10**(-1)
    x[C.HRG_kD] = 5.00*10**(-2)
    x[C.IGF1R_basal_activation] = 1.17*10**(-3)
    x[C.IGF1R_basal_recycle] = 1.00*10**(3)
    x[C.IGF1R_dimerize] = 1.71*10**(1)
    x[C.IGF1R_lig_binding] = 1.53*10**(-3)
    x[C.IGF1_kD] = 3.00*10**(-1)
    x[C.MEK_internIGF1R_effect] = 1.00*10**(-5)
    x[C.MEK_phosphorylation_pEGFR] = 1.00*10**(-5)
    x[C.MEK_phosphorylation_pErbB12] = 2.74*10**(-1)
    x[C.MEK_phosphorylation_pErbB13] = 1.00*10**(-5)
    x[C.MEK_phosphorylation_pErbB32] = 6.06*10**(-2)
    x[C.MEK_phosphorylation_pIGF1R] = 2.99*10**(-2)
    x[C.MEK_phosphorylation_pMetEGFR] = 1.00*10**(-5)
    x[C.MEK_phosphorylation_pMetErbB3] = 3.83*10**(-2)
    x[C.MEK_phosphorylation_pMetd] = 1.88*10**(0)
    x[C.Met_EGFR_BTC_dimerize] = 1.11*10**(-2)
    x[C.Met_EGFR_basal_act] = 1.75*10**(-5)
    x[C.Met_EGFR_dimerize] = 5.13*10**(-4)
    x[C.Met_ErbB3_basal_act] = 3.29*10**(0)
    x[C.Met_ErbB3_dimerize] = 3.71*10**(-2)
    x[C.Met_basal_act] = 1.00*10**(-5)
    x[C.Met_dimerize] = 9.17*10**(-3)
    x[C.Met_lig_ErbB3_dimerize] = 5.67*10**(2)
    x[C.Met_lig_binding] = 4.52*10**(-3)
    x[C.Met_recycle] = 5.42*10**(-1)
    x[C.S6K1_phosphorylation_pAKT] = 2.50*10**(-1)
    x[C.S6K1_phosphorylation_pERK] = 1.07*10**(-5)
    x[C.S6_phosphorylation_pERK] = 1.00*10**(-5) #
    x[C.S6_phosphorylation_pS6K1] = 8.57*10**(-3) #
    x[C.feedback_pAKT] = 1.06*10**(-5)
    x[C.feedback_pERK] = 1.00*10**(3)
    x[C.feedback_pERK_on_AKT] = 1.00*10**(-5)
    x[C.feedback_pS6K1] = 2.09*10**(-5)
    x[C.init_AKT] = 2.71*10**(0)
    x[C.init_EGFR] = 1.79*10**(1)
    x[C.init_EGFR_BTC] = 0.00*10**(0)
    x[C.init_EGFR_EGF] = 0.00*10**(0)
    x[C.init_ErbB2] = 5.70*10**(0)
    x[C.init_ErbB3] = 2.48*10**(0)
    x[C.init_ErbB3_HRG] = 0.00*10**(0)
    x[C.init_IGF1R] = 4.73*10**(0)
    x[C.init_IGF1R_IGF1] = 0.00*10**(0)
    x[C.init_MEK] = 4.24*10**(0)
    x[C.init_Met] = 7.90*10**(0)
    x[C.init_Met_HGF] = 0.00*10**(0)
    x[C.init_RTKph] = 6.19*10**(-1)
    x[C.init_S6] = 1.46*10**(2)
    x[C.init_pERK] = 3.34*10**(-1)
    x[C.init_pS6K1] = 1.24*10**(-3)

    #251-326
    x[C.pAKT_deactivation] = 3.03*10**(-1)
    x[C.pEGFR_degradation] = 1.00*10**(-5)
    x[C.pEGFR_internalize] = 6.23*10**(0)
    x[C.pEGFR_phosphatase_binding] = 1.85*10**(2)
    x[C.pEGFRi_dephosph] = 2.17*10**(1)
    x[C.pERK_dephosphorylation] = 5.43*10**(-1)
    x[C.pErbB12_degradation] = 1.82*10**(-1)
    x[C.pErbB12_internalize] = 1.90*10**(0)
    x[C.pErbB12i_dephosph] = 1.00*10**(3)
    x[C.pErbB12i_phosphatase] = 8.45*10**(-1)
    x[C.pErbB13_degradation] = 4.97*10**(1)
    x[C.pErbB13_internalize] = 1.00*10**(3)
    x[C.pErbB13i_dephosph] = 5.84*10**(1)
    x[C.pErbB13i_phosphatase] = 1.60*10**(-5)
    x[C.pErbB2_degradation] = 3.19*10**(2)
    x[C.pErbB2_internalize] = 1.00*10**(3)
    x[C.pErbB2i_dephosph] = 8.24*10**(0)
    x[C.pErbB2i_phosphatase] = 1.00*10**(3)
    x[C.pErbB32_degradation]  = 5.74*10**(-1)
    x[C.pErbB32_internalize] = 1.09*10**(0)
    x[C.pErbB32i_dephosph] = 1.19*10**(-2)
    x[C.pErbB32i_phosphatase] = 4.88*10**(-2)
    x[C.pErbB3_degradation] = 9.08*10**(-1)
    x[C.pErbB3_internalize] = 1.00*10**(3)
    x[C.pErbB3i_dephosph] = 1.63*10**(1)
    x[C.pErbB3i_phosphatase] = .22*10**(1)
    x[C.pIGF1R_degradation] = 1.00*10**(-5)
    x[C.pIGF1R_internalize] = 1.00*10**(3)
    x[C.pIGF1Ri_dephosph] = 3.32*10**(2)
    x[C.pIGF1Ri_phosphatase] = 1.00*10**(3)
    x[C.pMEK_dephosphorylation] = 3.28*10**(-1)
    x[C.pMetEGFR_degradation] = 1.43*10**(0)
    x[C.pMetEGFR_internalize] = 1.33*10**(0)
    x[C.pMetEGFRi_dephosph] = 5.04*10**(-1)
    x[C.pMetEGFRi_phosphatase] = 3.57*10**(-5)
    x[C.pMetErbB3_degradation] = 9.84*10**(2)
    x[C.pMetErbB3_internalize] = 1.00*10**(3)
    x[C.pMetErbB3i_dephosph] = 1.00*10**(3)
    x[C.pMetErbB3i_phosphatase] = 1.00*10**(3)
    x[C.pMet_degradation] = 1.91*10**(0)
    x[C.pMet_internalize] = 1.00*10**(3)
    x[C.pMeti_dephosph] = 1.30*10**(1)
    x[C.pMeti_phosphatase] = 1.00*10**(3)
    x[C.pS6K1_dephosphorylation] = 1.03*10**(-2)
    x[C.pS6_dephosphorylation] = 1.19*10**(-1) #
    x[C.relto_A431_init_EGFR] = 9.63*10**(0)
    x[C.relto_A431_init_ErbB2] = 1.00*10**(0)
    x[C.relto_A431_init_ErbB3] = 9.11*10**(-1)
    x[C.relto_A431_init_IGF1R] = 2.65*10**(0)
    x[C.relto_A431_init_Met] = 2.24*10**(-1)
    x[C.relto_ACHN_init_EGFR] = 5.40*10**(0)
    x[C.relto_ACHN_init_ErbB2] = 7.33*10**(-1)
    x[C.relto_ACHN_init_ErbB3] = 4.46*10**(-1)
    x[C.relto_ACHN_init_IGF1R] = 7.03*10**(-1)
    x[C.relto_ACHN_init_Met] = 1.29*10**(0)
    x[C.relto_ADRr_init_EGFR] = 1.03*10**(0)
    x[C.relto_ADRr_init_ErbB2] = 1.07*10**(0)
    x[C.relto_ADRr_init_ErbB3] = 5.74*10**(-1)
    x[C.relto_ADRr_init_IGF1R] = 2.02*10**(0)
    x[C.relto_ADRr_init_Met] = 4.82*10**(-1)
    x[C.relto_BT20_init_EGFR] = 1.05*10**(1)
    x[C.relto_BT20_init_ErbB2] = 1.50*10**(0)
    x[C.relto_BT20_init_ErbB3] = 1.85*10**(0)
    x[C.relto_BT20_init_IGF1R] = 3.55*10**(0)
    x[C.relto_BT20_init_Met] = 3.82*10**(-1)
    x[C.relto_IGROV_init_EGFR] = 9.41*10**(-1)
    x[C.relto_IGROV_init_ErbB2] = 4.25*10**(0)
    x[C.relto_IGROV_init_ErbB3] = 5.76*10**(-1)
    x[C.relto_IGROV_init_IGF1R] = 1.59*10**(-1)
    x[C.relto_IGROV_init_Met] = 6.42*10**(-1)
    x[C.relto_init_EGFR] = 1.83*10**(0)
    x[C.relto_init_ErbB2] = 6.07*10**(-1)
    x[C.relto_init_ErbB3] = 1.04*10**(0)
    x[C.relto_init_IGF1R] = 1.48*10**(0)
    x[C.relto_init_Met] = 1.80*10**(0)
    x[C.scale_Ligand] = 3.78*10**(4)   

    #scale
    x[C.scale_pAKT_CelllineA431] = 7.83*10**(0)
    x[C.scale_pAKT_CelllineACHN_197] = 3.44*10**(4)
    x[C.scale_pAKT_CelllineACHN_200] = 5.18*10**(5)
    x[C.scale_pAKT_CelllineACHN_218] = 1.35*10**(3)
    x[C.scale_pAKT_CelllineACHN_DM] = 1.62*10**(5)
    x[C.scale_pAKT_CelllineADRr] = 1.31*10**(1)
    x[C.scale_pAKT_CelllineADRr_B] = 5.65*10**(3)
    x[C.scale_pAKT_CelllineADRr_B2] = 4.18*10**(2)
    x[C.scale_pAKT_CelllineBT20] = 4.38*10**(0)
    x[C.scale_pAKT_CelllineBxPc3] = 9.87*10**(-1)
    x[C.scale_pAKT_CelllineH322M] = 7.14*10**(-1)
    x[C.scale_pAKT_CelllineIGROV1] = 1.24*10**(1)
    x[C.scale_pEGFR_CelllineA431] = 7.89*10**(2)
    x[C.scale_pEGFR_CelllineACHN_197] = 9.71*10**(4)
    x[C.scale_pEGFR_CelllineACHN_200] = 3.13*10**(-1)
    x[C.scale_pEGFR_CelllineACHN_218] = 1.72*10**(-4)
    x[C.scale_pEGFR_CelllineACHN_DM] = 1.43*10**(4)
    x[C.scale_pEGFR_CelllineADRr] = 7.54*10**(-1)
    x[C.scale_pEGFR_CelllineADRr_B] = 1.41*10**(3)
    x[C.scale_pEGFR_CelllineADRr_B2] = 1.90*10**(2)
    x[C.scale_pEGFR_CelllineBT20] = 1.39*10**(3)
    x[C.scale_pEGFR_CelllineBxPc3] = 2.45*10**(1)
    x[C.scale_pEGFR_CelllineH322M] = 3.30*10**(1)
    x[C.scale_pEGFR_CelllineIGROV1] = 5.01*10**(3)
    x[C.scale_pERK_CelllineA431] = 4.18*10**(-1)
    x[C.scale_pERK_CelllineACHN_197] = 3.40*10**(4)
    x[C.scale_pERK_CelllineACHN_200] = 9.02*10**(4)
    x[C.scale_pERK_CelllineACHN_218] = 3.33*10**(4)
    x[C.scale_pERK_CelllineACHN_DM] = 4.58*10**(4)
    x[C.scale_pERK_CelllineADRr] =  8.92*10**(-1)
    x[C.scale_pERK_CelllineADRr_B] = 5.76*10**(3)
    x[C.scale_pERK_CelllineADRr_B2] = 2.26*10**(2)
    x[C.scale_pERK_CelllineBT20] = 5.72*10**(-1)
  
    x[C.scale_pERK_CelllineBxPc3] = 9.12*10**(-1)
    x[C.scale_pERK_CelllineH322M] = 3.85*10**(-1)
    x[C.scale_pERK_CelllineIGROV1] = 5.80*10**(-1)
    x[C.scale_pErbB2_CelllineA431] = 8.48*10**(2)
    x[C.scale_pErbB2_CelllineACHN_197] = 3.89*10**(5)
    x[C.scale_pErbB2_CelllineACHN_200] = 3.97*10**(-2)
    x[C.scale_pErbB2_CelllineACHN_218] = 2.82*10**(5)
    x[C.scale_pErbB2_CelllineACHN_DM] = 2.11*10**(3)
    x[C.scale_pErbB2_CelllineADRr] = 6.91*10**(2)
    x[C.scale_pErbB2_CelllineADRr_B] = 2.08*10**(3)
    x[C.scale_pErbB2_CelllineADRr_B2] = 8.00*10**(1)
    x[C.scale_pErbB2_CelllineBT20] = 2.97*10**(2)
    x[C.scale_pErbB2_CelllineBxPc3] = 3.79*10**(0)
    x[C.scale_pErbB2_CelllineH322M] = 5.27*10**(0)
    x[C.scale_pErbB2_CelllineIGROV1] = 6.37*10**(2)
    x[C.scale_pErbB3_CelllineA431] = 1.54*10**(3)
    x[C.scale_pErbB3_CelllineACHN_197] = 1.71*10**(3)
    x[C.scale_pErbB3_CelllineACHN_200] = 5.63*10**(-1)
    x[C.scale_pErbB3_CelllineACHN_218] = 3.95*10**(5)
    x[C.scale_pErbB3_CelllineACHN_DM] = 1.75*10**(-3)
    x[C.scale_pErbB3_CelllineADRr] = 1.02*10**(3)
    x[C.scale_pErbB3_CelllineADRr_B] = 6.75*10**(2)
    x[C.scale_pErbB3_CelllineADRr_B2] = 1.31*10**(-4)
    x[C.scale_pErbB3_CelllineBT20] = 5.42*10**(2)
    x[C.scale_pErbB3_CelllineBxPc3] = 2.76*10**(-1)
    x[C.scale_pErbB3_CelllineH322M] = 2.71*10**(0)
    x[C.scale_pErbB3_CelllineIGROV1] = 1.82*10**(1)
    x[C.scale_pIGF1R_CelllineA431] = 1.10*10**(3)
    x[C.scale_pIGF1R_CelllineACHN_197] = 6.62*10**(2)
    x[C.scale_pIGF1R_CelllineACHN_200] = 4.54*10**(2)
    x[C.scale_pIGF1R_CelllineACHN_218] = 2.31*10**(-4)
    x[C.scale_pIGF1R_CelllineACHN_DM] = 1.05*10**(1)
    x[C.scale_pIGF1R_CelllineADRr] = 1.97*10**(2)
    x[C.scale_pIGF1R_CelllineADRr_B] = 1.44*10**(-2)
    x[C.scale_pIGF1R_CelllineADRr_B2] = 2.17*10**(5)
    x[C.scale_pIGF1R_CelllineBT20] = 9.08*10**(1)
    x[C.scale_pIGF1R_CelllineBxPc3] = 3.43*10**(2)
    x[C.scale_pIGF1R_CelllineH322M] = 1.19*10**(4)
    x[C.scale_pIGF1R_CelllineIGROV1] = 2.35*10**(3)
    x[C.scale_pMEK_CelllineA431] = 2.20*10**(3)
    x[C.scale_pMEK_CelllineACHN_197] = 2.14*10**(-4)
    x[C.scale_pMEK_CelllineACHN_200] = 6.79*10**(-4)
    x[C.scale_pMEK_CelllineACHN_218] = 2.06*10**(1)
    x[C.scale_pMEK_CelllineACHN_DM] = 6.92*10**(0)
    x[C.scale_pMEK_CelllineADRr] = 6.76*10**(-4)

    x[C.scale_pMEK_CelllineADRr_B] = 4.70*10**(2)
    x[C.scale_pMEK_CelllineADRr_B2] = 2.51*10**(3)
    x[C.scale_pMEK_CelllineBT20] = 3.66*10**(3)
    x[C.scale_pMEK_CelllineBxPc3] = 1.34*10**(3)
    x[C.scale_pMEK_CelllineH322M] = 3.51*10**(2)
    x[C.scale_pMEK_CelllineIGROV1] = 7.66*10**(3)
    x[C.scale_pMet_CelllineA431] = 6.41*10**(-3)
    x[C.scale_pMet_CelllineACHN_197] = 2.83*10**(3)
    x[C.scale_pMet_CelllineACHN_200] = 2.52*10**(3)
    x[C.scale_pMet_CelllineACHN_218] = 1.24*10**(3)
    x[C.scale_pMet_CelllineACHN_DM] = 8.92*10**(3)
    x[C.scale_pMet_CelllineADRr] = 9.16*10**(0)
    x[C.scale_pMet_CelllineADRr_B] = 1.52*10**(-2)
    x[C.scale_pMet_CelllineADRr_B2] = 6.40*10**(-2)
    x[C.scale_pMet_CelllineBT20] = 9.33*10**(-4)
    x[C.scale_pMet_CelllineBxPc3] = 4.84*10**(3)
    x[C.scale_pMet_CelllineH322M] = 6.53*10**(-3)
    x[C.scale_pMet_CelllineIGROV1] = 3.61*10**(-4)
    x[C.scale_pS6K1_CelllineA431] = 5.92*10**(-1)
    x[C.scale_pS6K1_CelllineACHN_197] = 4.40*10**(5)
    x[C.scale_pS6K1_CelllineACHN_200] = 3.76*10**(-4)
    x[C.scale_pS6K1_CelllineACHN_218] = 1.71*10**(4)
    x[C.scale_pS6K1_CelllineACHN_DM] = 1.63*10**(-1)
    x[C.scale_pS6K1_CelllineADRr] = 1.39*10**(1)
    x[C.scale_pS6K1_CelllineADRr_B] = 4.00*10**(5)
    x[C.scale_pS6K1_CelllineADRr_B2] = 1.14*10**(0)
    x[C.scale_pS6K1_CelllineBT20] = 6.97*10**(4)
    x[C.scale_pS6K1_CelllineBxPc3] = 4.69*10**(2)
    x[C.scale_pS6K1_CelllineH322M] = 3.22*10**(2)
    x[C.scale_pS6K1_CelllineIGROV1] = 6.14*10**(3)
    x[C.scale_pS6_CelllineA431] = 5.45*10**(2)
    x[C.scale_pS6_CelllineACHN_197] = 2.75*10**(2)
    x[C.scale_pS6_CelllineACHN_200] = 4.86*10**(3)
    x[C.scale_pS6_CelllineACHN_218] = 2.30*10**(5)
    x[C.scale_pS6_CelllineACHN_DM] = 6.14*10**(4)
    x[C.scale_pS6_CelllineADRr] = 3.48*10**(2)
    x[C.scale_pS6_CelllineADRr_B] = 5.72*10**(4)
    x[C.scale_pS6_CelllineADRr_B2] = 1.70*10**(0)
    x[C.scale_pS6_CelllineBT20] = 2.40*10**(2)
    x[C.scale_pS6_CelllineBxPc3] = 4.10*10**(1)
    x[C.scale_pS6_CelllineH322M] = 2.65*10**(1)
    x[C.scale_pS6_CelllineIGROV1] = 2.33*10**(2)
    x[C.scale_tEGFR_CelllineA431] = 1.16*10**(2)
    x[C.scale_tEGFR_CelllineACHN_197] = 1.64*10**(-2)
    x[C.scale_tEGFR_CelllineACHN_200] = 3.71*10**(-2)
    x[C.scale_tEGFR_CelllineACHN_218] = 2.02*10**(5)
    x[C.scale_tEGFR_CelllineACHN_DM] = 2.42*10**(3)
    x[C.scale_tEGFR_CelllineADRr] = 8.24*10**(-4)
    x[C.scale_tEGFR_CelllineADRr_B] = 2.47*10**(5)
    x[C.scale_tEGFR_CelllineADRr_B2] = 2.04*10**(4)
    x[C.scale_tEGFR_CelllineBT20] = 8.20*10**(0)
    x[C.scale_tEGFR_CelllineBxPc3] = 8.62*10**(-1)
    x[C.scale_tEGFR_CelllineH322M] = 7.91*10**(-1)
    x[C.scale_tEGFR_CelllineIGROV1] = 2.57*10**(1)
    x[C.scale_tErbB2_CelllineA431] = 1.67*10**(1)
    x[C.scale_tErbB2_CelllineACHN_197] = 1.70*10**(5)
    x[C.scale_tErbB2_CelllineACHN_200] = 4.55*10**(3)
    x[C.scale_tErbB2_CelllineACHN_218] = 2.84*10**(-4)
    x[C.scale_tErbB2_CelllineACHN_DM] = 3.45*10**(1)
    x[C.scale_tErbB2_CelllineADRr] = 2.00*10**(0)
    x[C.scale_tErbB2_CelllineADRr_B] = 7.73*10**(3)
    x[C.scale_tErbB2_CelllineADRr_B2] = 3.40*10**(4)
    x[C.scale_tErbB2_CelllineBT20] = 7.52*10**(0)
    x[C.scale_tErbB2_CelllineBxPc3] = 1.00*10**(-4)
    x[C.scale_tErbB2_CelllineH322M] = 1.00*10**(-4)
    x[C.scale_tErbB2_CelllineIGROV1] = 9.41*10**(-1)
    x[C.scale_tErbB3_CelllineA431] = 4.57*10**(-4)
    x[C.scale_ErbB3_CelllineACHN_197] = 3.67*10**(3)
    x[C.scale_tErbB3_CelllineACHN_200] = 4.08*10**(0)
    x[C.scale_tErbB3_CelllineACHN_218] = 9.14*10**(-2)
    x[C.scale_tErbB3_CelllineACHN_DM] = 9.27*10**(1)
    x[C.scale_tErbB3_CelllineADRr] = 1.25*10**(0)
    x[C.scale_tErbB3_CelllineADRr_B] = 6.25*10**(1)
    x[C.scale_tErbB3_CelllineADRr_B2] = 1.15*10**(-2)
    x[C.scale_tErbB3_CelllineBT20] = 9.93*10**(-2)
    x[C.scale_tErbB3_CelllineBxPc3] = 5.74*10**(-4)
    x[C.scale_tErbB3_CelllineH322M] = 3.69*10**(-4)
    x[C.scale_tErbB3_CelllineIGROV1] = 4.18*10**(-1)
    x[C.scale_tIGF1R_CelllineA431] = 2.26*10**(1)
    x[C.scale_tIGF1R_CelllineACHN_197] = 3.70*10**(5)
    x[C.scale_tIGF1R_CelllineACHN_200] = 6.73*10**(0)
    x[C.scale_tIGF1R_CelllineACHN_218] = 2.35*10**(3)
    x[C.scale_tIGF1R_CelllineACHN_DM] = 2.39*10**(3)
    x[C.scale_tIGF1R_CelllineADRr] = 2.03*10**(1)
    x[C.scale_tIGF1R_CelllineADRr_B] = 1.63*10**(1)
    x[C.scale_tIGF1R_CelllineADRr_B2] = 2.51*10**(0)
    x[C.scale_tIGF1R_CelllineBT20] = 1.08*10**(1)
    x[C.scale_tIGF1R_CelllineBxPc3] = 1.70*10**(-5)
    x[C.scale_tIGF1R_CelllineH322M] = 2.17*10**(0)
    x[C.scale_tIGF1R_CelllineIGROV1] = 1.45*10**(1)
    
    

    #offset
    x[C.offset_tEGFR_CelllineH322M] = 1.46*10**(0) 
    x[C.offset_tErbB2_CelllineH322M] = 7.91*10**(0)  
    x[C.offset_tErbB3_CelllineH322M] = 7.86*10**(-1)
    x[C.offset_tIGF1R_CelllineH322M] = 4.21*10**(-2) 
    x[C.offset_pEGFR_CelllineH322M] = 4.90*10**(0) 
    x[C.offset_pErbB2_CelllineH322M] = 1.09*10**(0)
    x[C.offset_pErbB3_CelllineH322M] = 1.00*10**(-5) 
    x[C.offset_pIGF1R_CelllineH322M] = 4.07*10**(2) 
    x[C.offset_pMet_CelllineH322M] = 3.14*10**(-2) 
    x[C.offset_pMEK_CelllineH322M] = 1.37*10**(-1) 
    x[C.offset_pERK_CelllineH322M] = 1.00*10**(-7)
    x[C.offset_pAKT_CelllineH322M] = 1.87*10**(-1)
    x[C.offset_pS6K1_CelllineH322M] = 1.00*10**(-7) 
    x[C.offset_pS6_CelllineH322M] = 1.00*10**(-7) 
    


    return x


def initial_values():
    y0 = [0]*V.NUM
    
    y0[V.dose_EGF] = 0.0
    y0[V.dose_HGF] = 0.0
    y0[V.RTKph] = 0.618911491797731 
    y0[V.dose_IGF1] = 0.0
    y0[V.dose_HRG] = 0.0
    y0[V.dose_BTC] = 0.0
    y0[V.EGFR] = 17.8621933083143 
    y0[V.EGFR_EGF] = 0.0
    y0[V.EGFR_BTC] = 0.0
    
    
    y0[V.pEGFRd] = 5.12011130278668E-4
    y0[V.pEGFRi] = 2.79223720669219E-5
    y0[V.pEGFRi_ph] = 1.4687856601509E-4
    y0[V.EGFRi] = 1.37508187561569E-8 
    
    y0[V.ErbB2] = 5.70185166249099
    
    
    y0[V.pErbB2] = 2.20826262632109E-4 
    y0[V.pErbB2i] = 2.35511421879916E-4
    y0[V.ErbB2i] = 44.4835113645705
    y0[V.pErbB2i_ph] = 0.0176807431775487 
    y0[V.pErbB12] = 5.37306859494303E-4 
    y0[V.pErbB12i] = 0.00144471037537624
    y0[V.pErbB12i_ph] = 7.55785246775258E-7
    
    y0[V.ErbB3] = 2.47992342696256
    y0[V.ErbB3_HRG] = 0.0
    
    
    y0[V.pErbB3d] = 1.8018926279905E-4
    y0[V.pErbB3i] =  0.00348026782363202
    y0[V.pErbB3i_ph] =  0.0108514486150842
    y0[V.ErbB3i] = 34.3224209878038
    y0[V.pErbB13] = 3.32712466211581E-5
    y0[V.pErbB13i] = 6.69142208681604E-4
    y0[V.pErbB13i_ph] = 1.13074197411592E-10
    y0[V.pErbB32] = 1.30059969850016E-4
    y0[V.pErbB32i] = 2.34208535412277E-4
    y0[V.pErbB32i_ph] = 5.93238579976826E-4
    
    y0[V.IGF1R] = 4.73494621402554
    y0[V.IGF1R_IGF1] = 0.0
    
    y0[V.pIGF1Rd] = 2.6239258403409E-5
    y0[V.pIGF1Ri] = 4.2395816408642E-5
    y0[V.pIGF1Ri_ph] = 7.91085256809129E-5
    y0[V.IGF1Ri] = 5.24785159589016E-5
    
    y0[V.Met] = 7.90290414461229
    y0[V.Met_HGF] = 0.0
  
    y0[V.pMetd] = 6.24560598662565E-7
    y0[V.pMeti] = 1.0060257690714E-6
    y0[V.pMeti_ph] = 4.79508059771836E-5
    y0[V.Meti] = 45.960014100956
    y0[V.pMetErbB3] = 0.0645520569171923
    y0[V.pMetErbB3i] = 0.0402793824584546
    y0[V.pMetErbB3i_ph] = 0.0249293726860515
    y0[V.pMetEGFR] = 0.00185677841647765 
    y0[V.pMetEGFRi] = 0.00172863499055847
    y0[V.pMetEGFRi_ph] = 7.58806259570584E-8
   
    y0[V.MEK] = 4.2412663925898 
    
    y0[V.pMEK] = 1.014543757693E-4
    y0[V.ERK] = 6922167.20947519
   

    y0[V.pERK] = 0.334274838149849 #
    
    y0[V.AKT] = 2.70857345464684
    y0[V.pAKT] = 0.0263677143207646
    y0[V.S6K1] = 0.00194894402116983
    
    y0[V.pS6K1] = 0.00124327830478657 #
    y0[V.S6] = 145.50079875804 #
    
    y0[V.pS6] = 0.0171533722671392 #
    
    
    return y0

    
''''
# call class
if __name__ == '__main__':
    D = DifferentialEquation(3) #create new instance
    print(D.pertubation)
'''
