
### HiForest Configuration
# Collisions: PbPb
# Type: Data
# Input: AOD
# mem check

cleanJets = True

import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')
process.options = cms.untracked.PSet(SkipEvent = cms.untracked.vstring('ProductNotFound'))

###############################################################################
# HiForest labelling info
###############################################################################

process.load("HeavyIonsAnalysis.JetAnalysis.HiForest_cff")
process.HiForest.inputLines = cms.vstring("HiForest 103X")
import subprocess, os
version = subprocess.check_output(['git',
    '-C', os.path.expandvars('$CMSSW_BASE/src'), 'describe', '--tags'])
if version == '':
    version = 'no git info'
process.HiForest.HiForestVersion = cms.string(version)


############################
# Memory Check
############################
#process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",
#    ignoreTotal = cms.untracked.int32(1)
#)

###############################################################################
# Input source
###############################################################################

process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    fileNames = cms.untracked.vstring(
        #"file:/afs/cern.ch/work/r/rbi/public/forest/HIHardProbes_HIRun2018A-PromptReco-v2_AOD.root"
        "/store/hidata/HIRun2018A/HIForward/AOD/04Apr2019-v1/50005/8DBBBB66-2713-2742-A217-954ED493456D.root"
),
    )

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

###############################################################################
# Load Global Tag, Geometry, etc.
###############################################################################

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '103X_dataRun2_Prompt_v2', '')
process.HiForest.GlobalTagLabel = process.GlobalTag.globaltag

print('\n\033[31m~*~ USING CENTRALITY TABLE FOR PbPb 2018 DATA ~*~\033[0m\n')
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
process.GlobalTag.toGet.extend([
    cms.PSet(record = cms.string("HeavyIonRcd"),
        tag = cms.string("CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1033p1x01_offline"),
        connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
        label = cms.untracked.string("HFtowers")
        ),
    ])

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")

process.GlobalTag.toGet.extend([
    cms.PSet(record = cms.string("BTagTrackProbability3DRcd"),
             tag = cms.string("JPcalib_Data103X_2018PbPb_v1"),
             connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")

         )
      ])

###############################################################################
# Define tree output
###############################################################################

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("HiForestAOD_trig.root"))

###############################################################################
# Additional Reconstruction and Analysis: Main Body
###############################################################################

#############################
# Jets
#############################
# jet reco sequence
process.load('HeavyIonsAnalysis.JetAnalysis.fullJetSequence_pponAA_data_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.hiFJRhoAnalyzer_cff')
process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzer_cfi")
process.pfcandAnalyzer.doTrackMatching  = cms.bool(True)

from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import overrideJEC_DATA_PbPb5020_2018
process = overrideJEC_DATA_PbPb5020_2018(process)

###############################################################################

############################
# Event Analysis
############################
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.skimanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hltobject_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.l1object_cfi')

from HeavyIonsAnalysis.EventAnalysis.hltobject_cfi import trigger_list_data
process.hltobject.triggerNames = trigger_list_data

###############################################################################
process.triggerSelection = cms.EDFilter( "TriggerResultsFilter",
    triggerConditions = cms.vstring(
     'HLT_HIZeroBiasPixel_SingleTrack_v1',
     'HLT_HIZeroBias_v1' ),
    hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
    l1tResults = cms.InputTag( "gtDigis" ),
    l1tIgnoreMask = cms.bool( False ),
    l1techIgnorePrescales = cms.bool( False ),
    daqPartitions = cms.uint32( 1 ),
    throw = cms.bool( True )
)
#########################
# Track Analyzer
#########################
process.load('HeavyIonsAnalysis.TrackAnalysis.ExtraTrackReco_cff')
process.load('HeavyIonsAnalysis.TrackAnalysis.TrkAnalyzers_cff')

# Use this instead for track corrections
# process.load('HeavyIonsAnalysis.TrackAnalysis.TrkAnalyzers_Corr_cff')

###############################################################################

#####################
# Photons
#####################
SSHIRun2018A = "HeavyIonsAnalysis/PhotonAnalysis/data/SSHIRun2018A.dat"
process.load('HeavyIonsAnalysis.PhotonAnalysis.correctedElectronProducer_cfi')
process.correctedElectrons.correctionFile = SSHIRun2018A

process.load('HeavyIonsAnalysis.PhotonAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.doGenParticles = False
process.ggHiNtuplizerGED.doGenParticles = False
process.ggHiNtuplizerGED.gsfElectronLabel = "correctedElectrons"

###############################################################################

# Exclusive ?
#process.load('Exclusivity.ExlAnalyzer.ExlAnalyzer_cfg')


#######################
# B-tagging
######################
# replace pp CSVv2 with PbPb CSVv2 (positive and negative taggers unchanged!)
process.load('RecoBTag.CSVscikit.csvscikitTagJetTags_cfi')
process.load('RecoBTag.CSVscikit.csvscikitTaggerProducer_cfi')
process.akPu4PFCombinedSecondaryVertexV2BJetTags = process.pfCSVscikitJetTags.clone()
process.akPu4PFCombinedSecondaryVertexV2BJetTags.tagInfos = cms.VInputTag(
    cms.InputTag("akPu4PFImpactParameterTagInfos"),
    cms.InputTag("akPu4PFSecondaryVertexTagInfos"))
process.akCs4PFCombinedSecondaryVertexV2BJetTags = process.pfCSVscikitJetTags.clone()
process.akCs4PFCombinedSecondaryVertexV2BJetTags.tagInfos = cms.VInputTag(
    cms.InputTag("akCs4PFImpactParameterTagInfos"),
    cms.InputTag("akCs4PFSecondaryVertexTagInfos"))
process.akPu4CaloCombinedSecondaryVertexV2BJetTags = process.pfCSVscikitJetTags.clone()
process.akPu4CaloCombinedSecondaryVertexV2BJetTags.tagInfos = cms.VInputTag(
    cms.InputTag("akPu4CaloImpactParameterTagInfos"),
    cms.InputTag("akPu4CaloSecondaryVertexTagInfos"))

# trained on CS jets
process.CSVscikitTags.weightFile = cms.FileInPath(
    'HeavyIonsAnalysis/JetAnalysis/data/TMVA_Btag_CsJets_PbPb2018_BDTG.weights.xml')

###############################################################################

#########################
# RecHits & pfTowers (HF, Castor & ZDC)
#########################
# ZDC RecHit Producer
process.load('RecoHI.ZDCRecHit.QWZDC2018Producer_cfi')
process.load('RecoHI.ZDCRecHit.QWZDC2018RecHit_cfi')

process.load('HeavyIonsAnalysis.JetAnalysis.rechitanalyzer_cfi')
process.rechitanalyzerpp.doZDCRecHit = True
process.rechitanalyzerpp.zdcRecHitSrc = cms.InputTag("QWzdcreco")
process.pfTowerspp.doHF = False

process.rechitanalyzerpp.doHF=False
#process.rechitanalyzerpp.HFtowerMin = cms.untracked.double(0)
#process.rechitanalyzerpp.HFTreePtMin = cms.untracked.double(0)
#process.rechitanalyzerpp.hcalHFRecHitSrc = cms.InputTag("reducedHcalRecHits","hfreco")
process.rechitanalyzerpp.doHBHE=False
#process.rechitanalyzerpp.HBHETreePtMin = cms.untracked.double(0)
#process.rechitanalyzerpp.hcalHBHERecHitSrc = cms.InputTag("reducedHcalRecHits","hbhereco")
process.rechitanalyzerpp.doEcal=False
#process.rechitanalyzerpp.EBTreePtMin = cms.untracked.double(0)
#process.rechitanalyzerpp.EBRecHitSrc = cms.InputTag("reducedEcalRecHitsEB")
#process.rechitanalyzerpp.EETreePtMin = cms.untracked.double(0)
#process.rechitanalyzerpp.EERecHitSrc = cms.InputTag("reducedEcalRecHitsEE")
###############################################################################
#Recover peripheral primary vertices
#https://twiki.cern.ch/twiki/bin/view/CMS/HITracking2018PbPb#Peripheral%20Vertex%20Recovery
process.load("RecoVertex.PrimaryVertexProducer.OfflinePrimaryVerticesRecovery_cfi")
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")

# clean bad PF candidates
if cleanJets:
    process.load("RecoHI.HiJetAlgos.HiBadParticleFilter_cfi")
    process.pfBadCandAnalyzer = process.pfcandAnalyzer.clone(pfCandidateLabel = cms.InputTag("filteredParticleFlow","cleaned"))
    process.pfFilter = cms.Path(process.filteredParticleFlow + process.pfBadCandAnalyzer)

#########################
# Main analysis list
#########################

process.jetSequence_reduced_r2 = cms.Sequence(
    process.rhoSequence +
    process.highPurityTracks +
    process.ak2PFJets +
    process.ak2PFJetSequence
)

process.jetSequence_reduced_r6 = cms.Sequence(
    process.rhoSequence +
    process.highPurityTracks +
    process.ak6PFJets +
    process.ak6PFJetSequence
)

process.jetSequence_softdrop_r4 = cms.Sequence(
    process.rhoSequence +
    process.highPurityTracks +
    process.akSoftDrop4PFJets +
    process.akSoftDrop4PFJetSequence
)

process.ana_step = cms.Path(
    process.offlinePrimaryVerticesRecovery +
    process.HiForest +
    #process.hltanalysis +
    #process.hltobject +
    #process.l1object +
    #process.triggerSelection *
    process.centralityBin +
    process.hiEvtAnalyzer +
    process.rhoSequence +
    process.highPurityTracks +
    #process.ak2PFJets +
    #process.ak2PFJetSequence +   
    #process.ak4PFJets +
    #process.ak4PFJetSequence +   
    #process.ak8PFJets +
    #process.ak8PFJetSequence +
    process.akSoftDrop4PFJets +   
    process.akSoftDrop4PFJetSequence +
    #process.hiPuRhoR3Analyzer + 
    process.correctedElectrons +
    #process.ExlAnalyzer +
    process.ggHiNtuplizer +
    #process.ggHiNtuplizerGED +
    #process.hiFJRhoAnalyzer +
    #process.hiFJRhoAnalyzerFinerBins +
    process.pfcandAnalyzer +
    #process.pfcandAnalyzerCS +
    process.trackSequencesPP +
    process.zdcdigi +
    process.QWzdcreco +
    process.rechitanalyzerpp
    )

# # edm output for debugging purposes
process.output = cms.OutputModule(
     "PoolOutputModule",
     fileName = cms.untracked.string('HiForestEDM.root'),
     outputCommands = cms.untracked.vstring(
         'keep *',
         # drop aliased products
         'drop *_akULPu3PFJets_*_*',
         'drop *_akULPu4PFJets_*_*',
         )
     )

#process.output_path = cms.EndPath(process.output)

###############################################################################

#########################
# Event Selection
#########################

process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
process.pclusterCompatibilityFilter = cms.Path(process.clusterCompatibilityFilter)
process.pprimaryVertexFilter = cms.Path(process.primaryVertexFilter)
process.pBeamScrapingFilter = cms.Path(process.beamScrapingFilter)
process.collisionEventSelectionAOD = cms.Path(process.collisionEventSelectionAOD)
process.collisionEventSelectionAODv2 = cms.Path(process.collisionEventSelectionAODv2)

process.load('HeavyIonsAnalysis.Configuration.hfCoincFilter_cff')
#process.phfCoincFilter1Th3 = cms.Path(process.hfCoincFilterTh3)
#process.phfCoincFilter2Th3 = cms.Path(process.hfCoincFilter2Th3)
#process.phfCoincFilter3Th3 = cms.Path(process.hfCoincFilter3Th3)
#process.phfCoincFilter4Th3 = cms.Path(process.hfCoincFilter4Th3)
#process.phfCoincFilter5Th3 = cms.Path(process.hfCoincFilter5Th3)
#process.phfCoincFilter1Th4 = cms.Path(process.hfCoincFilterTh4)
#process.phfCoincFilter2Th4 = cms.Path(process.hfCoincFilter2Th4)
#process.phfCoincFilter3Th4 = cms.Path(process.hfCoincFilter3Th4)
#process.phfCoincFilter4Th4 = cms.Path(process.hfCoincFilter4Th4)
#process.phfCoincFilter5Th4 = cms.Path(process.hfCoincFilter5Th4)
#process.phfCoincFilter1Th5 = cms.Path(process.hfCoincFilterTh5)
#process.phfCoincFilter4Th2 = cms.Path(process.hfCoincFilter4Th2)

process.load("HeavyIonsAnalysis.VertexAnalysis.PAPileUpVertexFilter_cff")
process.pVertexFilterCutG = cms.Path(process.pileupVertexFilterCutG)
process.pVertexFilterCutGloose = cms.Path(process.pileupVertexFilterCutGloose)
process.pVertexFilterCutGtight = cms.Path(process.pileupVertexFilterCutGtight)
process.pVertexFilterCutGplus = cms.Path(process.pileupVertexFilterCutGplus)
process.pVertexFilterCutE = cms.Path(process.pileupVertexFilterCutE)
process.pVertexFilterCutEandG = cms.Path(process.pileupVertexFilterCutEandG)

process.load('HeavyIonsAnalysis.JetAnalysis.EventSelection_cff')
process.pHBHENoiseFilterResultProducer = cms.Path(process.HBHENoiseFilterResultProducer)
process.HBHENoiseFilterResult = cms.Path(process.fHBHENoiseFilterResult)
process.HBHENoiseFilterResultRun1 = cms.Path(process.fHBHENoiseFilterResultRun1)
process.HBHENoiseFilterResultRun2Loose = cms.Path(process.fHBHENoiseFilterResultRun2Loose)
process.HBHENoiseFilterResultRun2Tight = cms.Path(process.fHBHENoiseFilterResultRun2Tight)
process.HBHEIsoNoiseFilterResult = cms.Path(process.fHBHEIsoNoiseFilterResult)

process.pAna = cms.EndPath(process.skimanalysis)

from HLTrigger.Configuration.CustomConfigs import MassReplaceInputTag
process = MassReplaceInputTag(process,"offlinePrimaryVertices","offlinePrimaryVerticesRecovery")
process.offlinePrimaryVerticesRecovery.oldVertexLabel = "offlinePrimaryVertices"

if cleanJets == True:
    from HLTrigger.Configuration.CustomConfigs import MassReplaceInputTag
    process = MassReplaceInputTag(process,"particleFlow","filteredParticleFlow")                                                                                                               
    process.filteredParticleFlow.PFCandidates  = "particleFlow"

###############################################################################

# no screen text output
#process.MessageLogger = cms.Service("MessageLogger",
#                          destinations = cms.untracked.vstring('detailedInfo'),
#                          categories = cms.untracked.vstring('eventNumber'),
#                          detailedInfo = cms.untracked.PSet(eventNumber = cms.untracked.PSet(reportEvery = cms.untracked.int32(1000))),
#                          )

process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)

# Customization
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltfilter = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltfilter.HLTPaths = ["HLT_HIUPC_SingleEG5_NotMBHF2AND_v1"]  

process.superFilterPath = cms.Path(process.hltfilter)
process.skimanalysis.superFilters = cms.vstring("superFilterPath")      

for path in process.paths:
    getattr(process,path)._seq = process.hltfilter * getattr(process,path)._seq

