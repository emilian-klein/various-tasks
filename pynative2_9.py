#How to check file is empty or not

import os
print(os.stat(r"test2_6.txt").st_size == 0)