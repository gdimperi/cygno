# CYGNO library
*tools to handle cygno repository, images, ecc.*

install the CYGNO library:

      pip install git+https://github.com/CYGNUS-RD/cygno.git -U

requirements:
* Pyroot: https://root.cern/manual/python/ 
* oidc-agent: https://indigo-dc.gitbook.io/oidc-agent/installation
* boto3sts: https://github.com/DODAS-TS/boto3sts
* MIDAS: https://github.com/CYGNUS-RD/middleware/tree/master/midas

## CYGNO CLI Tool *cygno_repo*

tool to operate on CYGNO backet in S3 exeperiment repository

requirements:

* configure *oidc-agent* on your machine: https://codimd.web.cern.ch/s/SL-cWzDZB (DAQ setup, expert only https://codimd.web.cern.ch/s/_XqFfF_7V)
* example for osx

      brew tap indigo-dc/oidc-agent
      brew install oidc-agent

* install the IAM-Profile (not WLCG-Profile token) as reported in the second part of the guide https://codimd.web.cern.ch/s/SL-cWzDZB

* install python library  (https://github.com/DODAS-TS/boto3sts): 

      pip install git+https://github.com/DODAS-TS/boto3sts
      pip install git+https://github.com/CYGNUS-RD/cygno.git
      
* see https://boto3.amazonaws.com/v1/documentation/api/latest/index.html for S3 documentation

before run the script crate the iam token:

      eval `oidc-agent`
      oidc-token infncloud-iam (to generate or see your active token)
 
or refresh the token
 
      eval `oidc-agent`
      oidc-gen --reauthenticate --flow device infncloud-iam (if you alrady have the token)

usage

	Usage: cygno_repo	 [-tsv] [ls backet]
				 [put backet filename]
				 [[get backet filein] fileout]
				 [rm backet fileneme]
	
	
	Options:
	  -h, --help            	show this help message and exit
	  -t TAG, --tag=TAG     	tag where dir for data;
	  -s SESSION, --session=SESSION	token profile [infncloud-iam];
	  -v, --verbose         	verbose output;
                   
example:

      Giovannis-MacBook-Air-2:script mazzitel$ cygno_repo ls cygno-sim -t test
      2021-10-17 10:03:21  test/s3_list.py
      Giovannis-MacBook-Air-2:script mazzitel$ cygno_repo put cygno-sim s3_function.py -t test
      Giovannis-MacBook-Air-2:script mazzitel$ cygno_repo ls cygno-sim -t test
      2021-10-26 16:36:03  test/s3_function.py
      2021-10-17 10:03:21  test/s3_list.py
      Giovannis-MacBook-Air-2:script mazzitel$ cygno_repo get cygno-sim s3_function.py -t test
      downloading file of 5.82 Kb...
      Giovannis-MacBook-Air-2:script mazzitel$ cygno_repo ls cygno-sim -t test
      2021-10-26 16:36:03  test/s3_function.py
      2021-10-17 10:03:21  test/s3_list.py
      Giovannis-MacBook-Air-2:script mazzitel$ cygno_repo rm cygno-sim s3_function.py -t test
      removing file of 5.82 Kb...
      removed file: s3_function.py
      Giovannis-MacBook-Air-2:script mazzitel$ cygno_repo ls cygno-sim -t test
      2021-10-17 10:03:21  test/s3_list.py

Data are also shared in CYGNO CLOUD resources via the CYGNO application: https://notebook.cygno.cloud.infn.it:8888/ (jupyter notebook, python, root and terminal use dodasts/cygno-jupyter:v2.1 image) and availeble via web broser https://minio.cloud.infn.it/
      
## CYGNO CLI Tool *cygno_runs*

tool to show runs infromation stored in the logbook

	Usage: cygno_runs        [-ajgv] run number

	Options:
	  -h, --help     show this help message and exit
	  -a, --all      all runs in DBs;
	  -j, --json     json output;
	  -g, --google   old google sheet;
	  -v, --verbose  verbose output;
		
example:

	cygno_runs 826 -g (old logbook text output)
	or 
	cygno_runs 5360 -j (new logbook json output)
	cygno_runs -a (dump all the dadabase)
	
	
## CYGNO CLI Tool *cygno_his2root*

convert HIS HoKaWo output file in CYGNO root histograms data files

	Usage: cygno_his2root	 [-d] DIRECTORY
	
	Options:
	  -h, --help     show this help message and exit
	  -d, --delete   delete HIS file after conversion;
	  -v, --verbose  verbose output;
	  
## CYGNO CLI Tool *cygno_mid2root*

convert MIDAS output file in CYGNO root histograms data files

	pip install 'https://github.com/CYGNUS-RD/middleware/blob/master/midas/midaslib.tar.gz?raw=true’


	Usage: cygno_mid2root	 <RUN number>

	Options:
	  -h, --help            show this help message and exit
	  -p PATH, --path=PATH  path to file or cache directory
	  -v, --verbose         verbose output;

## CYGNO library tool

### data class for ROOT files

	class cfile:
		def __init__(self, file, pic, wfm, max_pic, max_wfm, x_resolution, y_resolution):
			self.file         = file
			self.pic          = pic 
			self.wfm          = wfm
			self.max_pic      = max_pic
			self.max_wfm      = max_wfm
			self.x_resolution = x_resolution
			self.y_resolution = y_resolution

* open_mid(run, path='/tmp/',  cloud=True,  tag='LNGS', verbose=False) open/cache MIDAS form cloud in path
* open_root(run, path='/tmp/',  cloud=True,  tag='LAB', verbose=False)  open/cache ROOT form cloud in path
* open_(run, tag='LAB', posix=False, verbose=True) - open cygno ROOT/MID file from remote or on cloud posix like access and return cfile class type
* read_(f, iTr) - return image array from file poiter
* pic_(cfile, iTr=0) - return immage array of track iTr from cfile
* wfm_(cfile, iTr=0, iWf=0) - return amplitude and time of iTr track and iWr waveform from cfile
* ped_(run, path='./ped/', tag = 'LAB', posix=False, min_image_to_read = 0, max_image_to_read = 0, verbose=False) - cerate (if not exist) root file image of mean and sigma for each pixel and return main and sigma imege of pedestal runs

### logbook 
* read_cygno_logbook(verbose=False) 		ruturn pandas db old google sheet logbook info
* read_cygno_sql_logbook(verbose=False)		return pandas db sql logbook info
* run_info_logbook(run, sql=True, verbose=True)	return pandas db google/sql run [int] info

### s3 repo
* s3.root_file(run, tag='LAB', posix=False, verbose=False)
* s3.backet_list(tag, bucket='cygno-sim', session="infncloud-iam", verbose=False)
* s3.obj_put(filename, tag, bucket='cygno-sim', session="infncloud-iam", verbose=False)
* s3.obj_get(filein, fileout, tag, bucket='cygno-sim', session="infncloud-iam", verbose=False)
* s3.obj_rm(filename, tag, bucket='cygno-sim', session="infncloud-iam", verbose=False)


