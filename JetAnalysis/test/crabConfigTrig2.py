from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.requestName = 'HiForest_PbPb_Run2018_trig_softdrop'
#config.General.requestName = 'HiForest_PbPb_Run2018_trig_ak4PF'
#config.General.requestName = 'HiForest_PbPb_Run2018_trig_ak6PF'
#config.General.requestName = 'HiForest_PbPb_Run2018_trig_ak8PF'

config.section_('JobType')
config.JobType.psetName = 'runForestAOD_pponAA_DATA_103X_trig.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['HiForestAOD_trig.root']
config.JobType.pyCfgParams = ['noprint']
config.JobType.numCores = 4
#config.JobType.maxMemoryMB = 4400
config.JobType.maxMemoryMB = 4000
#config.JobType.maxJobRuntimeMin=190
config.JobType.maxJobRuntimeMin=250
#config.JobType.maxMemoryMB = 2000

config.section_('Data')
config.Data.inputDataset = '/HIForward/HIRun2018A-04Apr2019-v1/AOD'
config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON_HF_and_MuonPhys.txt'

config.Data.publication = False
config.Data.publishDBS = 'phys03'
#config.Data.unitsPerJob = 18
config.Data.unitsPerJob = 1
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'LumiBased'
#config.Data.splitting = 'Automatic'
config.Data.outputDatasetTag = 'HiForward_Hiforest_PbPb_Run2018'
config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T3_CH_CERNBOX'
