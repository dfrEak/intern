from pywebcopy import save_webpage
import time

kwargs = {'project_name': 'tabelog'}

# from A1301 to A1331 (Tokyo area)
for area in range(1, 2):
    # dummy for area A1301 50 pages
    for pageList in range(1,51):
        save_webpage(
            url="https://tabelog.com/tokyo/A13"+format(area, '02d')+"/rstLst/"+str(pageList)+"/",
            project_folder='C:/Users/staff/work/eric/downloads',
            **kwargs)
        # give 1s to next download
        time.sleep(1)

#########################################################
#NOTE : Before run, they will open a lot of pages
#########################################################