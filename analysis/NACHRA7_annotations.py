'''
Annotations for nicotinic receptor alpha-7 project
'''

import itertools

#  used for mdtraj
subunit_dic = {0:0,1:1,2:2,3:3,4:4,5:0,-1:4}

#  used for MDAnalysis
subunit_dic_mda = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'A'}

subunit_type = {0:'a7',1:'a7',2:'a7',3:'a7',4:'a7',5:'a7'}

#  pore lining residues
pore_annotation = {
    'a7':{
            '-1': '(resid 237 and resname GLU)',
            '2': '(resid 240 and resname SER)',
            '6': '(resid 244 and resname THR)',
            '9':  '(resid 247 and resname LEU)',
            '13': '(resid 251 and resname VAL)',
            '16': '(resid 254 and resname LEU)',
            '20': '(resid 258 and resname GLU)'
    }
}
secondary_structure_annotation = {
    'a7':{
        'ECD': '(resSeq 10 to 206)',
        'TMD': '(resSeq 207 to 401)'
    }
    }

domain_structure_annotation = {
    'a7':{
        'M1': '(resSeq 207 to 232)',
        'M2': '(resSeq 235 to 261)',
        'M3': '(resSeq 267 to 298)',
        'MX': '(resSeq 300 to 321)',
        'MA': '(resSeq 331 to 358)',
        'M4': '(resSeq 359 to 390)',
        'MC': '(resSeq 391 to 401)',
        'loop_C': '(resSeq 176 to 205)',
        'M2_M3_loop': '(resSeq 260 to 268)',
    }
}

residue_annotations_plot = {
                     "9'": 0,
                     "20'": 15,
                     "-1'": -14,
                     "D100": 51, "E97": 38, "D43": 28}

domain_annotations_plot = {
                     'Water_1':range(80,100),
                     'ECD':range(25,80),
                     'TMD': range(-25,25),
                     'ICD': range(-57,-25),
                     'Water_2':range(-100,-57)}

traj_notes = ['BGT',
              'PNU_EPJ',
              'EPJ',
]

default_load_location = '../trajectory/'
default_save_location = '../trajectory/'
default_skip = 1
default_rep = 4

mutation = 'WT'

production_dic = {'traj_note': traj_notes,
                 'load_location': ["".join(i) for i in itertools.product([default_load_location], traj_notes,['/production/'])],
                 'save_location': [default_save_location] * len(traj_notes),
                 'skip': [default_skip] * len(traj_notes),
                 'rep': [default_rep] * len(traj_notes)}

ca_eq_dic = {'traj_note': traj_notes,
                 'load_location': ["".join(i) for i in itertools.product([default_load_location], traj_notes)],
                 'save_location': [default_save_location] * len(traj_notes),
                 'skip': [default_skip] * len(traj_notes),
                 'rep': [1] * len(traj_notes)}

walker_dic = {'traj_note': traj_notes,
              #'load_location': ["".join(i) for i in itertools.product([default_load_location], traj_notes)],
              'ion_type': ['SOD','CAL','CAM','CLA','POT'],
              'save_location': ["".join(i) for i in itertools.product([default_load_location], traj_notes)],
              #'skip': [default_skip] * len(traj_notes),
              'walker': [16] * len(traj_notes)}

comp_ephys_dic = {'traj_note': traj_notes,
              #'load_location': ["".join(i) for i in itertools.product([default_load_location], traj_notes)],
              'imbalance': [12,14,16,18,20,22,24,26,28,30,32,34],
              'dir': 'EPHYS',
              'save_location': ["".join(i) for i in itertools.product([default_load_location], traj_notes)]}

ef_dic = {'traj_note': ['PNU_EPJ', 'EPJ', 'PNU_EPJ_NOECD','PNU_EPJ_NOICD','PNU_EPJ_E97A', 'PNU_EPJ_CAM'],
          
                 'load_location': ["".join(i) for i in itertools.product([default_load_location], ['PNU_EPJ'],['/EF_200/','/EF_n200','/EF_200_0CA','/EF_n200_0CA'])] + 
                                  ["".join(i) for i in itertools.product([default_load_location], ['EPJ'],['/EF_200/','/EF_n200'])] +
                                  ["".join(i) for i in itertools.product([default_load_location], ['PNU_EPJ_NOECD'],['/EF_200/','/EF_n200'])] + 
                                  ["".join(i) for i in itertools.product([default_load_location], ['PNU_EPJ_NOICD'],['/EF_200/','/EF_n200'])] +
                                  ["".join(i) for i in itertools.product([default_load_location], ['PNU_EPJ_E97A'],['/EF_200/','/EF_n200'])] + 
                              ["".join(i) for i in itertools.product([default_load_location], ['PNU_EPJ_CAM'],['/EF_200/','/EF_n200'])],
                 'save_location': ["".join(i) for i in itertools.product([default_load_location], ['PNU_EPJ'],['/EF_200/','/EF_n200','/EF_200_0CA','/EF_n200_0CA'])] + 
                                  ["".join(i) for i in itertools.product([default_load_location], ['EPJ'],['/EF_200/','/EF_n200'])] +
                                  ["".join(i) for i in itertools.product([default_load_location], ['PNU_EPJ_NOECD'],['/EF_200/','/EF_n200'])] + 
                                  ["".join(i) for i in itertools.product([default_load_location], ['PNU_EPJ_NOICD'],['/EF_200/','/EF_n200'])] + 
                                  ["".join(i) for i in itertools.product([default_load_location], ['PNU_EPJ_E97A'],['/EF_200/','/EF_n200'])] + 
                              ["".join(i) for i in itertools.product([default_load_location], ['PNU_EPJ_CAM'],['/EF_200/','/EF_n200'])],                 
                 'skip': [default_skip] * 12,
                 'rep': [default_rep] * 12}




cg_dic = {'traj_note': ['EPJ', 'PNU_EPJ', 'BGT'],
              'load_location': ["".join(i) for i in itertools.product(['../trajectory/' + 'CG/'], ['EPJ', 'PNU_EPJ', 'BGT'])],
              'save_location': ["".join(i) for i in itertools.product(['../trajectory/' + 'CG/'], ['EPJ', 'PNU_EPJ', 'BGT'])]}

cg_pnu_dic = {'traj_note': ['BGT_WITHPNU', 'EPJ_WITHPNU', 'PNU_EPJ_WITHPNU', 'PNU_EPJ_M253L_A225D_WITHPNU', 'PNU_EPJ_M253L_WITHPNU', 'PNU_EPJ_A225D_WITHPNU'],
              'load_location': ["".join(i) for i in itertools.product(['../trajectory/' + 'CG/'], ['BGT_WITHPNU', 'EPJ_WITHPNU', 'PNU_EPJ_WITHPNU', 'PNU_EPJ_M253L_A225D_WITHPNU', 'PNU_EPJ_M253L_WITHPNU', 'PNU_EPJ_A225D_WITHPNU'])],
              'save_location': ["".join(i) for i in itertools.product(['../trajectory/' + 'CG/'], ['BGT_WITHPNU', 'EPJ_WITHPNU', 'PNU_EPJ_WITHPNU', 'PNU_EPJ_M253L_A225D_WITHPNU', 'PNU_EPJ_M253L_WITHPNU', 'PNU_EPJ_A225D_WITHPNU'])],
              'skip': [10] * 6,
             'rep': [4] * 6}


ion_param_dic = {'traj_note': ['SOD', 'POT', 'CAL_old', 'CAL', 'CAM'],
              'load_location': ["".join(i) for i in itertools.product(['../trajectory/simulation_ions/'], ['sod', 'pot', 'cal_old', 'cal', 'cam'])]}

first_hydration_shell_dic = {'SOD': 2.23,
                             'POT': 2.64,
                             'CAL': 2.23,
                             'CAM': 2.43,
                             'CLA': 3.04,}

