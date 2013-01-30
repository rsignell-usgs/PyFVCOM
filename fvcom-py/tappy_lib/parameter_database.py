
letter_to_factor_map = {'Z':0,
                        'Y':-1,
                        'X':-2,
                        'W':-3,
                        'V':-4,
                        'U':-5,
                        'T':-6,
                        'A':1,
                        'B':2,
                        'C':3,
                        'D':4,
                        'E':5,
                        'F':6,
                        'G':7,
                        'H':8,
                        'I':9,
                        'J':10,
                        'K':11,
                        'L':12,
                        'M':13,
                        'N':14,
                       }


import math as m
def _m1b(p, N):
    A = 2.783*m.sin(2*p) + 0.558*m.sin(2*p - N) + 0.184*m.sin(N)
    B = 1 + A
    f = (A**2 + B**2)**0.5
    u = m.asin(A/f)
    return (u, f)

_master_speed_dict = {
'Zo': {
       'edn':'ZZZZZZZ',
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# Why are there 2 Sa constituents in the Proudman database?
# Very close speeds.
'Sa_': {
       'edn':'ZZAZZYZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# This is the one also used by Flater.
'Sa': {
       'edn':'ZZAZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'Ssa': {
       'edn':'ZZBZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'Sta': {
       'edn':'ZZCZZYY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# MSm is duplicate of
#  'Mnum': 'ZAXAZZZ', 
  'MSm':  {
         'edn':'ZAXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':['Mnum'],
      }, 
'Mm': {
       'edn':'ZAZYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# MSf duplicate of
#  'MSo': 'ZBXZZZZ', 
  'MSf': {
       'edn':'ZBXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# SM has same speeds as above but different nodal and u factors
  'SM': {
      'edn':'ZBXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'Mf':  {
         'edn':'ZBZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'KOo': 'ZBZZZZZ', 
#  'MKo': 'ZBZZZZZ', 
'Snu2': {
       'edn':'ZCVAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'SN': {
       'edn':'ZCXYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MStm': {
       'edn':'ZCXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'Mfm': {
       'edn':'ZCZYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':['A7'],
      }, 
'2SM': {
       'edn':'ZDVZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MSqm': {
       'edn':'ZDXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'Mqm': {
       'edn':'ZDZXZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2SMN': {
       'edn':'ZEVYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  '2Q1': {
         'edn':'AWZBZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'NJ1': 'AWZBZZY', 
# duplicate
  'nuJ1':   {
         'edn':'AWBZZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'sigma1': 'AWBZZZY', 
'Q1': {
       'edn':'AXZAZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'NK1': {
       'edn':'AXZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'rho1': {
         'edn':'AXBYZZY', 
       'u':0.0,
       'f':1.0,
       'aka':['rho'],
      }, 
#  'nuK1': 'AXBYZZY', 
# duplicate
  'O1':  {
         'edn':'AYZZZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'MK1': 'AYZZZZY', 
'MS1': {
       'edn':'AYAZZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MP1': {
       'edn':'AYBZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'MP1':  {
         'edn':'AYBZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'tau1': 'AYBZZZA', 
'M1B': {
       'edn':'AZZYZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'M1B': {
       'edn':'AZZYZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'M1C': {
       'edn':'AZZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'M1': {
       'edn':'AZZZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'M1': {
       'edn':'AZZZZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'NO1': {
         'edn':'AZZAZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'M1A': 'AZZAZZA', 
#  'M1':  'AZZAZZA', 
'LP1': {
       'edn':'AZBYZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'chi1': {
       'edn':'AZBYZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'pi1': {
         'edn':'AAWZZAY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'TK1': 'AAWZZAY', 
'P1': {
       'edn':'AAXZZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'SK1': {
       'edn':'AAXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'S1': {
       'edn':'AAYZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#'S1': {
#       'edn':'AAYZZZB', 
#       'u':0.0,
#       'f':1.0,
#       'aka':[],
#      }, 
#'S1': {
#       'edn':'AAYZZAA', 
#       'u':0.0,
#       'f':1.0,
#       'aka':[],
#      }, 
# duplicate
  'SP1': {
         'edn':'AAZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'K1':  'AAZZZZZ', 
#  'MO1': 'AAZZZZZ', 
'K1': {
       'edn':'AAZZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'RP1': {
       'edn':'AAAZZYY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'psi1': {
       'edn':'AAAZZYA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'phi1': {
         'edn':'AABZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'KP1':  'AABZZZA', 
'lambdaO1': {
       'edn':'ABXAZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'theta1': {
       'edn':'ABXAZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MQ1': {
       'edn':'ABZYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'J1': {
       'edn':'ABZYZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2PO1': {
       'edn':'ACVZZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'SO1': {
       'edn':'ACXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'SO1': {
       'edn':'ACXZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'OO1': {
       'edn':'ACZZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'ups1': {
         'edn':'ADZYZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'KQ1':  'ADZYZZA', 
'2MN2S2': {
       'edn':'BUDAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  '3M(SK)2': {
         'edn':'BVBZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  '3MKS2':   'BVBZZZZ', 
'2NS2': {
       'edn':'BVBBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  '3M2S2': {
         'edn':'BVDZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  '3MS2':  'BVDZZZZ', 
'2NK2S2': {
       'edn':'BVDBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'OQ2':  {
         'edn':'BWZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'MNK2': 'BWZAZZZ', 
'OQ2': {
       'edn':'BWZAZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'MNS2': {
         'edn':'BWBAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'eps2': 'BWBAZZZ', 
'MnuS2': {
       'edn':'BWDYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2ML2S2': {
       'edn':'BWDYZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MNK2S2': {
       'edn':'BWDAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MS2K2': {
       'edn':'BXXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  '2MK2': {
         'edn':'BXZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'O2':   'BXZZZZZ', 
'NLK2': {
       'edn':'BXZZZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2N2': {
       'edn':'BXZBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'mu2':  {
         'edn':'BXBZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  '2MS2': 'BXBZZZZ', 
'SNK2': {
       'edn':'BYXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'NA2': {
       'edn':'BYYAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'NA2': {
       'edn':'BYYAZAZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'N2':  {
         'edn':'BYZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'KQ2': 'BYZAZZZ', 
'NB2': {
       'edn':'BYAAZYZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'NA2*': {
       'edn':'BYAAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'nu2': {
       'edn':'BYBYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2KN2S2': {
       'edn':'BYDAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MSK2': {
       'edn':'BZXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'OP2': {
       'edn':'BZXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'OP2': {
       'edn':'BZXZZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'gamma2': {
       'edn':'BZXBZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MA2': {
       'edn':'BZYZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MPS2': {
       'edn':'BZYZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'alpha2': {
         'edn':'BZYZZAB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'M(SK)2': 'BZYZZAB', 
# duplicate
  'M2':  {
         'edn':'BZZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'KO2': 'BZZZZZZ', 
'M(KS)2': {
       'edn':'BZAZZYZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MSP2': {
       'edn':'BZAZZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'MB2':  {
         'edn':'BZAZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'MA2*': 'BZAZZZZ', 
# duplicate
  'MKS2':   {
         'edn':'BZBZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
  'delta2': {
         'edn':'BZBZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'M2(KS)2': {
         'edn':'BZDZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  '2KM2S2':  'BZDZZZZ', 
'2SN(MK)2': {
       'edn':'BAVAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'lambda2': {
       'edn':'BAXAZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'L2': {
         'edn':'BAZYZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  '2MN2': 'BAZYZZB', 
'L2A': {
       'edn':'BAZYZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'L2B':  {
         'edn':'BAZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'NKM2': 'BAZAZZZ', 
'2SK2': {
       'edn':'BBVZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'T2': {
       'edn':'BBWZZAZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'S2':  {
         'edn':'BBXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'KP2': 'BBXZZZZ', 
'R2': {
       'edn':'BBYZZYB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'K2': {
       'edn':'BBZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MSnu2': {
       'edn':'BCVAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MSN2': {
       'edn':'BCXYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'xi2': {
       'edn':'BCXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'eta2': {
       'edn':'BCZYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'KJ2': {
       'edn':'BCZYZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2KM(SN)2': {
       'edn':'BCBYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2SM2': {
       'edn':'BDVZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MS2N2': {
       'edn':'BDXXZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'SKM2': {
       'edn':'BDXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  '2Snu2':   {
         'edn':'BETAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  '3(SM)N2': 'BETAZZZ', 
'2SN2': {
       'edn':'BEVYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'SKN2': {
       'edn':'BEXYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3S2M2': {
       'edn':'BFTZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2SK2M2': {
       'edn':'BFVZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'MQ3': {
         'edn':'CXZAZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'NO3': 'CXZAZZY', 
# duplicate
  'MQ3': {
         'edn':'CXZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
  'NO3': {
         'edn':'CXZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'MO3': {
         'edn':'CYZZZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  '2MK3': 'CYZZZZY', 
'MO3': {
       'edn':'CYZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2NKM3': {
       'edn':'CYZBZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MS3': {
       'edn':'CYAZZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MP3': {
       'edn':'CYBZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'M3': {
       'edn':'CZZZZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'NK3': {
       'edn':'CZZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'NK3': {
       'edn':'CZZAZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'SO3': {
         'edn':'CAXZZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'MP3': 'CAXZZZY', 
'MP3': {
       'edn':'CAXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MS3': {
       'edn':'CAYZZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MK3': {
       'edn':'CAZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MK3': {
       'edn':'CAZZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'NSO3': {
       'edn':'CBXAZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MQ3': {
       'edn':'CBZYZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'SP3': {
       'edn':'CCVZZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'SP3': {
       'edn':'CCVZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'S3': {
       'edn':'CCWZZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'SK3': {
       'edn':'CCXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'SK3': {
       'edn':'CCXZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'K3': {
       'edn':'CCZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'K3': {
       'edn':'CCZZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2SO3': {
       'edn':'CEVZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  '4MS4':  {
         'edn':'DVDZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  '4M2S4': 'DVDZZZZ', 
'2MNK4': {
       'edn':'DWZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3NM4': {
       'edn':'DWZCZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MNS4': {
       'edn':'DWBAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MnuS4': {
       'edn':'DWDYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MK4': {
       'edn':'DXZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MNLK4': {
       'edn':'DXZZZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'N4':  {
         'edn':'DXZBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  '2N4': 'DXZBZZZ', 
'3MS4': {
       'edn':'DXBZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2NKS4': {
       'edn':'DXBBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MSNK4': {
       'edn':'DYXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MN4': {
       'edn':'DYZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'Mnu4': {
       'edn':'DYBYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MLS4': {
       'edn':'DYBYZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MNKS4': {
       'edn':'DYBAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MSK4': {
       'edn':'DZXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MA4': {
       'edn':'DZYZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'M4': {
       'edn':'DZZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MRS4': {
       'edn':'DZAZZYB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MKS4': {
       'edn':'DZBZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'SN4': {
       'edn':'DAXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  '3MN4': {
         'edn':'DAZYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'ML4':  'DAZYZZZ', 
'ML4': {
       'edn':'DAZYZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'KN4': {
         'edn':'DAZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'NK4': 'DAZAZZZ', 
# duplicate
  '2SMK4': {
         'edn':'DBVZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'M2SK4': 'DBVZZZZ', 
'MT4': {
       'edn':'DBWZZAZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MS4': {
       'edn':'DBXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MR4': {
       'edn':'DBYZZYB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MK4': {
       'edn':'DBZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2SNM4': {
       'edn':'DCVAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MSN4': {
       'edn':'DCXYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MSN4': {
       'edn':'DCXYZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'SL4': {
       'edn':'DCXYZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MKN4': {
       'edn':'DCZYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'ST4': {
       'edn':'DDUZZAZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'S4': {
       'edn':'DDVZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'SK4': {
       'edn':'DDXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'K4': {
       'edn':'DDZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3SM4': {
       'edn':'DFTZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2SKM4': {
       'edn':'DFVZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'MNO5': {
         'edn':'EXZAZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  '2MQ5': 'EXZAZZY', 
'2NKMS5': {
       'edn':'EXBBZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  '3MK5': {
         'edn':'EYZZZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  '2MO5': 'EYZZZZY', 
'2NK5': {
       'edn':'EYZBZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MS5': {
       'edn':'EYAZZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MP5': {
       'edn':'EYBZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'NSO5': {
       'edn':'EZXAZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'M5': {
       'edn':'EZZZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'M5': {
       'edn':'EZZZZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'M5':   {
         'edn':'EZZAZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'MNK5': 'EZZAZZA', 
'MB5': {
       'edn':'EZAZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'MSO5': {
         'edn':'EAXZZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  '2MP5': 'EAXZZZY', 
'2MS5': {
       'edn':'EAYZZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  '3MO5': {
         'edn':'EAZZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  '2MK5': 'EAZZZZA', 
'NSK5': {
       'edn':'EBXYZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MQ5': {
       'edn':'EBZYZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MSP5': {
       'edn':'ECVZZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MSK5': {
       'edn':'ECXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MSK5': {
       'edn':'ECXZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3KM5': {
       'edn':'ECZZZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2SP5': {
       'edn':'EETZZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2SK5': {
       'edn':'EEVZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'(SK)K5': {
       'edn':'EEXZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2(MN)K6': {
       'edn':'FVZBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'5MKS6': {
       'edn':'FVBZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2(MN)S6': {
       'edn':'FVBBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'5M2S6': {
       'edn':'FVDZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MNK6': {
       'edn':'FWZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'N6': {
       'edn':'FWZCZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MNS6': {
       'edn':'FWBAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3NKS6': {
       'edn':'FWBCZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MnuS6': {
       'edn':'FWDYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4MK6': {
       'edn':'FXZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  '2NM6': {
         'edn':'FXZBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'M2N6': 'FXZBZZZ', 
'4MS6': {
       'edn':'FXBZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2NMKS6': {
       'edn':'FXBBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MSNK6': {
       'edn':'FYXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MN6': {
       'edn':'FYZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  '2Mnu6': {
         'edn':'FYBYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  '2MNO6': 'FYBYZZZ', 
'2MNKS6': {
       'edn':'FYBAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MSK6': {
       'edn':'FZXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MA6': {
       'edn':'FZYZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'M6': {
       'edn':'FZZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MKS6': {
       'edn':'FZBZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MTN6': {
       'edn':'FAWAZAZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MSN6': {
       'edn':'FAXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4MN6': {
       'edn':'FAZYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2ML6': {
       'edn':'FAZYZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'MNK6': {
         'edn':'FAZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'MKN6': 'FAZAZZZ', 
'MKnu6': {
       'edn':'FABYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2(MS)K6': {
       'edn':'FBVZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MT6': {
       'edn':'FBWZZAZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MS6': {
       'edn':'FBXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MK6': {
       'edn':'FBZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2SN6': {
       'edn':'FCVAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MTN6': {
       'edn':'FCWYZAZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MSN6': {
       'edn':'FCXYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MSL6': {
       'edn':'FCXYZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'NSK6': {
         'edn':'FCXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'SNK6': 'FCXAZZZ', 
'MKL6': {
       'edn':'FCZYZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MKN6': {
       'edn':'FCZYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MST6': {
       'edn':'FDUZZAZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2SM6': {
       'edn':'FDVZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'MSK6': {
         'edn':'FDXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  'SKM6': 'FDXZZZZ', 
'2KM6': {
       'edn':'FDZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MSTN6': {
       'edn':'FEUYZAZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2(MS)N6': {
       'edn':'FEVYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MSKN6': {
       'edn':'FEXYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'S6': {
       'edn':'FFTZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  '2MNO7': {
         'edn':'GXZAZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  '3MQ7':  'GXZAZZY', 
'4MK7': {
       'edn':'GYZZZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2NMK7': {
       'edn':'GYZBZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MNSO7': {
       'edn':'GZXAZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'M7': {
       'edn':'GZZZZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  'M7':    {
         'edn':'GZZAZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  '2MNK7': 'GZZAZZA', 
#  'MNKO7': 'GZZAZZA', 
'2MSO7': {
       'edn':'GAXZZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MK7': {
       'edn':'GAZZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MSKO7': {
       'edn':'GCXZZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3M2NS8': {
       'edn':'HVBBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4MNS8': {
       'edn':'HWBAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'5MK8': {
       'edn':'HXZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2(MN)8': {
       'edn':'HXZBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'5MS8': {
       'edn':'HXBZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2(MN)KS8': {
       'edn':'HXBBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MSNK8': {
       'edn':'HYXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MN8': {
       'edn':'HYZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3Mnu8': {
       'edn':'HYBYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MNKS8': {
       'edn':'HYBAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4MSK8': {
       'edn':'HZXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MA8': {
       'edn':'HZYZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'M8': {
       'edn':'HZZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4MKS8': {
       'edn':'HZBZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MSN8': {
       'edn':'HAXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3ML8': {
       'edn':'HAZYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MNK8': {
       'edn':'HAZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3M2SK8': {
       'edn':'HBVZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2(NS)8': {
       'edn':'HBVBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MT8': {
       'edn':'HBWZZAZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MS8': {
       'edn':'HBXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MK8': {
       'edn':'HBZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  '2SNM8': {
         'edn':'HCVAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  '2SMN8': 'HCVAZZZ', 
'2MSL8': {
       'edn':'HCXYZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MSNK8': {
       'edn':'HCXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4MSN8': {
       'edn':'HCZYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MST8': {
       'edn':'HDUZZAZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2(MS)8': {
       'edn':'HDVZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MSK8': {
       'edn':'HDXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2(MK)8': {
       'edn':'HDZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3SN8': {
       'edn':'HETAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2SML8': {
       'edn':'HEVYZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2SKN8': {
       'edn':'HEVAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MSKL8': {
       'edn':'HEXYZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3SM8': {
       'edn':'HFTZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2SMK8': {
       'edn':'HFVZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'S8': {
       'edn':'HHRZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MNO9': {
       'edn':'IXZAZZY', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
# duplicate
  '2M2NK9':  {
         'edn':'IYZBZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
#  '2(MN)K9': 'IYZBZZA', 
'MA9': {
       'edn':'IZYZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MNK9': {
       'edn':'IZZAZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4MK9': {
       'edn':'IAZZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MSK9': {
       'edn':'ICXZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'5MNS10': {
       'edn':'JWBAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3M2N10': {
       'edn':'JXZBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'6MS10': {
       'edn':'JXBZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3M2NKS10': {
       'edn':'JXBBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4MSNK10': {
       'edn':'JYXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4MN10': {
       'edn':'JYZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4Mnu10': {
       'edn':'JYBYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'5MSK10': {
       'edn':'JZXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'M10': {
       'edn':'JZZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'5MKS10': {
       'edn':'JZBZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MSN10': {
       'edn':'JAXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'6MN10': {
       'edn':'JAZYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4ML10': {
       'edn':'JAZYZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MNK10': {
       'edn':'JAZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2(SN)M10': {
       'edn':'JBVBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4MS10': {
       'edn':'JBXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4MK10': {
       'edn':'JBZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2(MS)N10': {
       'edn':'JCVAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2MNSK10': {
       'edn':'JCXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'5MSN10': {
       'edn':'JCZYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3M2S10': {
       'edn':'JDVZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MSK10': {
       'edn':'JDXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3SMN10': {
       'edn':'JETAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2SMKN10': {
       'edn':'JEVAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4M2SN10': {
       'edn':'JEXYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3S2M10': {
       'edn':'JFTZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2(MS)K10': {
       'edn':'JFVZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4MSK11': {
       'edn':'KCXZZZA', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'5M2NS12': {
       'edn':'LVBBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3(MN)12': {
       'edn':'LWZCZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'6MNS12': {
       'edn':'LWBAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4M2N12': {
       'edn':'LXZBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'7MS12': {
       'edn':'LXBZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4M2NKS12': {
       'edn':'LXBBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'5MSNK12': {
       'edn':'LYXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3N2MS12': {
       'edn':'LYZAYZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'5MN12': {
       'edn':'LYZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'5Mnu12': {
       'edn':'LYBYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'6MSK12': {
       'edn':'LZXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3M2SN12': {
       'edn':'LZXBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'MA12': {
       'edn':'LZYZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'M12': {
       'edn':'LZZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4MSN12': {
       'edn':'LAXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4ML12': {
       'edn':'LAZYZZB', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4MNK12': {
       'edn':'LAZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'2(MSN)12': {
       'edn':'LBVBZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'5MT12': {
       'edn':'LBWZZAZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'5MS12': {
       'edn':'LBXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'5MK12': {
       'edn':'LBZZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3M2SN12': {
       'edn':'LCVAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'6MSN12': {
       'edn':'LCXYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3MNKS12': {
       'edn':'LCXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'5MSN12': {
       'edn':'LCZYZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4MST12': {
       'edn':'LDUZZAZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4M2S12': {
       'edn':'LDVZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'4MSK12': {
       'edn':'LDXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3(MS)12': {
       'edn':'LFTZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'3M2SK12': {
       'edn':'LFVZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'5MSN14': {
       'edn':'NAXAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'5MNK14': {
       'edn':'NAZAZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
'6MS14': {
       'edn':'NBXZZZZ', 
       'u':0.0,
       'f':1.0,
       'aka':[],
      }, 
}

