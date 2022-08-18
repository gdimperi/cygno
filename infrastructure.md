# Computing infrastrcture
The CYGNO exepriment develop a facility based on the [INFN cloud](https://www.cloud.infn.it/) to host:
- data experiment storage (S3 based - [https://minio.cloud.infn.it/](https://minio.cloud.infn.it/))
- tape backup storage
- notebook web interface with python and root kernles, bach resources
- bach resources accesible via condor queues

Moreover, computing resources are available at LNF and LNGS (Cygno login and U-LITE nodes) and two [DAQ server](https://drive.google.com/file/d/1kEzvfJK7WSXK2Y1vfEwRqcH9uSmoYsXl/view?usp=sharing) equipped with GPU

### Signup on computing ressources (needed for all resources: CLOUD, LNGS, LNF)
* if you are not associeted/hosted/employed of INFN plese signup on: https://signup.app.infn.it/ (see note (1)) 
* accept the security policy  https://userportal.app.infn.it/;
* follow the traning on computing security;

### Computing resources on INFN Cloud
* signup as **user** on [INFN CLOUD](https://guides.cloud.infn.it/docs/users-guides/en/latest/users_guides/getting_started.html), as responsable put everyware **Giovanni Mazzitelli**
* follow the [howto](https://github.com/CYGNUS-RD/cygno/blob/main/infrastructure.md#usage-of-the-cygno-notebook) 


### Computing resources and OPEN VPN @ LNF (test DAQ server, ecc)
* send an email to: giovanni.mazzitelli@lnf.infn.it to be autorized
* when aproved install the profile http://www.lnf.infn.it/computing/networking/openvpn-en.php
* if you need also local computing resesources plese fill http://www.lnf.infn.it/computing/cgi-bin/newaccountrequest.pl 

### Computing resources and OPEN VPN @ LNGS (DAQ, shift, ecc)
* send an email to: giovanni.mazzitelli@lnf.infn.it to be autorized
* if you need also local computing resesources **Cygno login and U-LITE nodes** (deprecated) plese specify in the mail.
* when aproved install the profile install the profile https://www.lngs.infn.it/en/vpn

### DAQ and Middle Ware ###
* Data are collected by DAQ at LNF and LNGS [server configuration](https://drive.google.com/file/d/1kEzvfJK7WSXK2Y1vfEwRqcH9uSmoYsXl/view?usp=sharing) 
* Exeperiment data are monitored by the quasi-online recostracion by the [Middle Ware](https://github.com/CYGNUS-RD/middleware)

### CYGNO CLOUD Storage
Data collected are automatically pushed by DAQ on INFN S3 cloud storage. The storage data can be mange via: 

* Web Tool: https://minio.cloud.infn.it/minio/login
* Cloud CYGNO web interface tool: https://notebook.cygno.cloud.infn.it:8888/ 
* CLI tool: https://github.com/CYGNUS-RD/cygno#cygno-cli-tool-cygno_repo

the cloud-storage/ contain tree backet:
* cloud-data: daq stored data, read only
* cloud-sim: simulation input and output data, read and write
* cloud-analysis: analysis input and output data, read and write
* (cygno - old data repository, USERNAME private repository on cloud, scratch repository on cloud)

*(1) for foreign users 
* to be reggistred on AAI you need a CODICE FISCALE (CF) that you can generate with the tool:

      https://quifinanza.it/strumenti/codice-fiscale 
      (Provincia: “Stato Estero")
      (LUOGO di NASCITA: BRASILE)

* up to now also a local username in INFN local sites computing resources is required (see prevous point)

### Usage of the CYGNO notebook web interface

CYGNO default notebook is reachable at the address https://notebook.cygno.cloud.infn.it:8888/; a test environment is also available at the address https://192.135.24.159:8888/ for expert users. The notebook is configured with:
- ROOT 6.24/06
- Python 2/3.6 ([Default package list notebook >= 16](https://raw.githubusercontent.com/CYGNUS-RD/cygno/main/img/PackageListV16.txt))
- Garfield 
- GEANT 4.10.5
- https://gitlab.cern.ch/RooUnfold
- https://github.com/christopherpoole/CADMesh
- notebook version >16: python 3.9.10, emacs
- CONDOR queues are recheble by the notebook terminal or via any computer by means of dedicated container ([https://github.com/CYGNUS-RD/mycondor])
* to access the resource login with AAI credentials (see above to be athorized) 
<img src="https://github.com/CYGNUS-RD/cygno/blob/main/img/login.png" alt="login" style="width:400px;"/>
<img src="https://github.com/CYGNUS-RD/cygno/blob/main/img/aai.png" alt="login" style="width:400px;"/>
* start your notebook choosing version and RAM needed. That RAM is the maximum your interactive job can exploit. if there are concurred interactive job form other users draining the ram you can have your job killed. so don't ask the maximum of RAM if you don't relay need, and use condor queue instead of interactive jobs: https://github.com/CYGNUS-RD/mycondor#cygno-condor-queue 
<img src="https://github.com/CYGNUS-RD/cygno/blob/main/img/resorce.png" alt="login" style="width:400px;"/>
* run/edit your notebook Python/ROOT or script via the available buttons
<img src="https://github.com/CYGNUS-RD/cygno/blob/main/img/buttos.png" alt="login" style="width:400px;"/>
* use private folder to develop and store your code
* use path /jupyter-workspace/cloud-storage/ to access cygno data/repository (cygno-data is RO accessible only by DAQ, the other are RW) or: https://github.com/CYGNUS-RD/cygno/blob/main/infrastructure.md#cygno-cloud-storage 
