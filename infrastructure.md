# Computing infrastrcture

### Signup on computing ressources
* if you are not associeted/hosted/employed of INFN plese signup on: https://signup.app.infn.it/ (1) and then accept the securety policy at https://userportal.app.infn.it/ 
* to access CYGNO bach system, jupyter notebook and storage plese register as USER also on the INFN CLOUD https://guides.cloud.infn.it/docs/users-guides/en/latest/users_guides/getting_started.html

as responsable put everyware **Giovanni Mazzitelli**: giovanni.mazzitelli@lnf.infn.it

### Computing resources and OPEN VPN @ LNF
if you need to access LNF LAN via OpenVPN install the infn-user profile
* send an email to: giovanni.mazzitelli@lnf.infn.it to be autorized
* http://www.lnf.infn.it/computing/networking/openvpn-en.php
* if you need also local computing resesources plese fill http://www.lnf.infn.it/computing/cgi-bin/newaccountrequest.pl 

### Computing resources and OPEN VPN @ LNGS
* send an email to: giovanni.mazzitelli@lnf.infn.it to be autorized
* install the profile https://www.lngs.infn.it/en/vpn
* if you need also local computing resesources plese ask for it by mail to giovanni.mazzitelli@lnf.infn.it

### CYGNO CLOUD Storage
you can upload/dowdload and mange data on the CYGNO cloud repositoty by: 

* Web Tool: https://minio.cloud.infn.it/minio/login
* Cloud CYGNO interface tool: https://notebook.cygno.cloud.infn.it:8888/ 
* CLI tool: https://github.com/CYGNUS-RD/cygno#cygno-cli-tool-cygno_repo

the cloud-storage/ contan tree backet:
* cloud-data: daq stored data, read only
* cloud-sim: simulation input and output data, read and write
* cloud-analysis: analisys input and output data, read and write
* (cygno - olda data repository, USERNAME private repository on cloud, scratch repository on cloud)

*(1) for foreign users 
* to be reggistred on AAI you need a CODICE FISCALE (CF) that you can generate with the tool:

      https://quifinanza.it/strumenti/codice-fiscale 
      (Provincia: “Stato Estero")
      (LUOGO di NASCITA: BRASILE)

* up to now also a local username in INFN local sites computing resources is required (see prevous point)

### Usage of the CYGNO notebook
cygno default notebook is reachble at the address https://notebook.cygno.cloud.infn.it:8888/ 
* login with AAI credentials
* start your notebook choosing version and RAM needed. That RAM is the maximum your interactive job can exploit. if there are concurred interactive job form other users draining the ram you can have your job killed. so don't ask the maximum of RAM if you don't relay need, and use condor queue instead of interactive jobs. 
* run/edit your notebook Python/ROOT or script via the available buttons
* use private folder to develop and store your code
* use path /jupyter-workspace/cloud-storage/ to access cygno data/repository (cygno-data is RO accessible only by DAQ, the other are RW)  
