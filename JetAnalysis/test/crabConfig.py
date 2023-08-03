from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs = True
#config.General.requestName = 'Hiforest_PbPb_Run2015_FWD_newest1'
config.General.requestName = 'HiForest_PbPb_Run2018'

config.section_('JobType')
#config.JobType.psetName = 'runForestdat.py'
config.JobType.psetName = 'runForestAOD_pponAA_DATA_103X.py'
config.JobType.pluginName = 'Analysis'
#config.JobType.outputFiles = ['HiforestAOD_PbPb_Run2015.root']
config.JobType.outputFiles = ['HiForestAOD.root']
config.JobType.pyCfgParams = ['noprint']
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 18000

config.section_('Data')
config.Data.inputDataset = '/HIForward/HIRun2018A-04Apr2019-v1/AOD'
#config.Data.inputDataset = '/HIForward/HIRun2015-02May2016-v1/AOD'
#config.Data.inputDataset = '/HIMinimumBias1/HIRun2015-PromptReco-v1/AOD'
#config.Data.inputDataset = '/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIWinter15GS-MCRUN1_71_V0-v1/GEN-SIM'
#config.Data.inputDataset = '/MinBias_TuneCUETP8M1_13TeV-pythia8/echapon-MinBias_TuneCUETP8M1_13TeV-pythia8_run1_step2_20150902-53128c16d7c8b597617eae6db0c76986/USER'
#config.Data.inputDataset = '/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-NhcalZSNoPU_74X_mcRun2_startup_dataMC_comparison_v1-v1/GEN-SIM-RAW'
#config.Data.inputDBS     = 'global'
config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON_HF_and_MuonPhys.txt'
config.Data.ignoreLocality=True

config.Data.publication = False
config.Data.publishDBS = 'phys03'
config.Data.unitsPerJob = 2
#NJOBS = 290
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.splitting = 'EventBased'
config.Data.splitting = 'FileBased'
config.Data.outputDatasetTag = 'HiForward_Hiforest_PbPb_Run2018'
#config.Data.publishDataName = 'MinBias_TuneCUETP8M1_13TeV_pythia8_RunIIWinter15GS-MCRUN2_71_V0-v1_GEN_SIM_RAW_v2'
config.Data.outLFNDirBase = '/store/user/clemahie'
config.section_('User')
config.section_('Site')
config.Site.blacklist = ['T2_US_Vanderbilt']
config.Site.whitelist = ['T2_US_*']
#config.Site.storageSite = 'T2_RU_ITEP'
#config.Site.storageSite = 'T2_US_Nebraska'
config.Site.storageSite = 'T3_CH_CERNBOX'
