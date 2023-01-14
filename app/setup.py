from distutils.core import setup
# from setuptools import setup
import py2app

# setup(
#     app=["livelife.py"], 
#     options={"py2app":{"argv_emulation": True}},
#     cmdclass={"py2app":py2app}
#     )

#Turns livelife.py into an executable

# setup(app = ["livelife.py"])
setup(console=['livelife.py'])

#ONLY RUN THIS WHEN LIVELIFE.PY IS DONE