from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.requestName = 'HiForest_PbPb_Run2018_noise'

config.section_('JobType')
config.JobType.psetName = 'runForestAOD_pponAA_DATA_103X_noise.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['HiForestAOD_noise.root']
config.JobType.pyCfgParams = ['noprint']
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 4400

config.section_('Data')
config.Data.inputDataset = '/HIEmptyBX/HIRun2018A-27Feb2019-v1/AOD'
config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON_HF_and_MuonPhys.txt'

config.Data.publication = False
config.Data.publishDBS = 'phys03'
config.Data.unitsPerJob = 1
config.Data.splitting = 'FileBased'
config.Data.outputDatasetTag = 'HIEmptyBX_Hiforest_PbPb_Run2018'
config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T3_CH_CERNBOX'
