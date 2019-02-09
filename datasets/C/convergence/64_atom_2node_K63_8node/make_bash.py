import numpy as np
import sys
import os
sys.path.append('../../../../modules')
import qe_input


bash_name = 'convergence.sh'

command = 'mpirun /n/home03/jonpvandermause/qe-6.2.1/bin/pw.x -npool 63 < C_conv.in > C_conv.out'

bash_inputs = dict(n=252, N=8, t=7, e='test.err', p='kozinsky', o='test.out',
                   mem_per_cpu=1000,
                   mail_user='jonathan_vandermause@g.harvard.edu',
                   command=command)

conv_bash = qe_input.BashInput(bash_name, bash_inputs)
conv_bash.write_bash_text()

if os.path.isdir('__pycache__'):
    os.system('rm -r __pycache__')